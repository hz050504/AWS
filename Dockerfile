FROM docker/whalesay:lastest
RUN apt-get -y update && apt-get install -y fortunes
CMD /usr/games/fortune -a | cowsay