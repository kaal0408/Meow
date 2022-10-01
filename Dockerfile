FROM debian:latest
FROM nikolaik/python-nodejs:python3.9-nodejs17
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash start.sh
CMD python3 -m Meow
