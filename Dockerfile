FROM python:3.8-alpine

WORKDIR /srv
EXPOSE 8000

RUN apk add --update alpine-sdk

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /srv
