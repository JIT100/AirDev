FROM ubuntu:20.04

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /code
WORKDIR /code
RUN apt-get update -y
#RUN apt-get install software-properties-common -y
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN add-apt-repository universe 
#RUN apt-get install sudo ufw build-essential libpq-dev libmysqlclient-dev python3.8-dev libpython3.8-dev -y
RUN apt-get install sudo ufw libpq-dev python3.8-dev -y
#ADD . /code
COPY ./requirements.txt  /code/requirements.txt
RUN pip install -r requirements.txt
RUN sudo ufw allow 8000
COPY . /code/
WORKDIR /code
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]


#EXPOSE 8000