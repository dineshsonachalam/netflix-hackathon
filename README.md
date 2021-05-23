# ADP NY Hackathon
<p>
  <a href="https://github.com/dineshsonachalam/ADP-NY-HACKATHON/actions" alt="CI/CD status">
      <img src="https://github.com/dineshsonachalam/ADP-NY-HACKATHON/actions/workflows/k8-deploy.yml/badge.svg" />
  </a>
  <a href="https://www.python.org/downloads/release/python-390/" alt="Python 3.9">
      <img src="https://img.shields.io/badge/python-3.9-blue.svg" />
  </a>
  <a href="https://hub.docker.com/repository/docker/dineshsonachalam/adp-ny-hackathon-backend" alt="Docker pulls">
      <img src="https://img.shields.io/docker/pulls/dineshsonachalam/adp-ny-hackathon-backend.svg" />
  </a>
</p>

#### To do: 
1. Create a file loading component and load if redux state is not updated.
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
```
dineshsonachalam@macbook ADP-NY-HACKATHON % kubectl get pods -n=dinesh
NAME                               READY   STATUS    RESTARTS   AGE
adp-backend-554b87fc9f-7kmc5       1/1     Running   0          33m
adp-frontend-6b984d7554-pqkms      1/1     Running   0          33m
elasticsearch-0                    1/1     Running   0          11h
mysql-0                            1/1     Running   0          33m
search-backend-dddf55555-hb6vt     1/1     Running   0          89m
search-frontend-78fdb94f44-sbhh6   1/1     Running   0          89m
dineshsonachalam@macbook ADP-NY-HACKATHON %
```



dineshsonachalam@macbook ADP-NY-HACKATHON % kubectl cp ./mysql-dump/adp.sql dinesh/mysql-0:docker-entrypoint-initdb.d
dineshsonachalam@macbook ADP-NY-HACKATHON %



dineshsonachalam@macbook ADP-NY-HACKATHON % kubectl exec mysql-0 /bin/bash -n=dinesh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
dineshsonachalam@macbook ADP-NY-HACKATHON % kubectl exec -it mysql-0 /bin/bash -n=dinesh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
root@mysql-0:/#
root@mysql-0:/# mysql
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
root@mysql-0:/# mysql -u dinesh -p simple
Enter password:
ERROR 1045 (28000): Access denied for user 'dinesh'@'localhost' (using password: YES)
root@mysql-0:/# mysql
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
root@mysql-0:/# mysmysql -u root -p^C
root@mysql-0:/# mysql -u root -p simple
Enter password:
ERROR 1049 (42000): Unknown database 'simple'
root@mysql-0:/# mysql -u root
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
root@mysql-0:/# clearmysql -u root -p
bash: clearmysql: command not found
root@mysql-0:/# mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7
Server version: 5.7.34 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show tables();
ERROR 1046 (3D000): No database selected
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| adp                |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

mysql> exit();
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'exit()' at line 1
mysql> exit()
    -> exit();
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'exit()
exit()' at line 1
mysql>



mysql -u root -psimple 

shows databases;






docker exec -it mysql sh -c 'mysql -u root -psimple  --execute="SHOW DATABASES;"; exit $?'


```
dineshsonachalam@macbook ADP-NY-HACKATHON % helm install adp-app ./helm
NAME: adp-app
LAST DEPLOYED: Sat May  8 22:58:13 2021
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

helm install tech-courses-search-engine ./helm

mysql -u root -psimple < /docker-entrypoint-initdb.d/adp.sql


```
kubectl exec -it postgres-0 /bin/bash -n=dinesh


psql -d dinesh-micro-apps -U dinesh -W


gdm-backend-55f5f6cf8b-szmmf

kubectl exec -it gdm-backend-55f5f6cf8b-szmmf /bin/bash -n=dinesh
```