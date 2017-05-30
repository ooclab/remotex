FROM ubuntu
MAINTAINER lijian@ooclab.com

ENV PATH /usr/local/bin:$PATH
#ENV LANG en_US.UTF-8

RUN apt-get update -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y python3 curl net-tools iputils-ping python3-nose vim ipython3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pip --upgrade
RUN pip3 install wheel python-dateutil tornado sqlalchemy six wtforms elasticsearch
# https://pypi.python.org/pypi/pyeva
RUN pip3 install https://pypi.python.org/packages/0e/80/cc67bdf4c3646ae8edd25470275637774e8f032d8220912f9d61cb8bf7d4/pyeva-2.0.2.tar.gz#md5=6d6e67a49db173bc7c114c3a7a72c4b8

VOLUME /work
WORKDIR /work

CMD ["bash"]
