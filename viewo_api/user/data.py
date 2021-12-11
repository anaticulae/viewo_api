# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import os
import typing

import flask_login
import utila

import viewo_api.user.config
import viewo_api.user.password
import viewo_api.user.serialize


@dataclasses.dataclass(unsafe_hash=True)
class User:
    email: str = None
    password: str = None
    documents: list = dataclasses.field(default_factory=list)
    payed: int = None
    userid: str = None

    def append_document(self, documentid: str):
        assert documentid not in self.documents  # pylint:disable=E1135
        self.documents.append(documentid)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.documents[index]  # pylint:disable=E1136


Users = typing.List[User]


def user_fromid(userid: str) -> User:
    path = userpath(userid, verify=True)
    if not path:
        # try to find user via email
        user = user_from_email(userid)
        return user
    if not path:
        return None
    loaded = viewo_api.user.serialize.load_user(path)
    return loaded


def user_from_email(email: str) -> User:
    email = hash_email(email)
    for user in users():
        if user.email != email:
            continue
        return user
    return None


def userpath(userid: int, verify: bool = False) -> str:
    result = os.path.join(viewo_api.user.config.userspath(), userid)
    if verify and not os.path.exists(result):
        return None
    return result


def users():
    upath = viewo_api.user.config.userspath()
    common_user = viewo_api.user.serialize.load_users(upath)
    return common_user


def userlist_raw():
    upath = viewo_api.user.config.userspath()
    common_user = viewo_api.user.serialize.load_users(upath)
    raw = [viewo_api.user.serialize.user_raw(item) for item in common_user]
    return raw


def userpublic_fromid(userid: str) -> dict:
    """Returns public data which are not security/data privacy
    relevant."""
    user = user_fromid(userid)
    if not user:
        return None
    result = {
        'user': userid,
        'documents': list(user.documents),
    }
    if user.email:
        # TODO: IS THIS A GOOD IDEA?
        # TODO: VERIFY BEFORE RELEASE XXX
        result['email'] = user.email
    if user.payed is not None:
        result['payed'] = user.payed
    return result


def hash_email(email: str):
    """\
    >>> hash_email('toy@roy.com')
    '...'
    """
    email = utila.secure_hash(
        email,
        salt=viewo_api.config.EMAIL_SALT,
        digits=viewo_api.config.EMAIL_DIGITS,
    )
    return email


@dataclasses.dataclass
class FlaskUser(flask_login.UserMixin):
    identifier: str = None

    def get_id(self):
        return self.identifier

    @property
    def payed(self):
        user = user_fromid(self.identifier)
        if not user:
            return 0
        return user.payed

    @property
    def is_admin(self):
        return False
