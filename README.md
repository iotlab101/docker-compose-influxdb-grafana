Sample docker-compose configuration for influxdb & grafana


**Note**
In the docker-commpose.yml, you see the volume sections for the data persisitency if you want. And for grafana container volume, you need to create 'grafana' directory and change the ownership to 472:472

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
