https://prometheus.io/docs/introduction/overview/
# Build image

 `docker image build -f Dockerfile -t [YOUR-DOCKERHUB-ACCOUNT]/prometheus-not-available-example:1.0.0 ./`

# Push image
First Login to your Dockerhub account.

`docker login`

Afterwards push the image to your Dockerhub account.

`docker image push [YOUR-DOCKERHUB-ACCOUNT]/prometheus-not-available-example:1.0.0`   

Once the image is pushed to your Dockerhub account you can refer to it in your Kubernetes Deployment. In the case you do not want to push the image to your own dockerhub account you can also use the following already existing image: `dragonbruceli/prometheus-not-available-example:1.0.0`

# Test container
Run `docker run -p 8000:8000 [YOUR-DOCKERHUB-ACCOUNT]/prometheus-not-available-example:1.0.0` in your console and navigate to [http://localhost:8000/metrics](http://localhost:8000/metrics).
You should now see a __Service Unavailable__ notification.

# Service Description
This application is used to simulate capacity problems. Therefore, for every request the HTTP status code __503__ is returned.


