FROM python:3.7-alpine

COPY src/requirements.txt /app/requirements.txt
RUN apk update \
    && apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install -r /app/requirements.txt \
    && apk del .build-deps

COPY src/ /app/

EXPOSE 5000

WORKDIR /app
USER 1001
CMD ["/usr/local/bin/gunicorn", "autoapp:app", "-c", "/app/gunicorn.conf", "--pythonpath", "/app"]