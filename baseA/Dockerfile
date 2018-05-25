FROM python:3.6

ADD . /baseA
WORKDIR /baseA

RUN pip3 install -r requirements.txt

EXPOSE 8001

CMD ["python", "-m", "sanic", "run.app", "--host=0.0.0.0", "--port=8001"]
