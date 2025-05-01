FROM python:3.10-slim

WORKDIR /app
copy . /app
RUN apt update -y && apt install awscli -y

RUN pip install -r requirements.txt


CMD ["python", "app.py"]
