#### Dev environment:
1. Add the following domains to /etc/hosts that points to localhost.
```
dineshsonachalam@macbook ~ % cat /etc/hosts
127.0.0.1	localhost
127.0.0.1 mysql
127.0.0.1 api-adp.dineshsonachalam.com
127.0.0.1 api-search.dineshsonachalam.com
```
2. Generate self signed ssl certificate for localhost and paste in certs-dev folder.
```
openssl req -x509 -sha256 -nodes -newkey rsa:2048 -days 365 -keyout private.key -out certificate.crt
```

3. Start nginx server:
```
# To start the nginx reverse proxy
nginx -c /Users/dineshsonachalam/Desktop/ADP-Hackathon/nginx.conf 

dineshsonachalam@macbook ~ % ps -ef | grep nginx
  501  3710     1   0  9:07PM ??         0:00.01 nginx: master process nginx -c /Users/dineshsonachalam/Desktop/ADP-Hackathon/nginx.conf
  501  3711  3710   0  9:07PM ??         0:00.00 nginx: worker process
  501  3712  3710   0  9:07PM ??         0:00.02 nginx: worker process
  501  3713  3710   0  9:07PM ??         0:00.02 nginx: worker process
  501  3714  3710   0  9:07PM ??         0:00.03 nginx: worker process
  501  4142  4110   0  9:26PM ttys002    0:00.01 grep nginx

# To stop the nginx:
nginx -s stop
```

4. Start the docker-compose
```
docker-compose up
```

5. Open the https://api-adp.dineshsonachalam.com URL in firefox and allow use of self signed certificate.


### Helm install:
```
helm install adp-app ./helm
```

KUBE_CONFIG_DATA:
```
dineshsonachalam@macbook ~ % cat ~/.kube/config | base64
```

```
Error: uninstall: Release name is invalid: ./helm
dineshsonachalam@macbook ADP-NY-HACKATHON % helm install adp-app ./helm  
NAME: adp-app
LAST DEPLOYED: Sat May  8 20:04:45 2021
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
dineshsonachalam@macbook ADP-NY-HACKATHON % git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
dineshsonachalam@macbook ADP-NY-HACKATHON % helm list
NAME                    NAMESPACE       REVISION        UPDATED                                 STATUS  CHART                            APP VERSION
adp-app                 kube-system     1               2021-05-08 20:04:45.172474 +0530 IST    deployedadp-ny-hackathon-app-0.1.0       1.0        
tech-search-engine      kube-system     1               2021-05-08 09:04:54.806979 +0530 IST    deployedtech-courses-search-engine-0.1.0 1.0        
dineshsonachalam@macbook ADP-NY-HACKATHON % kubectl get deployments -n=dinesh
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
adp-backend       1/1     1            1           29s
adp-frontend      1/1     1            1           29s
search-backend    1/1     1            1           11h
search-frontend   1/1     1            1           11h
```


