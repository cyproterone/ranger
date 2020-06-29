FROM ubuntu:latest


RUN apt update && \
    apt install -y \
    git \
    python3 python3-pip && \
    pip3 install ranger-fm


COPY . /root/.config/ranger
WORKDIR /root/.config/ranger
RUN ./bin/ranger-init
