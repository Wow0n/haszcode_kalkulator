FROM python:3.9.0-buster

WORKDIR /usr/src/app

COPY requirements.txt main.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]