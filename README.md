## Running Jaseci Server on clarity3
Standing up Jaseci Deployment
```
kubectl apply -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/jaseci.yaml
```

Deleting Jaseci Deployment
```
kubectl delete -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/jaseci.yaml
```

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


### Example - PDF Extractor

Standing up pod
```
kubectl apply -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/pdf_extractor.yaml
```

Deleting pod
```
kubectl delete -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/pdf_extractor.yaml
```

Loading the modules as a Jaseci remote module
```
actions load remote http://pdf-extractor-local
```

### Example - Summarization

Standing up pod
```
kubectl apply -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/summarization.yaml
```
Deleting pod
```
kubectl delete -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/summarization.yaml
```

Loading the modules as a Jaseci remote module
```
actions load remote http://summarization-local
```

### Example - Text Segmenter

Standing up pod
```
kubectl apply -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/text_segmenter.yaml
```
Deleting pod
```
kubectl delete -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/text_segmenter.yaml
```

Loading the modules as a Jaseci remote module
```
actions load remote http://js-segmenter-local
```
### Example - Entity Extraction Type 2
Standing up pod
```
kubectl apply -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/tfm-ner.yaml
```
Deleting pod
```
kubectl delete -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/tfm-ner.yaml
```

Loading the modules as a Jaseci remote module
```
actions load remote http://tfm-ner-local
```
### Example - USE QA
Standing up pod
```
kubectl apply -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/use_qa.yaml
```
Deleting pod
```
kubectl delete -f https://raw.githubusercontent.com/daynauth/jaseci_tools/master/manifests/local_modules/use_qa.yaml
```

Loading the modules as a Jaseci remote module
```
actions load remote http://js-use-qa-local
```