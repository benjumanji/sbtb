FROM centos:7
RUN yum install -y epel-release
RUN yum install -y python2-pip python-gunicorn
WORKDIR /opt/exchange
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./main.py .
COPY ./run.sh .
CMD /opt/exchange/run.sh
EXPOSE 8000
