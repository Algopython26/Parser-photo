from bs4 import BeautifulSoup
import os
import requests as rq

link=input("Введите ссылку: ")
folder = input("Введите название папки куда сохранять фото: ")
os.mkdir(folder)

r = rq.get(link)
r.encoding = 'cp1251'
s = BeautifulSoup(r.text, "html.parser")

myimg = s.find_all("img")

z = []
for i in myimg: 
	if "jpg" in i['src']:
			print(i['src'])
			z.append(i['src'])

i=1
for img_link in z:
	if i <= 100:
		img_data = rq.get(img_link).content
		with open( folder +"/"+ str(i) +".jpg" , "wb+") as f:
			f.write(img_data)
		print("Скачиваю фото №",i)
		i +=1
	else:
		f.close()
		break