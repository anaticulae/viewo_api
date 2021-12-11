# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configo
import flask

PASSWORD_SALT = configo.HV_STR(default='THISISSALT')

PASSWORD_DIGITS = configo.HV_INT_PLUS(default=64)

PASSWORD_RANDOM_LENGTH = configo.HV_INT_PLUS(default=16)

PASSWORD_MIN_LENGTH = configo.HV_INT_PLUS(default=8)
PASSWORD_MAX_LENGTH = configo.HV_INT_PLUS(default=64)

USER_LENGTH = configo.HV_INT_PLUS(default=16)

EMAIL_SALT = configo.HV_STR(default='EMAILNOGMAIL')

EMAIL_DIGITS = configo.HV_INT_PLUS(default=64)

EMAIL_NO_AUTHOR = configo.HV_STR(default='postkasten@checkitweg.de')

EMAIL_SERVER = configo.HV_STR(default='guardian@checkitweg.de')


def common():
    return flask.current_app.config['COMMON']


def todo():
    return flask.current_app.config['TODO']


def ready():
    return flask.current_app.config['READY']


configo.todo = todo
configo.ready = ready
configo.share = common
