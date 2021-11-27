# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import pytest
import utilatest

import viewo_api.visitor


@pytest.fixture
def client():
    app = flask.Flask(__name__)

    @app.route('/')
    def client_instance():
        result = viewo_api.visitor.request()
        return str(result), 200

    instance = app.test_client()
    with app.app_context():
        yield instance


def test_request(client):  # pylint:disable=W0621
    response = utilatest.decode(client.get('/'))
    assert 'Env(hashed=' in response
    assert "ip='NO_REMOTE_ADDR', agent='werkzeug/2.0.0'" in response
