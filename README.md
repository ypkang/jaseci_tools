## Running modules locally on clarity3
### Example - Bi Encoder

Standing up pod
```
kubectl apply -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/bi_enc.yaml
```

Deleting pod
```
kubectl delete -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/bi_enc.yaml
```

Loading the modules as a Jaseci remote module
```
actions load remote http://bi-enc-local
```