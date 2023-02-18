#!/bin/bash

docker build -t guess_number .
docker run -it --name guess_number guess_number:latest
