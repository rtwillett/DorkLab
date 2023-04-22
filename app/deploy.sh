#!/bin/bash

python -m spacy download en_core_web_lg
python -m gunicorn --bind 0.0.0.0:5000 app:app