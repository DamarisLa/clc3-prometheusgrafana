# Prometheus-Stack Setup

Study-project: Use Prometheus &amp; Grafana to observe applications in a Kubernetes Cluster.

The following instructions describe how to set up the components used in this project.

## Setup Prometheus
https://devopscube.com/setup-prometheus-monitoring-on-kubernetes/

The following commands must be executed inside the ```clc3-prometheusgrafana```  (```./```) directory:

```kubectl create namespace monitoring```

```kubectl create -f clusterRole.yaml```

```kubectl create -f config-map.yaml```

```kubectl create  -f prometheus-deployment.yaml```

```kubectl get deployments --namespace=monitoring```

```kubectl create -f prometheus-service.yaml --namespace=monitoring```

Check if deployment was ok:

```kubectl get deployments --namespace=monitoring```

```
------------------------------------------------------------
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
prometheus-deployment   1/1     1            1           10d
------------------------------------------------------------
```

The prometheus server can now be accessed using any of the kubernetes nodes IP on port 30000


## Setup State Metrics
https://devopscube.com/setup-kube-state-metrics/

The following command must be executed inside the ```clc3-prometheusgrafana```  (```./```) directory:

```kubectl apply -f kube-state-metrics-configs/```

Check if deployment was ok:

```kubectl get deployments kube-state-metrics -n kube-system```
```
---------------------------------------------------------
NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
kube-state-metrics   1/1     1            1           10d
---------------------------------------------------------
```

## Setup Alert manager
https://devopscube.com/alert-manager-kubernetes-guide/

The following commands must be executed inside the 
```./kubernetes-alert-manager``` directory:

```kubectl create -f AlertManagerConfigmap.yaml```

```kubectl create -f AlertTemplateConfigMap.yaml```

```kubectl create -f Deployment.yaml```

```kubectl create -f Service.yaml```

Check if deployment was ok:

```kubectl get deployments --namespace=monitoring```
```
------------------------------------------------------------
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
alertmanager            1/1     1            1           10d
prometheus-deployment   1/1     1            1           10d
------------------------------------------------------------
```
The alert manager can now be accessed using any of the kubernetes nodes IP on port 31000

## Setup Grafana
https://devopscube.com/setup-grafana-kubernetes/

The following commands must be executed inside the ```./kubernetes-grafana``` directory:

```kubectl create -f grafana-datasource-config.yaml```

```kubectl create -f deployment.yaml```

```kubectl create -f service.yaml```

Check if deployment was ok:

```kubectl get deployments --namespace=monitoring```
```
------------------------------------------------------------
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
alertmanager            1/1     1            1           10d
grafana                 1/1     1            1           10d
prometheus-deployment   1/1     1            1           10d
------------------------------------------------------------
```
Grafana can now be accessed using any of the kubernetes nodes IP on port 32000

## Setup Node Exporter
https://devopscube.com/node-exporter-kubernetes/

https://www.civo.com/learn/kubernetes-node-monitoring-with-prometheus-and-grafana

The following commands must be executed inside the ```./kubernetes-node-exporter``` directory:

```kubectl create -f daemonset.yaml```

```kubectl create -f service.yaml```

Check if everything is working:

```kubectl get daemonset -n monitoring```
```
----------------------------------------------------------------------------------
NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
node-exporter   1         1         1       1            1           <none>          10d
-----------------------------------------------------------------------------------
```

```kubectl get endpoints -n monitoring``` 

```
-----------------------------------------
NAME                 ENDPOINTS        AGE
alertmanager         10.1.0.60:9093   10d
grafana              10.1.0.55:3000   10d
node-exporter        10.1.0.62:9100   10d
prometheus-service   10.1.0.59:9090   10d
-----------------------------------------
```

## Setup Application1 (Sleep)

The following command must be executed inside the ```./application1``` directory:

``` kubectl create -f deployment.yaml -n monitoring```

Requests can be sent to Application1 on any of the kubernetes nodes IP on port 30033.
The API provided by application1 is described in the ```readme.md``` located inside the ```./application1``` folder.
```
-----------------------------------------------
deployment.apps/application1-deployment created
service/application1-service created
-----------------------------------------------
```

## Setup Application2 (Not available)

The following command must be executed inside the ```./application2``` directory:

``` kubectl create -f deployment.yaml -n monitoring```

Requests can be sent to Application2 on any of the kubernetes nodes IP on port 30034.
Application2 is described in the ```readme.md``` located inside the ```./application2``` folder.

```
-----------------------------------------------
deployment.apps/application2-deployment created
service/application2-service created
-----------------------------------------------
```

## Setup Redis and Redis Exporter
https://github.com/oliver006/redis_exporter

https://github.com/oliver006/redis_exporter/blob/master/contrib/k8s-redis-and-exporter-deployment.yaml

https://www.metricfire.com/blog/how-to-monitor-redis-performance/#span-stylefontweight-400Setting-up-Prometheus-to-send-data-to-Hosted-Prometheusspan

The following command must be executed inside the ```./redis``` directory:

```kubectl create -f deployment.yaml -n monitoring```


This command starts a pod containing redis and redis exporter container.

The redis-exporter is available on any of the kubernetes nodes IP on port 30042.

With the following command it is possible to connect to the redis-cli of the redis container:

```kubectl exec -i -t [Pod Name] -n monitoring --container redis -- redis-cli```
OR just in PowerShell
```kubectl exec -i -t $(kubectl get pod --namespace monitoring --selector="app=redis" --output jsonpath='{.items[0].metadata.name}') -n monitoring --container redis -- redis-cli```

Use ```kubectl get pods -n monitoring``` to get the name of your redis pod.

If you are connected to the redis-cli you can enter the following command to generate some data:

```DEBUG POPULATE 5 test 1000```

This command creates 5 key value pairs with a value size of 1000 characters. Values are filled up with null chars to reach the specified size.

Run the ```KEYS *``` command to see the created Keys. To inspect the value of a key type ```GET [name of key]```.
The following console output shows the expected result from the commands described above. For the sake of readability the output of the ```GET``` command was not documented.
````
>DEBUG POPULATE 5 test 1000
OK
> KEYS *
1) "test:2"
2) "test:0"
3) "test:4"
4) "test:3"
5) "test:1"
> STRLEN test:2
(integer) 1000
> GET test:2
````

If you inspect the metrics endpoint of the redis-exporter you should now notice an entry in the section _number of keys by DB_.

````
# HELP redis_db_keys Total number of keys by DB
# TYPE redis_db_keys gauge
redis_db_keys{db="db0"} 5
redis_db_keys{db="db1"} 0
redis_db_keys{db="db10"} 0
redis_db_keys{db="db11"} 0
````

Database 0 should now contain five keys.

To visualize Redis Metrics in Grafana one can use the import number ID: 763 (import Dashboard)
https://grafana.com/grafana/dashboards/763-redis-dashboard-for-prometheus-redis-exporter-1-x/

