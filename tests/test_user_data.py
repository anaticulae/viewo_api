# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================


import viewo_api.user.data


def test_dump_and_load_user():
    user = viewo_api.user.data.User(
        email='simpleone@uni.edu',
        documents=['ASDSA232GF', 'XA333333'],
        payed=1000,
        userid='AHF2332LL',
    )
    dumped = viewo_api.user.data.dump_user(user)
    loaded = viewo_api.user.data.load_user(dumped)
    assert loaded == user


def test_dump_users(testdir):
    outpath = str(testdir)
    assert not viewo_api.user.data.load_users(outpath)
    users = [  #nosec
        viewo_api.user.data.User(
            email='hans@dampf.eu',
            password='securehash',
            documents=[
                'ADS2399BBD',
                '2F2ADSL23N99BBD',
            ],
            payed=100,
            userid='ACABOFC',
        ),
        viewo_api.user.data.User(
            email=None,
            password=None,
            documents=['C0C0C0'],
            payed=None,
            userid='FF00FF',
        ),
    ]
    viewo_api.user.data.dump_users(users, outpath)
    loaded = viewo_api.user.data.load_users(outpath)
    assert loaded == users
