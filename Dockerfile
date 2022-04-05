FROM python:3.9

WORKDIR /opt/OtelApiGateway

COPY ./OtelApiGateway/requirements.txt /opt/OtelApiGateway/requirements.txt

COPY ./OtelApiGateway/server.py /opt/OtelApiGateway/server.py

COPY ./OtelApiGateway/config.json /opt/OtelApiGateway/config.json

RUN pip3 install -r /opt/OtelApiGateway/requirements.txt

RUN opentelemetry-bootstrap --action=install

COPY ./OtelApiGateway/app /opt/OtelApiGateway/app

EXPOSE 8005

CMD ["opentelemetry-instrument", "python3", "server.py"]