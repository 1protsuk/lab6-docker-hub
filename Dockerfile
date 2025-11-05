FROM python:3.9-slim
WORKDIR /app

# TODO: Вкажіть ваше прізвище
LABEL maintainer="ПРОЦУК"


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]

