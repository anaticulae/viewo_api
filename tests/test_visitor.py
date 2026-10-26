# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilotest


def test_request(client):  # pylint:disable=W0621
    response = utilotest.decode(client.get('/return_request'))
    assert 'Env(hashed=' in response
    # assert "agent='Werkzeug/3.1.8', method='GET', path='/return_request'" in response
    assert "agent='Werkzeug/" in response
    assert "', method='GET', path='/return_request'" in response
