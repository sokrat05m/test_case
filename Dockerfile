FROM python:3.12-alpine3.18


COPY requirements.txt /temp/requirements.txt
COPY market_case /market_case
WORKDIR /market_case
EXPOSE 8000 465 80

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user