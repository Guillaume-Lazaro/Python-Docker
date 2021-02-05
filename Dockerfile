FROM alpine
EXPOSE 5000
RUN apk add --update --no-cache \
    python3 \
    py3-pip \
    vim \
    && rm -rf /var/cache/apk/*
# RUN apt-get update && apt-get install -y \git \curl \python3.8 \python3-pip \vim

# FROM python:3.8
COPY requirements.txt .
COPY app /app/
ADD script.py /

RUN pip3 install -r requirements.txt
CMD [ "python3", "app/app_test.py" ]