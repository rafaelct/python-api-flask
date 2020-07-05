#!/bin/sh

docker stop python_container
docker rm python_container
docker run --name python_container -p 5000:5000 -v "$PWD":/api --link postgresql_container -d rafaelct1982/python3-api-flask
docker ps



