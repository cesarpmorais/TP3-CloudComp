kubectl delete configmap pyfile
kubectl delete configmap outputkey

kubectl create configmap pyfile --from-file pyfile=mymodule.py --output yaml > pyfile.yaml
kubectl create configmap outputkey --from-literal REDIS_OUTPUT_KEY=cesarmorais-proj3-output --output yaml > outputkey.yaml

kubectl apply -f deployment.yaml

kubectl rollout status deployment/serverless-redis

kubectl delete pods -l app=serverless-redis

kubectl rollout status deployment/serverless-redis