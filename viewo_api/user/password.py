# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import viewo_api.user.config


class PasswordError(ValueError):
    pass


class PasswordTooShort(PasswordError):
    pass


class PasswordTooLong(PasswordError):
    pass


def valid(password: str) -> bool:
    """\
    >>> valid('short')
    Traceback (most recent call last):
        ...
    viewo_api.user.password.PasswordTooShort

    >>> valid('VeryLongPassword1337')
    True
    """
    if password is None:
        return False
    password = str(password)
    if len(password) < viewo_api.user.config.PASSWORD_MIN_LENGTH:
        raise PasswordTooShort
    if len(password) > viewo_api.user.config.PASSWORD_MAX_LENGTH:
        raise PasswordTooLong
    return True


def hashed(password: str) -> str:
    valid(password)
    password = utila.secure_hash(
        password,
        salt=viewo_api.user.config.PASSWORD_SALT,
        digits=64,
    )  # pylint:disable=E1101
    return password


def generate() -> str:
    random = utila.tmpname(viewo_api.user.config.PASSWORD_RANDOM_LENGTH)
    return random
