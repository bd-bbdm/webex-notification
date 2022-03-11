FROM python:3.10-alpine as build

WORKDIR /src

COPY webhook webhook
COPY setup.py .

RUN python setup.py bdist_wheel

FROM python:3.10-alpine

COPY *.sh /


ARG USER_ID="1997"
ARG GROUP_ID="1995"
ARG USER_NAME="webhook"

COPY --from=build /src/dist/webEX_notify-_module._webhook.version_.from._src_webhook_version.py_-py3-none-any.whl /tmp

RUN addgroup -S -g "${GROUP_ID}" "${USER_NAME}" \
    && adduser -u "${USER_ID}" -G "${USER_NAME}" -D "${USER_NAME}" \
    && apk update \
    && apk upgrade \
    && apk add bash jq \
    && rm -rf /var/cache/apk/* \
    && chmod +x /*.sh \
    && pip install /tmp/webEX_notify-_module._webhook.version_.from._src_webhook_version.py_-py3-none-any.whl
USER 1997

ENTRYPOINT ["/entrypoint.sh"]
