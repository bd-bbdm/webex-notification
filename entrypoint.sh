#!/usr/bin/env bash

export COMMIT_MESSAGE=$(cat "$GITHUB_EVENT_PATH" | jq -r '.commits[-1].message')
export GITHUB_ACTOR=${MSG_AUTHOR:-"$GITHUB_ACTOR"}
export WEBEX_TITLE="Message"

PR_SHA=$(cat $GITHUB_EVENT_PATH | jq -r .pull_request.head.sha)
[[ 'null' != $PR_SHA ]] && export GITHUB_SHA="$PR_SHA"

if [[ -z "$WEBEX_MESSAGE" ]]; then
	export WEBEX_MESSAGE="$COMMIT_MESSAGE"
fi

webEX_notify
