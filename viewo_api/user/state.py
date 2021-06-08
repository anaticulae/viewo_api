# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask_login

import viewo_api.message
import viewo_api.user.data


def login(userid: str, password: str):
    if not viewo_api.user.data.verify_password(userid, password):
        return False
    flask_login.login_user(viewo_api.FlaskUser(userid))
    viewo_api.user.data.public_password_set(password)
    viewo_api.message.flash('Login erfolgreich.')
    return True


def logout():
    flask_login.logout_user()
    # remove public password
    viewo_api.user.data.public_password_set('')
    viewo_api.message.flash('Logout erfolgreich.')
