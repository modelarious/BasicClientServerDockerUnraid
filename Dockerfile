FROM python:3.9-slim

RUN pip install flask

EXPOSE 5000

WORKDIR /app
COPY app.py /app/app.py

CMD ["python", "app.py"]
