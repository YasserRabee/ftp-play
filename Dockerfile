FROM python:3.6

WORKDIR /app

ADD client.py /app

ENV SOURCE_ADDRESS='35.224.32.114'
ENV SOURCE_ADDRESS_PORT='2123'

ENTRYPOINT ["python", "client.py"]
