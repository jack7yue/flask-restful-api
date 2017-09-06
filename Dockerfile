FROM python:3.5.2
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt