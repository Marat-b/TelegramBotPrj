FROM python:3.8-slim
# FROM buran17/telegrambot-demo
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app/
# RUN python app.py