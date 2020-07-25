FROM python:3.8.4-slim

WORKDIR /app

COPY shakesphere-0.1.0-py3-none-any.whl .

RUN python -m pip install shakesphere-0.1.0-py3-none-any.whl

EXPOSE 8080

CMD [ "python", "-m", "shakesphere", "--docker" ]
