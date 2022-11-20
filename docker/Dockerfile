#FROM ubuntu:latest
FROM python:3
COPY ./*.py /exp/
COPY ./requirements.txt /exp/requirements.txt
COPY ./svm_gamma=0.001_C=0.5.joblib /exp/
COPY ./api/* /exp/
RUN pip3 install --no-cache-dir -r /exp/requirements.txt
WORKDIR /exp
#RUN mkdir models/
#RUN mkdir results/
EXPOSE 5000
CMD python, ./app/api.py
