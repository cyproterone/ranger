FROM ubuntu:latest


RUN apt update && \
    apt install -y \
    git \
    python3 python3-pip


COPY . /root/.config/ranger
WORKDIR /root/.config/ranger
RUN ./bin/ranger-init
