# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configos
import flask

PASSWORD_SALT = configos.HV_STR(default='THISISSALT')

PASSWORD_DIGITS = configos.HV_INT_PLUS(default=64)

PASSWORD_RANDOM_LENGTH = configos.HV_INT_PLUS(default=16)

PASSWORD_MIN_LENGTH = configos.HV_INT_PLUS(default=8)
PASSWORD_MAX_LENGTH = configos.HV_INT_PLUS(default=64)

USER_LENGTH = configos.HV_INT_PLUS(default=16)

EMAIL_SALT = configos.HV_STR(default='EMAILNOGMAIL')

EMAIL_DIGITS = configos.HV_INT_PLUS(default=64)

EMAIL_NO_AUTHOR = configos.HV_STR(default='postkasten@checkitweg.de')

EMAIL_SERVER = configos.HV_STR(default='guardian@checkitweg.de')
# inform admin about new customer
EMAIL_CUSTOMER_NEW = configos.env('CHANIA_CUSTOMER_NEW', default=None)


def common():
    return flask.current_app.config['COMMON']


def todo():
    return flask.current_app.config['TODO']


def ready():
    return flask.current_app.config['READY']


configos.todo = todo
configos.ready = ready
configos.share = common
