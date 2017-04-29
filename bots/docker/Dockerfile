FROM perl:5
MAINTAINER Jian Li <gwind@ooclab.org>

ENV PATH /usr/local/bin:$PATH
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

#RUN apt-get update -y \
#    && apt-get dist-upgrade -y \
#    && apt-get install -y vim tree curl net-tools iputils-ping dstat htop ipython \
#    && rm -rf /var/lib/apt/lists/*

RUN cpanm -nq Mojo::UserAgent Digest::MD5 Encode Time::HiRes DateTime YAML::Syck Path::Tiny JSON Time::Piece
RUN cd /tmp/ && git clone https://github.com/ooclab/remotex && cp -a /tmp/remotex/bots /usr/src/bots && rm -rf /tmp/remotex
#COPY /tmp/remotex/bots /usr/src/bots
WORKDIR /usr/src/bots
CMD [ "bash", "/usr/src/bots/start.sh" ]
