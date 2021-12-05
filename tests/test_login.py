# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http

import utilatest

import viewo_api
import viewo_api.user.state

PASSWORD = 'helmut1337'  # nosec


def test_login_logout(client):  # pylint:disable=W0613
    user = viewo_api.create_user(password=PASSWORD)
    utilatest.apipost(
        client,
        '/login',
        data=dict(user=user.userid, password=PASSWORD),
    )
    utilatest.apicall(client, '/logout')


def test_login_wrong_password(client):  # pylint:disable=W0613
    user = viewo_api.create_user(password=PASSWORD)
    utilatest.apipost(
        client,
        '/login',
        data=dict(user=user.userid, password='wrong'),  # nosec
        expected=http.HTTPStatus.FORBIDDEN,
    )
