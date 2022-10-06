# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import viewo_api
import viewo_api.config

AUTHOR = 'helm@helm.com'


@pytest.mark.xfail(reason='install aiosmtpd')
def test_send_new_customer(client_mail, monkeypatch):
    smtpserver = client_mail[1]
    assert not smtpserver.outbox
    data = dict(pages=1024, text='hohoh')
    with monkeypatch.context() as context:
        context.setattr(viewo_api.config, 'EMAIL_CUSTOMER_NEW', AUTHOR)
        viewo_api.send_upload_info(data=data)
    assert smtpserver.outbox
