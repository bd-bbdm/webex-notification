
import json
import logging
import os
import sys
from typing import Any

import requests as rq

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

env_webhook = "WEBHOOK"
env_title = "TITLE"
env_message = "MESSAGE"
env_github_actor = "ACTOR"


def webEXEnv(key: str) -> str:
    return os.getenv(f'WEBEX_{key}', '')


def githubEnv(key: str) -> str:
    return os.getenv(f'GITHUB_{key}', '')


def error(msg: str, *args):
    logger.error(msg, *args)
    sys.exit(1)


def main():
    endpoint = webEXEnv(env_webhook)
    if endpoint == "":
        error("URLは必須項目です")
    message = webEXEnv(env_message)
    if message == "":
        error('メッセージは必須項目です')

    if githubEnv('WORKFLOW').startswith('.github'):
        os.environ['GITHUB_WORKFLOW'] = "Link to action run"
    long_sha = githubEnv('SHA')
    commit_sha = long_sha[0:6]

    github_server = githubEnv('SERVER_URL')
    repository = githubEnv('REPOSITORY')
    title = webEXEnv(env_title)
    ref = githubEnv('REF')
    event = githubEnv('EVENT_NAME')
    action_url = f"[{githubEnv('WORKFLOW')}]({github_server}/{repository}/commit/{long_sha}/checks)"
    commit = f"[{commit_sha}]({github_server}/{repository}/commit/{long_sha})"
    author_name = githubEnv(env_github_actor)
    author_link = f'[{author_name}]({github_server}/{author_name})'

    msg = f"""# {title}

## {message}

### Attachment

- Author: {author_link}
- Ref: {ref}
- Event: {event}
- Actions URL: {action_url}
- Commit: {commit}

"""
    result = send(endpoint, {
        "markdown": msg,
    })
    return result


def send(endpoint: str, message: Any) -> bool:
    res = rq.post(endpoint, data=json.dumps(message), headers={
        'Content-Type': 'application/json'
    })
    return res.status_code >= 200 and res.status_code < 300
