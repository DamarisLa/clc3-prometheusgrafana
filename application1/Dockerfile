FROM python:3.8

WORKDIR ./app
COPY ./app .

RUN pip install -r requirements.txt


CMD uwsgi --http :8000 --wsgi-file flask_example.py --callable app

