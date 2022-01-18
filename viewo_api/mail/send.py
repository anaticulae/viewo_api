# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_mail

import viewo_api.config


def send_mail(
    recipient: str,
    subject: str,
    body: str,
    author: str = viewo_api.config.EMAIL_NO_AUTHOR,
):
    msg = flask_mail.Message(
        recipients=[recipient],
        subject=subject,
        body=body,
        sender=author.value,
    )
    flask.current_app.mail.send(msg)
    # threading.Thread(
    #     target=send_async,
    #     args=[flask.current_app, msg],
    # ).start()


# def send_async( msg):
#     with app.app_context():
#         app.mail.send(msg)
