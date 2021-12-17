FROM python:3.10-slim-buster
WORKDIR Task1
ADD converter.py .
ENTRYPOINT ["python", "./converter.py"]
