FROM gcc:latest

RUN apt-get update && apt-get install -y 
ADD . /code
WORKDIR /code
