#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

from viewo_api.mail.send import send_mail
from viewo_api.mail.tech import send_upload_info
from viewo_api.message import bad
from viewo_api.message import internal
from viewo_api.message import notfound
from viewo_api.message import success
from viewo_api.user.config import userspath
from viewo_api.user.create import create_user
from viewo_api.user.data import FlaskUser
from viewo_api.user.data import User
from viewo_api.user.data import hash_email
from viewo_api.user.data import user_fromid
from viewo_api.user.data import userlist_raw
from viewo_api.user.data import userpublic_fromid
from viewo_api.user.password import password_generate
from viewo_api.user.password import password_public_set
from viewo_api.user.password import password_valid
from viewo_api.user.password import password_verify
from viewo_api.user.password import username_valid
from viewo_api.user.state import login
from viewo_api.user.state import logout
from viewo_api.user.update import user_append_document
from viewo_api.user.update import user_email_update
from viewo_api.user.update import user_update
from viewo_api.utils import json
from viewo_api.visitor import access
from viewo_api.visitor import oneline
from viewo_api.visitor import request
from viewo_api.visitor import user_current
from viewo_api.visitor import user_hash

__version__ = '0.11.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
