FROM python:3.8

WORKDIR ./app
COPY ./app .

RUN pip install -r requirements.txt

CMD flask  --app flask_example run --host=0.0.0.0 -p 8001

