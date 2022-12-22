



![image](https://user-images.githubusercontent.com/62024017/209227689-d7aa55c9-0e19-4d7b-910c-79d3f01caf3e.png)

PROPOSAL:

The goal is to observe a Kubernetes cluster with services running in pods and get metrics about their health status. For this purpose we use Prometheus.
The services are implemented in python and built as docker images. One service holds a sleep function and one is  throwing server not available exceptions. One of the pods might hold a database. 
Prometheus is able to count the number of requests within specific timeframes. It will check whether servers are getting slow or if there is a bottleneck. 
With grafana we will visualize the traffic over time. 

1) Each of us implements a service in a container. 
2) Each container run in a pod in the kubernetes cluster
3) Prometheus is setup in the kubernetes cluster
4) Prometheus is setup to alert user via mail
5) Grafana is setup in the kubernetes cluster
6) Grafana visualization setup 
7) Live demo is prepared


Haijes: Implementation of a service, sets vizualization up, prepares live demo
Lattimer: Implementation of a service, writing of YAML file to deploy all services (including prometheus and grafana)
Schinninger: Implementation of a service, setup the alert manager 


