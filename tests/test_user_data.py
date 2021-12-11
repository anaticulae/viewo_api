# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import viewo_api

PASSWORD, MAIL = 'helmut1337', 'helm@helm.com'  # nosec


def test_user_list_create_list(client):  # pylint:disable=W0613
    users = viewo_api.userlist_raw()
    assert not users
    viewo_api.create_user(password=PASSWORD)
    users = viewo_api.userlist_raw()
    assert len(users) == 1


def test_user_public_fromid(client):  # pylint:disable=W0613
    user = viewo_api.create_user(password=PASSWORD)
    public = viewo_api.userpublic_fromid(userid=user.userid)
    assert not public['documents']
    user.email = MAIL
    viewo_api.user_update(user)
    public = viewo_api.userpublic_fromid(userid=user.userid)
    assert public['email'] == MAIL


def test_user_update(client):  # pylint:disable=W0613
    user = viewo_api.create_user(password=PASSWORD)
    user.email = MAIL
    viewo_api.user_update(user)
    public = viewo_api.userpublic_fromid(userid=user.userid)
    assert public['email'] == MAIL


def test_user_email_set(client):  # pylint:disable=W0613
    user = viewo_api.create_user(password=PASSWORD)
    userid = user.userid
    viewo_api.create_email(MAIL, userid=userid)
    public = viewo_api.userpublic_fromid(userid=user.userid)
    assert public['email'] == MAIL


def test_user_append_document(client):  # pylint:disable=W0613
    user = viewo_api.create_user(password=PASSWORD)
    public = viewo_api.userpublic_fromid(userid=user.userid)
    assert not public['documents']
    viewo_api.user_append_document(user.userid, '111111')
    public = viewo_api.userpublic_fromid(userid=user.userid)
    assert public['documents']
