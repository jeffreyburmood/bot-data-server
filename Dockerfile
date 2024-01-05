FROM python:3.12
LABEL authors="jeffrey"

ENTRYPOINT ["top", "-b"]