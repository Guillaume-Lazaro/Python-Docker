FROM alpine
RUN apk add --update-cache \
    python3 \
    vim \
    && rm -rf /var/cache/apk/*
# RUN apt-get update && apt-get install -y \git \curl \python3.8 \python3-pip \vim

FROM python:3.8
COPY requirements.txt .
COPY app /app
ADD script.py /

RUN pip3 install -r requirements.txt
CMD [ "python", "app/app_test.py" ]