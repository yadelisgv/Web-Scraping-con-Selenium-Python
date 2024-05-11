from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc



app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def scrap_x_municipio():
    busqueda = request.form['municipio']
    browser=uc.Chrome()
    
    busqueda=busqueda.replace(' ','-')
    ids=[] 
    url=f"https://www.idealista.com/venta-viviendas/{busqueda}-malaga/"
    browser.get(url)
    time.sleep(random.randint(10,12))
    try:
        # esto es para cerrar las cookies
        browser.find_element("xpath",'//*[@id="didomi-notice-agree-button"]').click()
    except:
        pass
    html=browser.page_source
    soup = bs(html, 'html.parser')
    articles = soup.find('main',{'class':'listing-items'}).find_all('article')
    for article in articles:
        # estamos obteniendo todos los id de cada inmueble y además eliminando los que devuelven None 
        id_muebles = article.get('data-element-id')
        ids.append(id_muebles)
        time.sleep(random.randint(1,3)),
    ids=[muebles for muebles in ids if muebles is not None]
    #convierto a Dataframe los id de los inmuebles
    ids_casas = pd.DataFrame(ids, columns=['id'])

    
    casas=pd.Series()
    #esta función saca la info de cada inmueble 
    def parsear_inmueble(id_inmueble):
        url=f"https://www.idealista.com/inmueble/{id_inmueble}/"
        browser.get(url)
        time.sleep(random.randint(10,12))
        try:
            browser.find_element("xpath",'//*[@id="didomi-notice-agree-button"]').click()
        except:
            pass

        html=browser.page_source
        soup = bs(html, 'html.parser')
        titulo=soup.find('span',{'class':'main-info__title-main'}).text
        localizacion=soup.find('span',{'class':'main-info__title-minor'}).text.split(",")[0]
        precio=int(soup.find('span',{'class':'txt-bold'}).text.replace('.',''))
        div_caracteristicas = soup.find('div', class_='details-property-feature-one')

        # Extraer las características básicas del inmueble
        if div_caracteristicas:
            ctas_basicas = [caract.text.strip() for caract in div_caracteristicas.find_all('li')]
        else:
            ctas_basicas = []
        
        div_extra = soup.find('div', class_='details-property-feature-two')
        if div_extra:
            ctas_extra = [caract.text.strip() for caract in div_extra.find_all('li')]
        else:
            ctas_extra = []
        
        ubicacion_desg=[zona.text.strip() for zona in soup.find('div',{'id':'headerMap'}).find_all('li')]

        #guardo los resultados en un dataframe que llamaré casa
        casas['titulo']=titulo
        casas['localizacion']=localizacion
        casas['precio']=precio
        casas['ctas_basicas']=ctas_basicas
        casas['ctas_extra']=ctas_extra
        casas['ubicacion_desg']=ubicacion_desg
        df=pd.DataFrame(casas)
        return(df.T)

    df_casas=parsear_inmueble(ids_casas.iloc[0].id)
    #solo mostraré 6 inmuebles en una tabla en el frontend
    for i in range(1, min(6, len(ids))):
        df_casas = pd.concat([df_casas, parsear_inmueble(ids[i])])
        time.sleep(random.randint(4, 8))

    data_list = df_casas.to_dict(orient='records')
    return render_template('index.html', data=data_list)
    

if(__name__=="__main__"):
    app.run(debug=True,host= '0.0.0.0',port=5000)



