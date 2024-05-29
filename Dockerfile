FROM python:3.11.6-alpine3.18
LABEL maintainer="mykola22dubyna@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN pip install bcrypt
RUN flask db migrate
RUN flask db upgrade
CMD ["flask", "run", "--host=0.0.0.0"]
