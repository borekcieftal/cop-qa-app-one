FROM python:3.9.5-windowsservercore-1809

WORKDIR /

RUN pip3 install flask requests

COPY . .

CMD [ "python", "my_api1.py"]