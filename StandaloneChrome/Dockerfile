# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOTE: DO *NOT* EDIT THIS FILE.  IT IS GENERATED.
# PLEASE UPDATE Dockerfile.txt INSTEAD OF THIS FILE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
FROM selenium/node-chrome:3.4.0-dysprosium_warsaw
LABEL authors=SeleniumHQ

USER seluser

#====================================
# Scripts to run Selenium Standalone
#====================================
COPY entry_point.sh /opt/bin/entry_point.sh

RUN  sudo mkdir -p /opt/warsaw \
  && sudo chown seluser:seluser /opt/warsaw \
  && wget --no-verbose https://cloud.gastecnologia.com.br/bb/downloads/ws/warsaw_setup64.deb -O /opt/warsaw/warsaw_setup64.deb

RUN echo 1 > /tmp/standalone_ok

EXPOSE 4444
