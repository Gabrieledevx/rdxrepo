from bs4 import BeautifulSoup
import requests 
import pandas as pd 
url = 'https://es.pdfdrive.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#secciones
trending = soup.find_all('h2')
categories = soup.find_all('p')
trenx = list()
categ=list()
con =0

for i in trending: 
    if con < 5: 
        trenx.append(i.text)
    else: 
        break
    con += 1

for i in categories: 
    if con < 15: 
        categ.append(i.text)
    else: 
        break
    con += 1

def trend_today(update, context):
    
    update.message.reply_text('Mostrando los 5 más populares')
    for x in trenx:
        
        update.message.reply_text(x)

def categories_inlist(update, context):
    
    update.message.reply_text('Mostrando listado de  Categorias')
    for x in categ:
        
        update.message.reply_text(x)       

  
    