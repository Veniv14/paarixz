FROM python:3.10-slim

WORKDIR /app

COPY app.py /app

RUN pip install flask
RUN pip install flask_cors
RUN pip install mysql-connector-python

EXPOSE 5000

CMD ["python3", "-u", "app.py"]
