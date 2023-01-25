# Build image

 `docker image build -f Dockerfile -t [YOUR-DOCKERHUB-ACCOUNT]/prometheus-flask-example:1.0.0 ./`

# Push image

`docker image push [YOUR-DOCKERHUB-ACCOUNT]/prometheus-flask-example:1.0.0`   

Once the image is pushed to your Dockerhub account you can refer to it in your Kubernetes Deployment. In the case you do not want to push the image to your own dockerhub account you can also use the following already existing image: `dragonbruceli
/
prometheus-flask-example`

# Test container
Run `docker run -p 8000:8000 [YOUR-DOCKERHUB-ACCOUNT]/prometheus-flask-example:1.0.0` in your console and navigate to [http://localhost:8000/metrics](http://localhost:8000/metrics).
You should now see some statistics regarding the previously started flask application. To create new statistics make some requests to the endpoints of the service.

# API Description

`/delay`

Triggers an immediate response

`/delay/<delay_ms>`

Triggers a response with user defined delay. Response times are recorded as histogram. Request times are binned into buckets with the label `request_processing_seconds_bucket`.

Try to make a request wit non-numeric values for `delay_ms`. This triggers a `ValueError` inside the application. Each  `ValueError` leads to the incrementation of the counter metric `number_of_value_errors_total`.
