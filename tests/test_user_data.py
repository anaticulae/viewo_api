# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import viewo_api.user.create
import viewo_api.user.data


def test_user_list_create_list(client):  # pylint:disable=W0613
    users = viewo_api.user.data.userlist()
    assert not users
    password = 'helmut1337'
    viewo_api.user.create.create_user(password=password)
    users = viewo_api.user.data.userlist()
    assert len(users) == 1
