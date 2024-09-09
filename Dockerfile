FROM caky/flask-sqlalchemy

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
