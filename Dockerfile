FROM ubuntu:20.04


ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
RUN apt-get update -y
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
RUN apt-get install sudo ufw libpq-dev python3.8-dev -y
COPY ./requirements.txt  /code/requirements.txt
RUN pip install -r requirements.txt
RUN sudo ufw allow 8000
COPY . /code/
WORKDIR /code
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]


#EXPOSE 8000