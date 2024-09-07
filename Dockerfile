FROM python:3.9-slim

WORKDIR /app

COPY app.py cloud-sql-proxy ./

RUN pip install psycopg2-binary

CMD /app/cloud-sql-proxy --private-ip resounding-rune-428908-p8:us-east1:sql-instance & \
    python3 app.py

