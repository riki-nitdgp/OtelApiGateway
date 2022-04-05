FROM python:3.9

WORKDIR /opt/api_gateway

COPY ./requirements.txt /opt/api_gateway/requirements.txt

COPY ./server.py /opt/api_gateway/server.py

COPY ./config.json /opt/api_gateway/config.json

RUN pip3 install -r /opt/api_gateway/requirements.txt

COPY ./app /opt/user_service/app

EXPOSE 8005

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]