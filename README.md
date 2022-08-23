
# CAPEv2-API

This API will an analyze uploaded file with CAPEv2 and return analysis result as JSON files

## Setup CAPEv2
You can start by downloading this repo with git command below
```
  git clone https://github.com/kevoreilly/CAPEv2.git
```


[CAPEv2 docs](https://capev2.readthedocs.io/en/latest/introduction/index.html)

[My suggestions about Cape](https://medium.com/@faruk008887/cape-malware-analysis-system-c470abaa2f60)

## Run cape



```bash
sudo python3 utils/rooter.py -g cape
```
```bash
sudo -u cape python3 cuckoo.py 
```

```bash
sudo -u cape  python3 utils/process.py -p7 auto
```
```bash
sudo -u cape python3 manage.py runserver 0.0.0.0:8000
```

## Get API

```bash
git clone https://github.com/omer832/capev2-api.git
```
## Create Token

Ensure you are in CAPE's web directory
```bash
cd /opt/CAPEv2/web
```
To create super user aka admin
```bash
python3 manage.py createsuperuser
```
To create normal user, use web interface /admin/ (in case if you not changed path)

By hand, only required if auth enabled and user MUST exist
```bash
python3 manage.py drf_create_token <your_user>
```


## Run API

```bash

python3 main.py

for docker:

docker build . -t cape-api:latest

docker run -p 8001:8001  cape-api:latest

```
### You can send your file request using command below
- This request gives you a task id

```bash
curl -F file=@/path/to/file http://0.0.0.0:8001/file-upload
```
### You can get your analysis report with your task id using command below

```bash
curl -L "http://0.0.0.0:8001/ready?task_id=<your_task_id>"
```

  
