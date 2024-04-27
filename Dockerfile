FROM python:3.10

WORKDIR /producer/app

COPY check_producer/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY check_producer/ .
