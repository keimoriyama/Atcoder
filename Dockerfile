FROM gcc:latest
LABEL maintainer "kei <keischwiiz@gmail.com>"

RUN apt-get update && apt-get install -y 
ADD . /code
WORKDIR /code
