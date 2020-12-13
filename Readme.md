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
### How to Run as A Kuberneties Microservice

git clone the repo of choice into the server
install the tool `kompose`(used to change docker-compose.yaml files to kuberneties yaml files)
run the command kompose convert -f docekr-compose.yml -o <ANYFILENAME>.yaml
a <ANYFILENAME>.yaml should be created 
use a text editor and add the following line above the `-port:` option of the microservice you want to expose : `type: LoadBalancer`
ie: if i want to expose my nginx service
```            
    name: nginx
  spec:
    ports:
    - name: "8000"
      port: 8000
      targetPort: 80
```
changed to 
```
    name: nginx
  spec:
    type: LoadBalancer
    ports:
    - name: "8000"
      port: 8000
      targetPort: 80
```
save the changes
run kubectl apply -f <file_name>.yaml
if everything is successful the pods will get created
check using command `kubectl get po` and find the exposed ip via `kubectl get svc`            
