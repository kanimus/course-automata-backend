FROM python:3

RUN mkdir /src
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
# COPY ./start.dev.sh .
COPY /src .