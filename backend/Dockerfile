FROM python:3.10.0

RUN apt update && \
apt install -y git && \
apt -y install locales && \
localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV TZ="Asia/Tokyo" \
TERM=xter
