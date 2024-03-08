Sample docker-compose configuration for influxdb & grafana
### this needs the docker installed
- `curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh`
- `sudo usermod -aG docker ubuntu` or `sudo usermod -aG docker pi`
- `exit` and relogin
- verify by running `docker ps`

**Note**
In the docker-commpose.yml, you see the volume sections for the data persisitency if you want it to persist. And for grafana container volume, you need to change the ownership to 472:472

<pre>
sudo chown -R 472:472 data/grafana
</pre>


# Lab

1. git clone git@github.com:iotlab101/docker-compose-influxdb-grafana.git
2. cd docker-compose-influxdb-grafana
3. sudo chown -R 472:472 data/grafana
4. docker-compose up -d
5. open a web browser for http://(your server or your pi).local:8086, and create token & bucket
6. modify sys.monitor with the token and the org id created on the previous step
7. take the flux query from influxdb web(http://(your server or your pi).local:8086)
8. and use it to create the grafana chart on http://(your server or your pi).local:3000 
