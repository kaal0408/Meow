FROM debian:latest
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
ENV PYTHONUNBUFFERED=1
COPY . .
RUN bash start.sh
CMD python3 -m Meow
