#### An Ambari Stack for NTPD
Ambari stack for easily installing and managing NTPD on HDP cluster

- Download HDP 2.2 sandbox VM image (Sandbox_HDP_2.2_VMware.ova) from [Hortonworks website](http://hortonworks.com/products/hortonworks-sandbox/)
- Import Sandbox_HDP_2.2_VMware.ova into VMWare and set the VM memory size to 8GB
- Now start the VM
- After it boots up, find the IP address of the VM and add an entry into your machines hosts file e.g.
```
192.168.191.241 sandbox.hortonworks.com sandbox    
```
- Connect to the VM via SSH (password hadoop) and start Ambari server
```
ssh root@sandbox.hortonworks.com
/root/start_ambari.sh
```

- To deploy the NTPD stack, run below
```
cd /var/lib/ambari-server/resources/stacks/HDP/2.2/services
git clone https://github.com/abajwa-hw/ntpd-stack.git   
sudo service ambari restart
```
- Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard:

On bottom left -> Actions -> Add service -> check NTPD service -> Next -> Next -> Next -> Deploy
![Image](../master/screenshots/1.png?raw=true)
![Image](../master/screenshots/2.png?raw=true)
![Image](../master/screenshots/3.png?raw=true)
![Image](../master/screenshots/4.png?raw=true)
![Image](../master/screenshots/5.png?raw=true)
![Image](../master/screenshots/6.png?raw=true)
![Image](../master/screenshots/7.png?raw=true)
![Image](../master/screenshots/8.png?raw=true)

- On successful deployment you will see the NTPD service as part of Ambari stack and will be able to start/stop the service from here:
![Image](../master/screenshots/9.png?raw=true)

- You can see the parameters you configured under 'Configs' tab
![Image](../master/screenshots/10.png?raw=true)


#### Use ntpd service

- Check the contents of the ntpd log file we specified
```
# cat /var/log/ntpd.log
Starting ntpd: [  OK  ]
```

- Use ntpd service 
```
# service ntpd status
ntpd (pid  9180) is running...
``` 

- One benefit to wrapping the component in Ambari service is that you can now monitor/manage this service remotely via REST API
```
export SERVICE=NTPD
export PASSWORD=admin
export AMBARI_HOST=sandbox.hortonworks.com
export CLUSTER=Sandbox

#get service status
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X GET http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#start service
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Start $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "STARTED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#stop service
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Stop $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE
```

#### Remove ntpd service

- To remove the NTPD service: 
  - Stop the service via Ambari
  - Delete the service
  
    ```
    curl -u admin:admin -i -H 'X-Requested-By: ambari' -X DELETE http://sandbox.hortonworks.com:8080/api/v1/clusters/Sandbox/services/NTPD
    ```
  - Remove artifacts 
  
    ```
    rm -rf /var/lib/ambari-server/resources/stacks/HDP/2.2/services/ntpd-stack
    ```
  - Restart Ambari
    ```
    service ambari restart
    ```