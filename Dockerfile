FROM debian:latest

FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt install git curl python3-pip ffmpeg -y

# installing NodeJs
RUN apt-get install -y nodejs
RUN npm i -g npm
# Done🤓

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash start.sh
CMD python3 -m Meow
