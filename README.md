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



**Youtube video explaining how to use this docker-compose.yml**
[![Youtube video explaining how to use this docker-compose.yml](https://user-images.githubusercontent.com/13171662/141387616-bb4895bd-71ad-4647-8851-498f49292fc9.png)](https://youtu.be/Gl6LU1BEr1I "Youtube video explaining how to use this docker-compose.yml")

# Additional Lab

1. Enable the Authetication for the InfluxDB
```sh
mkdir data/influxdb/etc
mv data/influxdb.conf data/influxdb/etc
docker-compose restart
docker exec -it influxdb influx
> CREATE USER admin WITH PASSWORD 'yourPassword' WITH ALL PRIVILEGES
> auth
> username: admin
> password:
> create database mydb
> CREATE USER iot WITH PASSWORD ‘iot'
> grant all on mydb to iot
> exit
```

2. Simulate CPU usages from multiple Host
if you pass the argument 'dummy', then it will insert an addition tweaked data for the lab purpose.
run the sys.monitor with the sub command 'dummy' as follows
```
./sys.monitor dummy
```

3. On the Grafana, you can create a dashboard with the same type of data from multiple sources.
select a tag for the groupby

<img src="https://user-images.githubusercontent.com/13171662/201512838-5342adf6-2862-4b26-8a9c-304e7ddc6962.png" width=600/>

set the alias with [[tag_&lt;tagname&gt;]]

<img src="https://user-images.githubusercontent.com/13171662/201512852-edd349cc-6334-4f36-af39-37d66ffd5a01.png" width=600/>
