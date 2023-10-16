FROM python:3.11.5-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends --yes vim netcat
