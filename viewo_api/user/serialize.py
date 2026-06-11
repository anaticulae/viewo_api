# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilo

import viewo_api.user.data


def user_raw(user: 'User') -> dict:
    result = {
        'documents': user.documents,
        'userid': user.userid,
        'payed': user.payed,
    }
    return result


def dump_users(users: 'Users', path: str):
    assert os.path.exists(path), path
    for user in users:
        dumped = dump_user(user)
        outpath = os.path.join(path, user.userid)
        utilo.file_replace(outpath, dumped)


def load_users(path: str) -> 'Users':
    assert os.path.exists(path), path
    files = utilo.file_list(path)
    files = utilo.files_sort(files)
    loaded = [load_user(os.path.join(path, item)) for item in files]
    return loaded


def dump_user(user: 'User') -> str:
    raw = vars(user)
    dumped = utilo.yaml_dump(raw)
    return dumped


def load_user(path: str) -> 'User':
    loaded = utilo.yaml_load(path)
    result = viewo_api.user.data.User(**loaded)
    return result
