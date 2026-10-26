# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import viewo_api
import viewo_api.user.data
import viewo_api.user.serialize


def user_update(user: 'User', verify=False) -> bool:
    path = viewo_api.user.data.userpath(user.userid, verify=verify)
    if not path:
        return False
    dumped = viewo_api.user.serialize.dump_user(user)
    # TODO: NOT THREAD SAFE
    utilo.file_replace(path, dumped)
    return True


PUBLIC_OWNER = '00000000'


def user_append_document(userid: str, documentid: str) -> bool:
    # TODO: REPLACE LATER
    if userid == PUBLIC_OWNER:
        # if userid == link.PUBLIC_OWNER:
        # do not add public document to public user
        return False
    user = viewo_api.user.data.user_fromid(userid)
    user.append_document(documentid)
    user_update(user)
    return True


def user_email_update(email: str, userid: str = None) -> bool:
    user = viewo_api.user.data.user_fromid(userid)
    if not user:
        return False
    user.email = viewo_api.hash_email(email)
    # write to user database
    user_update(user)
    return True
