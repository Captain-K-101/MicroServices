# python-flask-docker
Basic Python Flask app in Docker which prints the hostname and IP of the container

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/Captain-K-101/MicroServices.git
$ docker-compose build
$ docker-compose up

```

### Run the container individually(without rev-proxy)
Create a container from the image.
```
$ cd <Path/to/file>
$ docker build -t container1
$ docker run -d -p 5000:5000 container1
```

Now visit http://localhost:5000


