# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http
import os

import flask
import flask_login
import pytest

import viewo_api.mail.create
import viewo_api.message
import viewo_api.visitor


@pytest.fixture
def app(testdir):
    config = create_config(testdir.tmpdir)
    appx = flask.Flask(__name__)
    appx.secret_key = os.urandom(64)
    appx.config.update(config)
    return appx


@pytest.fixture
def client(app):  # pylint:disable=W0621
    loginmanager = flask_login.LoginManager(app)
    loginmanager._user_callback = lambda x: viewo_api.FlaskUser(identifier=x)  # pylint:disable=W0212

    @app.route('/return_request')
    def client_instance():
        result = viewo_api.visitor.request()
        return str(result), 200

    @app.route('/login', methods=['POST'])
    def login():
        send = flask.request.form.to_dict()
        if not viewo_api.login(send['user'], send['password']):
            return str('wrong'), http.HTTPStatus.FORBIDDEN
        return str('erfolgreich'), 200

    @app.route('/logout')
    def logout():
        viewo_api.logout()
        return viewo_api.message.success('erfolgreich')

    with app.app_context():
        yield app.test_client()


@pytest.fixture
def client_mail(app):  # pylint:disable=W0621
    viewo_api.mail.create.register(app)
    with app.app_context():
        yield app.test_client()


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
