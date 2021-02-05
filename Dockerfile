FROM alpine
CMD ["echo", "hello world!"]

FROM ubuntu:20.04
RUN apt-get update && apt-get install -y \git \curl \python3.8 \python3-pip \vim

FROM python:3.8
COPY requirements.txt .
ADD script.py /
RUN pip3 install -r requirements.txt
CMD [ "python", "script.py" ]