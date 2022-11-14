# mlops22

#Add flask app Command:

export FLASK_APP=app; flask run

#To build docker image(in the same level as api/docker)
docker build -t pred_digit:v5 -f docker/Dockerfile .

#To run the above image
sudo docker run --name pred_digit3 -p 5000:5000 pred_digit:v5

#When you'll send request, you'll see the logs as below:
![Alt text](server_logs.png?raw=true "Server Logs")
