#!/bin/bash

set -e

function retry_until_success {
  local cmd=$1
  local yaml_file=$2

  until $cmd; do
    echo "Retrying $yaml_file due to previous failure..."
    sleep 5
  done
}

helm repo add hashicorp https://helm.releases.hashicorp.com

helm repo update

helm install --values values-v1.yaml consul hashicorp/consul --version '1.2.0'

retry_until_success "kubectl apply -f proxy-defaults.yaml" "proxy-defaults.yaml"

retry_until_success "kubectl apply -f rabbitmq.yaml" "rabbitmq.yaml"

retry_until_success "kubectl apply -f auth-postgres.yaml" "auth-postgres.yaml"

retry_until_success "kubectl apply -f manager-postgres.yaml" "manager-postgres.yaml"

retry_until_success "kubectl apply -f measurements-postgres.yaml" "measurements-postgres.yaml"

retry_until_success "kubectl apply -f auth.yaml" "auth.yaml"

retry_until_success "kubectl apply -f manager.yaml" "manager.yaml"

retry_until_success "kubectl apply -f measurements.yaml" "measurements.yaml"

retry_until_success "kubectl apply -f nginx.yaml" "nginx.yaml"

retry_until_success "kubectl apply -f allow.yaml" "allow.yaml"

retry_until_success "kubectl apply -f consul-api-gateway.yaml" "consul-api-gateway.yaml"

retry_until_success "kubectl apply -f routes.yaml" "routes.yaml"

retry_until_success "kubectl apply -f referencegrant.yaml" "referencegrant.yaml"

retry_until_success "kubectl apply -f rbac.yaml" "rbac.yaml"

echo "#######################################"
echo "Deployment Complete"
echo "Grab your coffe and come back in 10 minutes :)"
echo "#######################################"
