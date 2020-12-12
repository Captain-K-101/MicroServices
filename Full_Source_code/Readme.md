# Python Flask Nginx Reverse Proxy Setup
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

### Add your own project to the path
Add your Project to a folder with its dockerfile
```
> Edit the nging.conf file add your needed path to it  ie 
            location /<ANY_NAME> {
            proxy_pass http://app1:<PORT_YOUR_APP_RUNS_ON>/;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
> Save and add the app to the docker-copose file


```
