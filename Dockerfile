FROM python:3.12-slim

WORKDIR /app

COPY ./web_project/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./web_project/ .

EXPOSE 5000

CMD ["python", "app.py"]
