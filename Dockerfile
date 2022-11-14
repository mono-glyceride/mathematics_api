FROM python:alpine

WORKDIR /app
ENV FLASK_APP=app

COPY ./app /app

RUN pip install Flask

CMD ["python", "app.py"]
