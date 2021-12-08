FROM python:3.10.0

RUN apt update && \
apt -y install locales && \
localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV TZ="Asia/Tokyo" \
TERM=xter