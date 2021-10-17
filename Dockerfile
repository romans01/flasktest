FROM ubuntu:latest

MAINTAINER Roman Smirnov

RUN apt-get update -y
RUN apt-get -y install python3
RUN apt-get install -y python3-pip python-dev build-essential
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT python3 app.py
