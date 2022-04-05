FROM python:3.9

WORKDIR /opt/api_gateway

COPY ./api_gateway/requirements.txt /opt/api_gateway/requirements.txt

COPY ./api_gateway/server.py /opt/api_gateway/server.py

COPY ./api_gateway/config.json /opt/api_gateway/config.json

RUN pip3 install -r /opt/api_gateway/requirements.txt

COPY ./api_gateway/app /opt/user_service/app

EXPOSE 8005

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]