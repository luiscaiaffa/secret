FROM python:3.6

ENV DB_NAME =
ENV DB_USER =
ENV DB_PASSWORD =
ENV DB_HOST =
ENV DB_PORT =

ADD . /authentication
WORKDIR /authentication

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
