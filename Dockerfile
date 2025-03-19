FROM ubuntu:latest

USER root
EXPOSE 5000
RUN apt update -y && apt install python3 python3-pip netcat-traditional -y
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --break-system-packages

ENTRYPOINT [ "python3","app.py" ]