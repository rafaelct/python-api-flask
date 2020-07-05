FROM ubuntu
LABEL version="1.0.0" description="Disponibilizando Python3 com Flask e psycopg2 (conector Postgresql)" maintainer="rafa@rafael.cteixeira.nom.br>"

RUN apt-get update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask
RUN pip3 install psycopg2-binary
EXPOSE 5000
WORKDIR /api
CMD python3 web.py





