FROM python:3.11

WORKDIR /backend

RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean

COPY requirments.txt ./

RUN python3 -m pip install -U pip
RUN python3 -m pip install -U setuptools wheel
RUN python3 -m ensurepip --upgrade

RUN python3 -m pip install --use-pep517 -r requirments.txt

COPY . .
