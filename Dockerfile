FROM python:3.7

COPY . /workspace
WORKDIR /workspace

EXPOSE 80

CMD ["python", "-u", "./main.py"]
