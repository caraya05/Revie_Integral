FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1
LABEL Loducode = "pruebas.jcsq@gmail.com"
RUN mkdir /src
WORKDIR /src
RUN pip install --upgrade pip
RUN apt-get update --fix-missing
RUN apt-get install -y build-essential libpq-dev git cmake locales gettext netcat gdal-bin
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# es_CO.UTF-8 UTF-8/es_CO.UTF-8 UTF-8/' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /src