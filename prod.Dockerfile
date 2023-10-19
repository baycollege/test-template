FROM debian:bookworm-slim AS builder
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes cron python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip \
    FROM builder AS builder-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM builder-venv AS tester

COPY . /app
WORKDIR /app
RUN /venv/bin/pytest

FROM gcr.io/distroless/python3-debian11 AS runner
COPY --from=tester /venv /venv
COPY --from=tester /app /app

WORKDIR /app

RUN crontab crontab

ENTRYPOINT ["crond", "-d"]
USER 1001

LABEL name={NAME}
LABEL version={VERSION}
