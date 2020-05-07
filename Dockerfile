FROM python:3.6

RUN pip install pyftpdlib

WORKDIR /app

ADD client.py /app
ADD server.py /app

ENV SOURCE_ADDRESS_PORT='2123'

ENTRYPOINT ["python"]
CMD ["client.py"]
