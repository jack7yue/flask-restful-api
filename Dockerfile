FROM python:3.5.2

# set the working directory
WORKDIR /app

ADD . /app

# install requirements
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
