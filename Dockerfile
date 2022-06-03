# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /app/

COPY ./requirements/prod.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

CMD [ "python", "/app/main.py" ]
