FROM ubuntu:20.04

ENV PATH=$PATH:/opt/qt-installer-framework/Tools/QtInstallerFramework/4.0/bin

WORKDIR /app

RUN apt update
RUN apt install -y python3-pip libfontconfig libx11-xcb1 libxcb1 libxrender1 libxtst6 libxkbcommon-x11-0 libdbus-1-3
RUN pip3 install aqtinstall
RUN aqt tool -O /opt/qt-installer-framework linux tools_ifw 4.0 qt.tools.ifw.40
