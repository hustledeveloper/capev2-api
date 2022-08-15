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
