FROM ooclab/eva
MAINTAINER lijian@ooclab.com

ENV PATH /usr/local/bin:$PATH
#ENV LANG en_US.UTF-8

#RUN pip3 install psycopg2 elasticsearch
COPY requirements.txt /
RUN pip3 install -r /requirements.txt && rm /requirements.txt

VOLUME /work
WORKDIR /work

CMD ["bash"]
