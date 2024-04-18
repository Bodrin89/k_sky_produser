FROM python:3.11-slim

ENV POETRY_VERSION=1.8.2
#RUN apt update && apt install -y curl
RUN apt update && apt install -y netcat-openbsd


RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi
COPY . .

