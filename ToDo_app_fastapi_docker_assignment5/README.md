## ToDo API


### Description

###### This API deployed on liara with Docker:
Its root live url is: https://mytodo-app.liara.run/

#### The main purpose of to do list:
To provide yourself with a list of your priorities in order to ensure that you don`t
forget anything and are able to effectively plan out your tasks so that they are all
accomplished in the correct time frame.



### API documentation

Copy and paste live server URL in your browser. In the continuation of URL add /redoc

![documentation](https://github.com/FahimeMirveisi/Python_for_Deployment/blob/main/ToDo_app_fastapi_docker_assignment5/To_Do_App/assets/docs.png)

### How to use this API

- Copy and paste URL in your browser or postman
- Follow API documentation instructure

###  * all Docker commands I used *

|Docker commands|What is command for?|
|---|---|
|docker build -t todo .| To build todo docker image|
|docker images|To see all my images|
|docker run -d -p 80:80 todo| To create a container from todo image with random name on port 80 (local)|
|docker ps|To see all runnung containers|
|docker ps -a|To see all hidden, running and exited containers|
|docker logs <CONTAINER NAME> |To see my app functionality|
|docker stop <CONTAINER NAME> |To stop a running container|
|docker rm <CONTAINER NAME> |To remove a container|
|docker rmi <IMAGE NAME> |To remove an image when Dockerfile had changes an then rebuild a new image|
