FROM ubuntu:latest
LABEL authors="malwenna"

ENTRYPOINT ["top", "-b"]