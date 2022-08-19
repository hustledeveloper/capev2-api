# CAPEv2-API  

This API will an analyze uploaded file with CAPEv2 and return analysis result as JSON files

### To-Do

- [x] File upload to API
  - [x] Extract malware path and name variables from request 
- [x] Return JSON response to request
- [x] Define static CAPEv2 API key




### How to setup

You can start by downloading this repo with git command below
```
git clone https://github.com/kevoreilly/CAPEv2
```

### You can send your file request using command below
```
#curl -F file=@/path/to/file -F machine="cuckoo1" -H "Authorization: Token YOU_TOKEN" 
```

- [x] 3-Programı çalıştırmak için komutların hepsini ayrı ayrı pencerede çalıştırın:

```
cd /opt/CAPEv2 && sudo python3 utils/rooter.py -g cape

cd /opt/CAPEv2 && sudo -u cape python3 cuckoo.py 

cd /opt/CAPEv2 && sudo -u cape  python3 utils/process.py -p7 auto

cd /opt/CAPEv2/web/ && sudo -u cape python3 manage.py runserver 0.0.0.0:8000

python3 main.py 

curl -F file=@/path/to/file http://127.0.0.1:5000/file-upload

curl -L "http://0.0.0.0:8000/apiv2/tasks/get/report/<your_task_id>/json"
⠀⠀⠀⠀⠀

...














