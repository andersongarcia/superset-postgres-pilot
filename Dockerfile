FROM apache/superset:latest

USER root
# Instala o driver do PostgreSQL
RUN pip install psycopg2-binary
USER superset