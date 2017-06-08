FROM python:2
MAINTAINER Jian Li <gwind@ooclab.org>

ENV PATH /usr/local/bin:$PATH
ENV LANG en_US.UTF-8

RUN apt-get update -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y vim tree curl net-tools iputils-ping dstat htop ipython \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /build/
COPY requirements.txt /build/
RUN pip install -r /build/requirements.txt

#VOLUME /work
WORKDIR /work/

CMD ["bash"]
