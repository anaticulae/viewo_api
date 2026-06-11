# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilo

import viewo_api.config
import viewo_api.user.data
import viewo_api.user.password
import viewo_api.user.update


def create_user(password: str, userid: str = None):
    # validate password
    password = viewo_api.user.password.hashed(password)
    # generate new random user name
    if not userid:
        userid = utilo.tmpname(viewo_api.config.USER_LENGTH)
        while os.path.exists(viewo_api.user.data.userpath(userid, False)):
            userid = utilo.tmpname(viewo_api.config.USER_LENGTH)
    new = viewo_api.user.data.User(userid=userid, password=password)
    # write to user database
    viewo_api.user.update.user_update(new)
    return new
