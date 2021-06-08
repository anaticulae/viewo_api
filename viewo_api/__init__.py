#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

from viewo_api.message import bad
from viewo_api.message import internal
from viewo_api.message import notfound
from viewo_api.message import success
from viewo_api.user.data import FlaskUser
from viewo_api.user.password import password_generate
from viewo_api.user.password import password_public_set
from viewo_api.user.password import password_verify
from viewo_api.user.state import login
from viewo_api.user.state import logout

__version__ = '0.6.1'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
