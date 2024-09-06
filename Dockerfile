FROM python:3.9-slim

WORKDIR /app

COPY app.py cloud-sql-proxy ./

RUN pip install psycopg2-binary

ENV DB_NAME="postgres"
ENV DB_USER="postgres"
ENV DB_PASSWORD="5`5d7V.t.#:hu/fn"

CMD cloud_sql_proxy --private-ip resounding-rune-428908-p8:us-east1:sql-instance & \
    python3 app.py

