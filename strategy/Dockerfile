FROM centos:7
RUN yum install -y epel-release
RUN yum install -y python2-pip python-gunicorn
WORKDIR /opt/strategy
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./main.py .
COPY ./run.sh .
CMD /opt/strategy/run.sh
EXPOSE 8000
