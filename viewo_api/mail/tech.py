# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import viewo_api
import viewo_api.config

MESSAGE_NEW_SUBJECT = 'New Customer'
MESSAGE_NEW_BODY = """\
New customer on the line!

{data}
"""


def send_upload_info(data: dict = None):
    if viewo_api.config.EMAIL_CUSTOMER_NEW is None:
        msg = 'CONFIGURE: CHANIA_CUSTOMER_NEW could not send_upload_info'
        utila.error(msg)
        return
    data = utila.dict_dump(data) if data else ''
    body = MESSAGE_NEW_BODY.format(data=data)
    viewo_api.send_mail(
        recipient=viewo_api.config.EMAIL_CUSTOMER_NEW,
        subject=MESSAGE_NEW_SUBJECT,
        body=body,
    )


def send_server_status():
    pass


def send_login_request():
    """Send token before login into admin area."""
