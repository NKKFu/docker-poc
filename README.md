# Docker POC

This POC is about creating a simple web application using Docker. There is two services in this application and one reverse proxy to manage the requests.

## 100% uptime

If there is any update, docker will identify the changes and update only the container where the change has been made, this way the other services will not be affected and a 100% uptime will be achieved there.

## Update only when it's necessary

If there is no updates in the code, the container will not be updated.

## Independent services

If any service is down or breaks during the build, other services will not be affected.

## How to test

You can simply run `restart_server.bat` in a Windows environment with Docker + Docker Composer installed. This script will build the images and run the containers.

After this command run successfully, you can access the application in your browser using the URL `http://localhost/app1` or `http://localhost/app2`.

If you want to verify uptime during updates, run both `tester_app1.py` and `tester_app2.py` which will output how many requests were successful and how many failed (based on their status code return) and run `restart_server.bat` again.

Of course that if you want to see services being restarted, you can change the code in `app1` or `app2` and run `restart_server.bat` again.

## Main points of changes

- Don't down/remove services when updating new containers
- Run multiple `docker-compose up --build -d <service_name>` in restart_server.bat
