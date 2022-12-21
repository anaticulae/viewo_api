# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import flask
import utila

Access = collections.namedtuple('Access', 'ip, agent')
Env = collections.namedtuple(
    'Env',
    'hashed, time, ip, agent, method, path, data, dictum',
)


def request() -> Env:
    env = flask.request.environ
    if not env:
        return None
    ip = env.get('REMOTE_ADDR', 'NO_REMOTE_ADDR')
    agent = env.get('HTTP_USER_AGENT', 'NO_HTTP_USER_AGENT')
    hashed = user_hash(ip, agent)
    method = env.get('REQUEST_METHOD', 'NO_USER_AGENT')
    path = env.get('PATH_INFO', 'NO_PATH_INFO')
    data = env.get('QUERY_STRING', 'NO_QUERY_STRING')
    data = oneline(data)
    time = utila.now()
    try:
        dictum = flask.request.form.to_dict()
    except OSError:
        utila.error(f'invalid/incomplete request: {flask.request}')
        utila.debug(vars(flask.request))
        dictum = {}
    return Env(hashed, time, ip, agent, method, path, data, dictum)


def user_hash(ip, agent) -> int:
    return hash(f'{ip}:{agent}')


def access(env: Env):
    return Access(env.ip, env.agent)


def user_current() -> int:
    current = request()
    hashed = user_hash(current.ip, current.agent)
    return hashed


def oneline(data, limit: int = 256):
    r"""Remove newlines and shrink content to `limit` to avoid logging to
    mutch data.

    >>> oneline('first\nnewline')
    'first%NL%newline'
    """
    data = data.replace('\r\n', '%WNL%')
    data = data.replace('\n', '%NL%')
    data = data.replace(' ', '%WS%')
    data = data[0:limit]
    return data
