FROM python:3.6

ENV DB_NAME postgres
ENV DB_USER postgres
ENV DB_HOST secret_db2_1
ENV DB_PORT 5432
ENV CONFIG dev
ENV DEBUG True

ADD . /authentication
WORKDIR /authentication

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
