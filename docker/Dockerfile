#################
#
# Author:      Des Jones (dejones@alertlogic.com)
# Project:     Alertlogic automation
# Date:        Tue 12 Nov 16:22:55 GMT 2019
# Version:     1.0
# Howto:
# docker build -t al-python38-amzn2 --build-arg user=$USER .
# docker run -d --name=al-python38-amzn2 -v ~/.ssh:/home/$USER/.ssh -v ~/al-python38-amzn2:/home/$USER/al-python38-amzn2 al-python38-amzn2
# docker exec -it al-python38-amzn2 bash
# cd al-python38-amzn2 && sudo ./install.sh && ./build.sh
#
###################################################
FROM centos:7
ARG user
ENV USER $user
RUN yum install -y redhat-lsb-core sudo wget bash curl gpg2 which git source vim
RUN yum groupinstall -y 'Development Tools'
RUN yum install -y rpmdevtools rpmlint createrepo
RUN echo '%sudo   ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/sudo
RUN adduser $USER
RUN groupadd -r sudo
RUN usermod -a -G sudo $USER
ENV USER $USER
WORKDIR /home/$USER
USER $USER
CMD while true; do sleep 1000; done
