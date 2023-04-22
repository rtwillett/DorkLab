# FROM nginx:1.23.4-alpine
FROM python:3.11-alpine

WORKDIR app/

COPY app/ /app


RUN apk add --no-cache --virtual .build-deps \
    build-base python3-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && python -m spacy download en_core_web_lg

CMD python -m gunicorn --bind 0.0.0.0:5000 app:app