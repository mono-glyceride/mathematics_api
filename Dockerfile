FROM python:alpine

WORKDIR /app
ENV FLASK_APP=app

COPY ./app /app
COPY requirements.txt /app/

RUN apk add --update \
&& apk add git \
&& apk add bash curl nodejs
RUN pip install -r requirements.txt
RUN curl https://cli-assets.heroku.com/install.sh | sh

CMD ["python", "app.py"]
