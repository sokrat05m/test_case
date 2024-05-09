FROM python:3.12-alpine3.18
ARG DJANGO_ENV
ENV DJANGO_ENV=${DJANGO_ENV} \

    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.2



COPY market_case /market_case
#COPY market_case/pyproject.toml poetry.lock* /market_case/
RUN pip install poetry
WORKDIR /market_case
EXPOSE 8000


RUN apk add postgresql-client build-base postgresql-dev
RUN poetry install
RUN adduser --disabled-password sokrat
USER sokrat