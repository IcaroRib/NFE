# -*- coding: cp1252 -*-
import mechanize, os, urllib2
from bs4 import BeautifulSoup
from PIL import Image
from StringIO import StringIO
from commands import getoutput
from xml.dom.minidom import parse
import types
from Oficial import *
from DicionarioBanco import *
from Chave import *
from datetime import date

encontrouXML = "nao"
resposta=""
contador = 1
numeroChavesEncontradas = 0
data = date.today()

listaDeCnpjs = []

arquivo = open('CNPJparaBusca.txt',"r")

for i in (arquivo.readlines()):
    if len(i) == 15:
        tupla = (i[0:14], "buscarPadrao")
        listaDeCnpjs.append(tupla)

arquivo.close()

for tupla in listaDeCnpjs:

    chave = Chave(tupla[0], tupla[1])

    continuarProcurando = True
    
    chaveCancelada = 0

    while continuarProcurando:

        cnpj = chave.getCnpj()
        
        encontrouXML = "nao"
        ini = time.time()
        while encontrouXML=="nao":
            try:
                browser = mechanize.Browser()
                browser.set_handle_robots(False)
                nfeEndereco = 'http://nfe.sefaz.pe.gov.br/nfe-web/'
                endereco1 = "%sentradaConsNfe?tp=C" % nfeEndereco
                html = browser.open(endereco1)
                soup = BeautifulSoup(html)
                image_tags = soup.findAll('img')
                i=0
             
                for image in image_tags:
                    if i==0:
                        filename = image['src'].lstrip('http://')
                        endereco2 = nfeEndereco+filename
                        imageData = browser.open(endereco2)
                        img = Image.open(imageData)
                        #img.show()
                    i=i+1

                captcha = resolve_captcha(img)
                browser.back()
                browser.select_form(nr = 0)        
                browser.form['chave'] = chave.getChave()
                browser.form['txtCodigoImpresso'] = captcha
                browser.method = "POST"
                response = browser.submit()
                resposta = response.read()
                if resposta[2:5]=="xml":
                    encontrouXML = "sim"
                    
                    arquivo = open('PadroesEncontrados.txt','a')
                    arquivo.write("A empresa "+chave.getCnpj()+" tem esse pivor : "+chave.getChave()+"\n")
                    arquivo.close()
                    print "A empresa ",chave.getCnpj()," tem esse pivor : ",chave.getChave() 

                    continuarProcurando = False
                    break
                    
                elif "confere com a figura" in resposta:
                    nada = 1
                        
                elif "existe na base" in resposta:
                    print "Erro - CHAVE", chave.getChave()                        
                    
                    if int(chave.getAno()) >= int(str(data.year)[2:]) and int(chave.getMes()) >= int(str(data.month)):
                        if int(chave.getNumero()) == 3000:
                            arquivo = open('PadroesEncontrados.txt','a')
                            arquivo.write("A empresa "+chave.getCnpj()+" nao tem padrao de repeticao.\n")
                            arquivo.close()
                            continuarProcurando = False
                            break
                        else:
                            chave.setAno("10")
                            chave.setMes("04")
                            chave.incrementarChave()

                    else:
                        chave.incrementarData()
                        

                else:
                    print "Erro desconhecido."
                    
            
            except Exception:
                print "Comunicacao com problemas."

    
