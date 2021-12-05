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
def client(testdir):
    config = create_config(testdir.tmpdir)
    app = flask.Flask(__name__)
    app.config.update(config)

    @app.route('/return_request')
    def client_instance():
        result = viewo_api.visitor.request()
        return str(result), 200

    instance = app.test_client()
    with app.app_context():
        yield instance


def create_config(tmpdir):
    for item in 'todo ready common'.split():
        tmpdir.mkdir(item)
    # create the app with common test config
    config = {
        'TESTING': True,
        'COMMON': tmpdir.join('common'),
        'TODO': tmpdir.join('todo'),
        'READY': tmpdir.join('ready'),
    }
    return config
