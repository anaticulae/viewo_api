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

import flask
import flask_login
import utila
import yaml

import viewo_api.user.config
import viewo_api.user.password


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


def user_raw(user: User) -> dict:
    result = {
        'documents': user.documents,
        'userid': user.userid,
        'payed': user.payed,
    }
    return result


def load_users(path: str) -> Users:
    assert os.path.exists(path), path

    users = utila.file_list(path)
    users = utila.files_sort(users)

    loaded = [load_user(os.path.join(path, item)) for item in users]
    return loaded


def dump_users(users: Users, path: str):
    assert os.path.exists(path), path

    for user in users:
        dumped = dump_user(user)
        outpath = os.path.join(path, user.userid)
        utila.file_replace(outpath, dumped)


def load_user(path: str) -> User:
    loaded = utila.yaml_from_raw_or_path(path)
    result = User(**loaded)
    return result


def dump_user(user: User) -> str:
    raw = vars(user)
    dumped = yaml.safe_dump(raw)
    return dumped


def user_fromid(userid: str) -> User:
    path = userpath(userid)
    if not path:
        return None
    loaded = load_user(path)
    return loaded


def userpath(userid: int, verify: bool = False) -> str:
    result = os.path.join(viewo_api.user.config.userpath(), userid)
    if verify and not os.path.exists(result):
        return None
    return result


def verify_password(userid: str, password: str) -> bool:
    user = user_fromid(userid)
    if not user:
        return False
    try:
        password = viewo_api.user.password.hashed(password)
    except viewo_api.user.password.PasswordError:
        return False
    return password == user.password


def public_password_set(password: str):
    # TODO: CHECK FOR SECURITY ISSUES
    flask.globals.session['password_raw'] = password


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
