# app_example_flask
Deployment steps (for windows operation system)
* install docker toolbox to windows machine and test making sure it can run docker helloworld. Do NOT use docker desktop as it will conflict with virtualbox.
* open "docker quickstart terminal"
* clone the package to local:**git clone https://github.com/decisiontree/app_example_flask.git**
* build docker container: **docker build -t flask-tutorial:latest .**
* run docker container: **docker run -d -p 5000:5000 flask-tutorial**
* confirm container is running (**docker ps**) and get docker machine ip (**docker-machine ip**) 
* open the brower to access flask server: **192.168.99.101:5000**
