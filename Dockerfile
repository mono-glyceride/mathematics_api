FROM python:alpine

WORKDIR /app
ENV FLASK_APP=app

COPY ./app /app

RUN apk add --update \
&& apk add git
RUN pip install Flask
RUN pip install gunicorn
RUN apk add bash curl nodejs
RUN curl https://cli-assets.heroku.com/install.sh | sh

CMD ["python", "app.py"]
