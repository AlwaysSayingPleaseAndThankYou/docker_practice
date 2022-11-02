FROM ubuntu:latest
FROM python:3.7
RUN apt-get update && apt-get install -y libc6-dev libunwind8 unzip git curl
RUN curl https://opentap.io/assets/OpenTAP.9.19.3.tar -o OpenTAP.tar
RUN tar -xf ./OpenTAP.tar
RUN chmod u+x INSTALL.sh
RUN echo y | sh ./INSTALL.sh
RUN pip3 install pip --upgrade
RUN pip3 install pyarrow perspective-python pandas numpy panel
COPY perspective_panel.py .
ENTRYPOINT ["python3", "perspective_panel.py"]