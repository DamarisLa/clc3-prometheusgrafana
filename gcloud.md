# Google Cloud with Services already running

Follow steps 1, 6, 8, 9, 10, 12, 14, 15, 17, 19

# First setup with Google Cloud

## Prerequisites
1. Account in [Google Cloud](http://cloud.google.com/) and start a trial version
2. Install [Google Cloud SDK](https://cloud.google.com/sdk/install) Run the command: 
```console
gcloud version
```
3. If not done before: run the ```kubectl``` installation command
```console
gcloud components intall kubectl
```

## Setup Cluster
1. Log in from your command line with
```console
gcloud auth login
```

2. Open the [Kubernetes Engine Overview](https://console.cloud.google.com/kubernetes)

3. Click on *Create Cluster* and select "Standard: you manage your cluster"

4. Create a cluster with the *default* settings except for the *Number of nodes* where you only need 1:

    ![K8s Cluster in GKE](./img/gcloud_01.PNG)
    ![K8s Cluster in GKE](./img/gcloud_02.PNG)
    ![K8s Cluster in GKE](./img/gcloud_03.PNG)

5. As soon as your cluster is ready, click on *Connect* and copy and paste this command into your terminal

6. Now your `kubectl` (i.e., the Kubernetes command-line tool) should be configured for your cluster. In order to verify this, execute the command: 

    ```console
    kubectl get nodes
    ```

7. Change to the directory in the git folder and run the commands for <B>Setup Prometheus</B> from the ```README.md``` 

8. Check if it is running with
```console
kubectl get pods --namespace monitoring
```

9. Forward the port (change the name of the pod as given in previous step)
```console
kubectl port-forward --namespace monitoring prometheus-deployment-5978c4f57-ljm2z 8080:9090
```

10. Now open the link <localhost:8080> in your browser.

11. Continue the ```README.md``` with <B>Setup State Metrics</B> and <B>Setup Alert manager</B>
Changed in ```kubernetes-alert-manager/Deployment.yaml``` the spec/resources/requests to 100m at cpu and 100M at memory

12. Run step 8 and 9 with alertmanager and port 8081:9093 now the link <localhost:8081> should work

13. Continue the ```README.md``` with <B>Setup Grafana</B>
Also change in this Deployment cpu and memory to 100m

14. Run step 8 and 9 with grafana and port 8082:3000

15. Open the link <localhost:8082> and login with admin admin and skip new password

16. Continue the ```README.md``` with <B>Setup Node Exporter</B> and <B>Setup Application1 (Sleep)</B>

17. Run step 8 and 9 with Application1 and port 8083:8000

18. Continue the ```README.md``` with <B>Setup Application2 (Not available)</B>

19. Run step 8 and 9 with Application2 and port 8084:8001

---------------
1. For updating a Deployment.yaml run for example
```console
kubectl edit deployment alertmanager --namespace monitoring
```


1. Go to Google Cloud / VPC Network / Firewall and create a new Firewall Rule with following settings

    ![K8s Cluster in GKE](./img/gcloud_04.PNG)
    ![K8s Cluster in GKE](./img/gcloud_05.PNG)
