#!/bin/sh

docker stop postgresql_container
docker rm postgresql_container
docker volume create dados
docker run -it --name postgresql_container -v dados:/var/lib/postgresql/12/main/ -d rafaelct1982/postgresql-12 bash
docker exec -i postgresql_container service postgresql start


