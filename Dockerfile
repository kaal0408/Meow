FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash start.sh
CMD python3 -m Meow
