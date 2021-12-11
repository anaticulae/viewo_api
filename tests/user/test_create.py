# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import viewo_api

PASSWORD = 'helmut1337'  # nosec


def test_user_create_verify(client):  # pylint:disable=W0613
    user = viewo_api.create_user(password=PASSWORD)
    assert viewo_api.password_verify(userid=user.userid, password=PASSWORD)
