FROM postgres
ENV POSTGRES_PASSWORD 123
ENV POSTGRES_DB sos
COPY database/dump_sos.sql /docker-entrypoint-initdb.d/
