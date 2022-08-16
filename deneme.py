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
	token = {'csrftoken':'32waZaYf3EW8HNx9Nk2zoeTcYr0iqc2qlQChAGRp2nXd3FKu2dI72W0kbPcCwivs'}
	res1 = requests.get(api_url+'/analysis/'+str(task_id)+'/')
	response = requests.post(api_url+'/filereport/'+str(task_id)+'/json/', cookies=res1.cookies )
	
	print(response.text)
      
task_id = upload_file()
asdasd(task_id)
    
    
    
  
#curl -F file=@/path/to/file -F machine="cuckoo1" -H "Authorization: Token YOU_TOKEN" http://0.0.0.0:8000/apiv2/tasks/create/file/

#http://0.0.0.0:8000/filereport/20/json/  


# cookie: csrftoken=DGDrHNLkvs9Mrymby1wjlFUzl1XW8oQny5Ux56lpvfjB2Mexm6QYm67N6x5TKlmg
#Error:  You are seeing this message because this site requires a CSRF cookie when submitting forms. This cookie is required for security reasons, to ensure that your browser is not being hijacked by third parties.
"""
Help
Reason given for failure:

    CSRF token missing.
    
In general, this can occur when there is a genuine Cross Site Request Forgery, or when Djangoâs CSRF mechanism has not been used correctly. For POST forms, you need to ensure:

Your browser is accepting cookies.
The view function passes a request to the templateâs render method.
In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.
If you are not using CsrfViewMiddleware, then you must use csrf_protect on any views that use the csrf_token template tag, as well as those that accept the POST data.
The form has a valid CSRF token. After logging in in another browser tab or hitting the back button after a login, you may need to reload the page with the form, because the token is rotated after a login.
Youâre seeing the help section of this page because you have DEBUG = True in your Django settings file. Change that to False, and only the initial error message will be displayed.

You can customize this page using the CSRF_FAILURE_VIEW setting.

"""
