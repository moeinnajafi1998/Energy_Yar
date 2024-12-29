FROM python:3.11-slim

# Install system dependencies
# RUN apt-get update && apt-get install -y \
#     unixodbc-dev \
#     curl \
#     gnupg \
#     apt-transport-https


ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .