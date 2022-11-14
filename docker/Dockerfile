FROM python:3
#WORKDIR /app
COPY ./docker/requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY ./svm_gamma=0.001_C=0.5.joblib /app/
COPY ./api/* /app/

WORKDIR /app

EXPOSE 5000
#ENTRYPOINT [ "python" ]
#CMD [  "python", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD python app.py
