# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import link
import utila

import viewo_api.user.data
import viewo_api.user.serialize


def user_update(user: 'User', verify=False) -> bool:
    path = viewo_api.user.data.userpath(user.userid, verify=verify)
    if not path:
        return False
    dumped = viewo_api.user.serialize.dump_user(user)
    # TODO: NOT THREAD SAFE
    utila.file_replace(path, dumped)
    return True


def user_append_document(userid: str, documentid: str) -> bool:
    if userid == link.PUBLIC_OWNER:
        # do not add public document to public user
        return False
    user = viewo_api.user.data.user_fromid(userid)
    user.append_document(documentid)
    user_update(user)
    return True
