FROM python:3.6-alpine
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV LIBRARY_PATH=/lib:/usr/lib
ENV PYTHONUNBUFFERED=1
ENV DEBUG=1
RUN apk add --update build-base python-dev py-pip jpeg-dev zlib-dev postgresql-dev
COPY . .
EXPOSE 8000
RUN pip install -qr requirements.txt
RUN python setup.py develop
CMD potaje runserver 0.0.0.0:8000