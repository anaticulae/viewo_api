# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import viewo_api.config

# TODO: HOLY SECURE VALUE # CONFIGO!
PASSWORD_SALT = 'THISISSALT'  # nosec
PASSWORD_RANDOM_LENGTH = 16

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 64

USER_LENGTH = 16  # TODO: HOLY VALUE


def userpath():
    result = os.path.join(viewo_api.config.common(), 'users')
    os.makedirs(result, exist_ok=True)
    return result
