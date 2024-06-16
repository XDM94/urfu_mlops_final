#!/bin/sh

#создаем и запускаем контейнер
sudo docker run -d --name titanic-container -p 8091:8091 titanic-img