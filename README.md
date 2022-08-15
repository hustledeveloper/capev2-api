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
### kurulum notları 
cape arkasında güçlü bir komünite olsa da kurulum ve kullanımında sorunlar yaşayabileceğiniz bir malware analiz programı. Bu sorunlardan bazıları ve çözmek için yapmanız gerekenler:
- [x] 1- Programın çalışma ortamının gömülü ubuntu olması ve sanal makine olarak da virt-manager'da win7 kullanmanız en mantıklı tercih olacaktır. Teorik olarak sanal makine olarak windows işletim sisteminizde, virtualbox'ta çalışan ubuntu'da çoklu sanallaştırma yaparak win7 kurup da programı çalıştırabilirsiniz (bunun için nested-virtualization destekleyen bir işlemciye sahip olduğunuzdan emin olun). Ama bu  inanılmaz bug'lar ve boşa harcanan saatlere sebep olabilir. Bu yüzden tavsiye ettiğim gömülü ubuntu-sanal win7  ortamını kullanın.
- [x] 2- 2 adet kurulum scripti bulunmakta, bunları tavsiye edilen şekillerde çalıştırıp programı kurabilirsiniz. Karşılaşacağınız ilk sorun, scriptin kurulum için çektiği bazı repo'ların artık kullanılamaz olması. Bu yüzden gerekli kütüphaneleriniz eksik kalacak ve error olarak bunu fark edeceksiniz. Önemli olan kısım ise bu eksik kütüphaneleri asla son sürümü ile kurmayın! Apt-get install kullanmayın. Programın çalışması için gerekli olan sürümü requiriments dosyasından bulun ve gerekli kütüphane versiyonunu yükleyin. Aksi halde yüklediğiniz güncel kütüphane, kendisinin beraber çalıştığı diğer kütüphaneleri de güncelleyecek ve sistem zehirlenmesi(os poisoning) yaşayacaksınız.
- [x] 3-Programı çalıştırmak için komutların hepsini ayrı ayrı pencerede çalıştırın:

```
cd /opt/CAPEv2 && sudo python3 utils/rooter.py -g cape

cd /opt/CAPEv2 && sudo -u cape python3 cuckoo.py 

cd /opt/CAPEv2 && sudo -u cape  python3 utils/process.py -p7 auto

cd /opt/CAPEv2/web/ && sudo -u cape python3 manage.py runserver 0.0.0.0:8000
```

