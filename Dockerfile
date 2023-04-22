# FROM nginx:1.23.4-alpine
FROM python:3.11

WORKDIR app/

COPY app/ /app

# EXPOSE 5000
RUN pip install -r requirements.txt 
RUN python -m spacy download en_core_web_lg
CMD python -m gunicorn --bind 0.0.0.0:5000 app:app