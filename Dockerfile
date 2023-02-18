FROM ubuntu:22.04

WORKDIR /guess_number
RUN apt update && apt install -y python3
RUN groupadd Recursion && useradd recursionist -G Recursion

COPY guess_number.py/ /guess_number/
USER recursionist
