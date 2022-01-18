# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import viewo_api.mail.app
import viewo_api.mail.send


def test_send(client_mail):  # pylint:disable=W0613
    smtpserver = client_mail[1]
    assert not smtpserver.outbox
    viewo_api.mail.send.send_mail(
        recipient='helmut@helmut.com',
        subject='Titel',
        body='Content',
    )
    assert smtpserver.outbox
    message = smtpserver.outbox[0]
    assert 'helmut@helmut.com' in message.values()
