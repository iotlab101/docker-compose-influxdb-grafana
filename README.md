Sample docker-compose configuration for influxdb & grafana


**Note**
In the docker-commpose.yml, you see the volume sections for the data persisitency if you want it to persist. And for grafana container volume, you need to create 'grafana' directory and change the ownership to 472:472

<pre>
grafana:
  ......
  volumes:
    - ./grafana:/var/lib/grafana
</pre>

<pre>
mkdir grafana
chown 472:472 grafana
</pre>


echo create database sensorDB | docker exec -i influxdb influx

sys.monitor [dummy]
if you pass the argument 'dummy', then it will insert an addition tweaked data for the lab purpose.

select cpu as the measurement, select the user, set distinct, add gropuby for tag(host), put [[tag_host]] to alias

**Youtube video explaining how to use this docker-compose.yml**
[![Youtube video explaining how to use this docker-compose.yml](https://user-images.githubusercontent.com/13171662/141387616-bb4895bd-71ad-4647-8851-498f49292fc9.png)](https://youtu.be/Gl6LU1BEr1I "Youtube video explaining how to use this docker-compose.yml")
