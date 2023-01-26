# clc3-prometheusgrafana
studyproject: Prometheus &amp; Grafana to observe an application

# Prometheus-Stack Setup

This readme summarizes the following tuturial: https://devopscube.com/setup-prometheus-monitoring-on-kubernetes/

## Setup Promethus

The following commands must be executed inside the ```kubernetes``` directory:

```kubectl create namespace monitoring```

```kubectl create -f clusterRole.yaml```

```kubectl create -f config-map.yaml```

```kubectl create  -f prometheus-deployment.yaml```

```kubectl get deployments --namespace=monitoring```

```kubectl create -f prometheus-service.yaml --namespace=monitoring```

Check if deployment was ok:

```kubectl get deployments --namespace=monitoring```

The prometheus server can now be accessed using any of the kubernetes nodes IP on port 30000


## Setup State Metrics
https://devopscube.com/setup-kube-state-metrics/

The following command must be executed inside the ```kubernetes``` directory:

```kubectl apply -f kube-state-metrics-configs/```

Check if deployment was ok:

```kubectl get deployments kube-state-metrics -n kube-system```


## Setup Alert manager
https://devopscube.com/alert-manager-kubernetes-guide/

The following commands must be executed inside the ```kubernetes/kubernetes-alert-manager``` directory:

```kubectl create -f AlertManagerConfigmap.yaml```

```kubectl create -f AlertTemplateConfigMap.yaml```

```kubectl create -f Deployment.yaml```

```kubectl create -f Service.yaml```

Check if deployment was ok:

```kubectl get deployments --namespace=monitoring```

The alert manager can now be accessed using any of the kubernetes nodes IP on port 31000

## Setup Grafana
https://devopscube.com/setup-grafana-kubernetes/

The following commands must be executed inside the ```kubernetes/kubernetes-grafana``` directory:

```kubectl create -f grafana-datasource-config.yaml```

```kubectl create -f deployment.yaml```

```kubectl create -f service.yaml```

Check if deployment was ok:

```kubectl get deployments --namespace=monitoring```

Grafana can now be accessed using any of the kubernetes nodes IP on port 32000

## Setup Node Exporter
https://devopscube.com/node-exporter-kubernetes/

https://www.civo.com/learn/kubernetes-node-monitoring-with-prometheus-and-grafana

The following commands must be executed inside the ```kubernetes/kubernetes-node-exporter``` directory:

```kubectl create -f daemonset.yaml```

```kubectl create -f service.yaml```

Check if everthing is working:

```kubectl get daemonset -n monitoring```

```kubectl get endpoints -n monitoring``` 

## Setup Application1 (Sleep)

The following command must be executed inside the ```kubernetes/application1``` directory:

``` kubectl create -f deployment.yaml -n monitoring```

Requests can be sent to Application1 on any of the kubernetes nodes IP on port 30033.
The API provided by application1 is described in the ```readme.md``` located inside the ```application1``` folder.

## Setup Application2 (Not available)

The following command must be executed inside the ```kubernetes/application2``` directory:

``` kubectl create -f deployment.yaml -n monitoring```

Requests can be sent to Application1 on any of the kubernetes nodes IP on port 30034.
Application2 is described in the ```readme.md``` located inside the ```application2``` folder.

