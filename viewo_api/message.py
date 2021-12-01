# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask

import viewo_api


def success(message: str = 'completed', **args):
    result = viewo_api.json({
        'message': message,
        **args,
    })
    return result, 200


def notfound(message: str):
    result = viewo_api.json({
        'error': 'not found',
        'message': message,
    })
    return result, 404


def bad(message: str):
    result = viewo_api.json({
        'error': 'bad request',
        'message': message,
    })
    return result, 400


def internal(message: str):
    result = viewo_api.json({
        'error': 'internal',
        'message': message,
    })
    return result, 500


def flash(message: str):
    flask.flash(message)
