from bs4 import BeautifulSoup
import requests

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
 "Access-Control-Allow-Credentials": "true",
 "Access-Control-Allow-Headers":"Authorization,Accept,Origin,DNT,User-Agent,Content-Type,Wb-AppType,Wb-AppVersion,Xwbuid,Site-Locale,X-Clientinfo,Storage-Type,Data-Version,Model-Version,__wbl, x-captcha-id",
 "Access-Control-Allow-Methods":"GET,OPTIONS",
 "Access-control-Allow-Origin":"https://www.wildberries.ru",
 "Content-Encoding":"gzip",
 "Content-Type":"application/json charset=utf-8"
 }

r = requests.get("https://www.wildberries.ru/catalog/192820101/detail.aspx", headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
## productTitle--J2W7I
print(r)
