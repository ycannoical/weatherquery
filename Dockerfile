FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN apt-get update -y && apt-get install -y python-pip
RUN pip3 install requests
CMD ["python3","weatherquery.py"]
