FROM python:3.11.3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install netcat -y
RUN apt upgrade -y
RUN apt install default-libmysqlclient-dev build-essential python3-dev -y
#RUN apt install net-tools -y
RUN pip install --upgrade pip
RUN pip install poetry


COPY ./pyproject.toml /usr/src/app/
COPY ./poetry.lock /usr/src/app/

# RUN poetry install --no-root
RUN poetry install --no-root

COPY . /usr/src/app/
