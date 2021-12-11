# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import utila

import viewo_api.config
import viewo_api.user


class PasswordError(ValueError):
    pass


class PasswordTooShort(PasswordError):
    pass


class PasswordTooLong(PasswordError):
    pass


def password_valid(password: str) -> bool:
    """\
    >>> password_valid('short')
    Traceback (most recent call last):
        ...
    viewo_api.user.password.PasswordTooShort

    >>> password_valid('VeryLongPassword1337')
    True
    """
    if password is None:
        return False
    password = str(password)
    if len(password) < viewo_api.config.PASSWORD_MIN_LENGTH:
        raise PasswordTooShort
    if len(password) > viewo_api.config.PASSWORD_MAX_LENGTH:
        raise PasswordTooLong
    return True


def hashed(password: str) -> str:
    """\
    >>> len(hashed('nononono'))
    64
    """
    password_valid(password)
    password = utila.secure_hash(
        password,
        salt=viewo_api.config.PASSWORD_SALT,
        digits=viewo_api.config.PASSWORD_DIGITS,
    )
    return password


def password_generate(length=viewo_api.config.PASSWORD_RANDOM_LENGTH) -> str:
    """\
    >>> assert len(password_generate(10)) == 10
    """
    random = utila.tmpname(length)
    return random


def password_verify(userid: str, password: str) -> bool:
    user = viewo_api.user.data.user_fromid(userid)
    if not user:
        # try to select user via email
        user = viewo_api.user.data.user_from_email(userid)
    if not user:
        return False
    try:
        password = viewo_api.user.password.hashed(password)
    except viewo_api.user.password.PasswordError:
        return False
    return password == user.password


def password_public_set(password: str):
    # TODO: CHECK FOR SECURITY ISSUES
    flask.globals.session['password_raw'] = password


def username_valid(name) -> False:
    """\
    >>> username_valid('not a valid user')
    False
    >>> username_valid('012ABxxF012ABxxF')
    True
    >>> username_valid(' 12  xxx')
    False
    """
    if not len(name) == viewo_api.config.USER_LENGTH:
        return False
    return all(item.isalnum() for item in name)
