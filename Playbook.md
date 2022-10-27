## Presentation Playbook

### Run Single Node Minikube:
* `minikube start`

#### Show That it is running:
* `kubectl get nodes -o wide`

#### Show the Kubernetes Dashboard:
* `minikube dashboard`

#### Show how to deploy something to the cluster:
* Via CLI
    * todo
* Via Kubectl Yaml
    * todo
* Via Helm Chart
  * https://artifacthub.io/packages/helm/prometheus-community/prometheus
    * `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
    * `helm repo update`
    * `helm install prometheus prometheus-community/prometheus -n prometheus-namespace --create-namespace`
  * Forward Port to access application
    * `kubectl --namespace prometheus-namespace port-forward TODO-ADD-PROMETHEUS-SERVER-POD-NAME 9090`

#### Show the Kubernetes REST API:

* Run a kubectl proxy
    * allows to circumvent authentication troubles
    * `kubectl proxy --port=8080 &`
* Show the API methods
  * http://localhost:8080/api/v1/
* List namespaces
  * http://localhost:8080/api/v1/namespaces
* List some pods
  * http://localhost:8080/api/v1/pods
* show some logs
  * http://localhost:8080/api/v1/namespaces/kube-system/pods/kube-controller-manager-minikube/log

### Run minikube with multiple nodes:
* `minikube start --nodes 2 -p multinode-demo`
* `minikube dashboard -p multinode-demo`

#### Drain a node and shut it down TODO
* Does not work that well on Minikube