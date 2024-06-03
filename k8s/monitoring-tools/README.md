## Monitoring tools installation

1. Make install-observability-suite.sh executable and run deployment:
    ```bash
    chmod +x install-observability-suite.sh
    ./install-observability-suite.sh
    ```

2. Connect with grafana via:
    ```bash
    kubectl port-forward svc/grafana --namespace default 3000:3000
    ```

and go to:
*http://localhost:3000/d/hydroponic*