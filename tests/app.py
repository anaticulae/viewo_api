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

import viewo_api.visitor


@pytest.fixture
def client():
    app = flask.Flask(__name__)

    @app.route('/return_request')
    def client_instance():
        result = viewo_api.visitor.request()
        return str(result), 200

    instance = app.test_client()
    with app.app_context():
        yield instance
