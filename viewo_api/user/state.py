# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask_login

import viewo_api.message
import viewo_api.user.data


def login(userid: str, password: str, publicpassword: bool = False):
    if not viewo_api.password_verify(userid, password):
        return False
    flask_login.login_user(viewo_api.FlaskUser(userid))
    if publicpassword:
        viewo_api.password_public_set(password)
    viewo_api.message.flash('Login erfolgreich.')
    return True


def logout():
    flask_login.logout_user()
    # remove public password
    viewo_api.password_public_set('')
    viewo_api.message.flash('Logout erfolgreich.')
