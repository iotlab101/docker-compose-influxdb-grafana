import requests
import numpy as np
import time

token="5zRK7tjI73ZCCCN4X4FuCHdshxvng5ag44uagzz5D-Jhmi3n0oqH2I4GC4RdOs20flsZ1WcwsyoquqKeKp_pVw=="
bucket="bucket01"
location="room01"
headers={
    "Authorization" : f"Token {token}"
}


URL = f"http://127.0.0.1:8086/write?db={bucket}"
while True:
    d = f"ambient,location={location} temperature={np.random.randint(200, 350)/10}"
    r = requests.post(url=URL, data=d, headers=headers)
    print(r.status_code)
    print(r.text)
    time.sleep(1)

