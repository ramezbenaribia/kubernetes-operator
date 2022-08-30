FROM python:3.7.3-alpine3.9

ADD . /app

RUN pip3 install /app

WORKDIR /app

# ENTRYPOINT ["copyrator"]

CMD [ "python3", "run_server.py" ]
