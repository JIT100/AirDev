FROM python:3.8

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /code
WORKDIR /code
ADD . /code
COPY ./requirements.txt  /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/