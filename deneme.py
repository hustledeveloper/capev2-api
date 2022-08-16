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
		'Content-Type': multipart_data.content_type,
		'Authorization': '6fc5be6ee1d904476ba6c255173ad3f086a6f537'
		}
	
	response = requests.post(api_url+'/apiv2/tasks/create/file/',
			  headers=header,
			  data=multipart_data
			)
	task_id = response.json()["data"]["task_ids"][0]
	return(task_id)



def get_ceysin(task_id):

	header = {
		
		'Authorization': '6fc5be6ee1d904476ba6c255173ad3f086a6f537'
		}
	
	#token = {'csrftoken':'32waZaYf3EW8HNx9Nk2zoeTcYr0iqc2qlQChAGRp2nXd3FKu2dI72W0kbPcCwivs'}
	#res1 = requests.get(api_url+'/analysis/'+str(task_id)+'/')
	response = requests.get(api_url+'/filereport/'+str(task_id)+'/json/', headers=header)
	
	print(response.text)
      
task_id = upload_file()
get_ceysin('29')
print(task_id)
 
""" 
daha önceden analiz edilmiş bir işlemin id'si ile json dosyasını almayı başardım, şimdi tek sorun
yapılan bir analiz için, json sonucu dönmesine kadar geçecek 2 dakikada bekleyebilecek ve sonuç çıkınca sonucu alacak bir kod yazmak, şu an kod analiz yaptığı an sonucu istiyor ve çıkmamış sonucu alamayıp hata veriyor 
""" 
 
#curl -F file=@/path/to/file -F machine="cuckoo1" -H "Authorization: Token YOU_TOKEN" http://0.0.0.0:8000/apiv2/tasks/create/file/
#http://0.0.0.0:8000/filereport/20/json/  

