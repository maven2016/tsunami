FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get -y update && apt-get -y install \
    iputils-ping \
    && pip install boto3 

CMD [ "python3" ]
