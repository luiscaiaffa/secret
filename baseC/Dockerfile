FROM python:3.6

ADD . /baseB
WORKDIR /baseB

RUN pip3 install -r requirements.txt

EXPOSE 8003

CMD ["python", "-m", "sanic", "run.app", "--host=0.0.0.0", "--port=8003"]
