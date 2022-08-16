import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

api_url = 'http://0.0.0.0:8000'

def upload_file():
	multipart_data = MultipartEncoder(fields={'file': (
							'danger.zip',
							open('/home/omer/İndirilenler/danger.zip','rb'),
							'application/octet-stream')})

	header = {
		'Content-Type': multipart_data.content_type
		}
	
	response = requests.post(api_url+'/apiv2/tasks/create/file/',
			  headers=header,
			  data=multipart_data
			)
	task_id = response.json()["data"]["task_ids"][0]
	return(task_id)



def  asdasd(task_id):
	
	response = requests.post(api_url+'/filereport/'+str(task_id)+'/json/',)
	
	print(response.text)
      
task_id = upload_file()
asdasd(task_id)
    
    
    
  
#curl -F file=@/path/to/file -F machine="cuckoo1" -H "Authorization: Token YOU_TOKEN" http://0.0.0.0:8000/apiv2/tasks/create/file/

#http://0.0.0.0:8000/filereport/20/json/  
# cookie: csrftoken=DGDrHNLkvs9Mrymby1wjlFUzl1XW8oQny5Ux56lpvfjB2Mexm6QYm67N6x5TKlmg
#Error:  You are seeing this message because this site requires a CSRF cookie when submitting forms. This cookie is required for security reasons, to ensure that your browser is not being hijacked by third parties.
