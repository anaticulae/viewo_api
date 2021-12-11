# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_mail


def register(app):
    mail = flask_mail.Mail(app)
    app.mail = mail


def configure(
    server,
    user=None,
    password=None,
    tls: bool = False,
    port: int = 587,
):
    config = flask.current_app.config
    config['MAIL_SERVER'] = server
    config['MAIL_PORT'] = port
    config['MAIL_USERNAME'] = user
    config['MAIL_PASSWORD'] = password
    config['MAIL_USE_TLS'] = tls
    config['MAIL_SUPPRESS_SEND'] = False
    flask.current_app.mail.init_app(flask.current_app)
