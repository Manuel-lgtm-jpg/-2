FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 5000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
