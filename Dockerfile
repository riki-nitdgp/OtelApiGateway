FROM python:3.9

WORKDIR /opt/api_gateway

COPY ./api_gateway/requirements.txt /opt/api_gateway/requirements.txt

COPY ./api_gateway/server.py /opt/api_gateway/server.py

COPY ./api_gateway/config.json /opt/api_gateway/config.json

RUN pip3 install -r /opt/api_gateway/requirements.txt

RUN opentelemetry-bootstrap --action=install

COPY ./api_gateway/app /opt/user_service/app

EXPOSE 8005

CMD ["opentelemetry-instrument", "python3", "server.py"]