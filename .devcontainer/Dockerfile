FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    curl \
    libbz2-dev

WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.3.5/Python-3.3.5.tgz \
    && tar xzf Python-3.3.5.tgz \
    && cd Python-3.3.5 \
    && ./configure --enable-optimizations \
    && make altinstall \
    && rm /tmp/Python-3.3.5.tgz

RUN apt-get install -y python3-pip \
    && pip3 install uncompyle6

RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.3 1

RUN apt-get install -y git vim

WORKDIR /workspace
COPY . /workspace

CMD ["bash"]
