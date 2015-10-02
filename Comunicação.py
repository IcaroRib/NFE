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

##tempo = 0
encontrouXML = "nao"
resposta=""
contador = 1
data = date.today()


listaDeChaves = [


#("26100424454886000101550010000000590000000598", "cnRepetido"),
#("26120308786654000102550010000000321000000323", "cnRepetido"),
#("26121008493134000101550010000004881000004880", "cnRepetido"),
#("26121107231408000113550000000001321000001327", "cnRepetido"),
#("26141109811654000170550100001123821001123823", "cnRepetido"),
#("26121111623188000655550010000169901000169902", "cnRepetido"),
#("26140908763294000115550010000020961000020960", "cnRepetido"),
#("26141209206498000118550010000015481000015488", "cnRepetido"),
#("26141204434408000122550010000003571000003576", "cnRepetido"),
#("26141209088948000115550010000025071000025070", "cnRepetido"),
#("26150211623188001899550010000291721000291727", "cnRepetido"),
#("26130610912293001966550000000007301000008600", "somador"),
#("26140811839719000137550010000054561000054565", "cnRepetido"),
#("26140907556072000169550010000004561000036482", "multiplicador"),
#("26121101377674000172550010000003861000030888", "multiplicador"),
##("26140200980971000145550010000006241010006242", "cnRepetido"),
##("26130943708379010598550010000257251000000017", "fixo"),
##("26140611623188001112550010000289051000289056", "cnRepetido"),
##("26141143708379010598550010000512961000000010", "fixo"),
##("26140500185372000130550010000010001000010006", "cnRepetido"),
##("26120701908026000103550010000010001000010009", "cnRepetido"),
##("26130705694130000195550010000020001000020006", "cnRepetido"),
##("26120209428405000108550010000010001000010004", "cnRepetido"),
##("26141011623188000817550010000311491000311490", "cnRepetido"),
##("26111210975119000133550010000010001000010001", "cnRepetido"),
##("26131204199007000488550010000010001000010009", "cnRepetido"),
##("26150304342730000121550010000020001000020004", "cnRepetido"),
##("26150102483001000160550010000020001000020003", "cnRepetido"),
##("26110507399435000108550010000010001000010003", "cnRepetido"),
##("26130707998863000149550010000020001000020007", "cnRepetido"),
##("26140705997476000162550010000010001000010000", "cnRepetido"),
##("26121012057437000140550010000010001000010008", "cnRepetido"),
##("26120605266246000123550010000020001000020005", "cnRepetido"),
##("26140215088054000128550010000010001000010008", "cnRepetido"),
##("26140807711012000173550010000031201000031205", "cnRepetido"),
##("26121101838829000120550010000010001000010001", "cnRepetido"),
##("26110408575154000113550010000020001000020006", "cnRepetido"),
##("26120104641887000158550010000010001000010000", "cnRepetido"),
##("26150111474375000100550010000020001000020003", "cnRepetido"),
##("26110711623188001201550010000010001000010001", "cnRepetido"),
##("26140818361562000126550010000010001000010004", "cnRepetido"),
##("26120200200671000104550010000010001000010003", "cnRepetido"),
##("26130401816329000198550010000010001000010003", "cnRepetido"),
##("26131203598907000192550010000010001000010002", "cnRepetido"),
##("26140411195603000102550010000010001000010009", "cnRepetido"),
##("26110711623188002194550010000010001000010000", "cnRepetido"),
##("26121112041869000163550010000010001000010000", "cnRepetido"),
##("26130712305624000104550010000010001000010003", "cnRepetido"),
##("26130508763492000189550010000010001000010000", "cnRepetido"),
##("26120110665917000169550010000010001000010003", "cnRepetido"),
##("26110400312673000187550010000020001000020007", "cnRepetido"),
##("26120701665341000149550010000010001000010005", "cnRepetido"),
##("26110802073130000180550010000030001000030001", "cnRepetido"),
##("26140402138273000122550010000010001000010009", "cnRepetido"),
##("26130102792860000130550010000010001000010000", "cnRepetido"),
##("26120111041333000185550010000010001000010002", "cnRepetido"),
##("26140915225751000183550010000010001000010000", "cnRepetido"),
##("26110711623188001112550010000010001000010004", "cnRepetido"),
##("26121203116141000162550010000020001000020000", "cnRepetido"),
##("26130502397168000108550010000010001000010007", "cnRepetido"),
##("26121204838724000402550010000010001000010000", "cnRepetido"),
##("26150105027195006703550010000010001000010002", "cnRepetido"),
##("26121206347409027870550010000010001000010004", "cnRepetido"),
##("26110608528729000147550010000030001000030004", "cnRepetido"),
##("26140700300568000128550020000869291000869290", "cnRepetido"),
##("26140409521975000210550010000010001000010003", "cnRepetido"),
##("26150424269417000112550010000040501000040509", "cnRepetido"),
##("26140911095677000177550010000005731000005731", "cnRepetido"),
##("26120912659779000130550000000056041000056044", "cnRepetido"),
##("26141269907756000115550010000032821000262562", "multiplicador"),
##("26140809379524000100550010000055411000443289", "multiplicador"),
##("26120504060236000174550010000010001000010004", "cnRepetido"),
##("26120104554147000184550010000010001000010000", "cnRepetido"),
##("26120104618334000184550010000010001000010000", "cnRepetido"),
##("26110905266210000573550010000010001000010004", "cnRepetido"),
##("26140106226929000110550010000010001000010001", "cnRepetido"),
##("26140207126674000186550010000010001000010002", "cnRepetido"),
##("26130407626826000100550010000010001000010000", "cnRepetido"),
##("26120408533211000100550010000010001000010009", "cnRepetido"),
##("26120609085324000144550010000010001000010008", "cnRepetido"),
##("26140409521975000210550010000010001000010003", "cnRepetido"),
##("26140915225751000183550010000010001000010000", "cnRepetido"),

("26140116952866000132550010000010001000010008", "cnRepetido"),


]


for tupla in listaDeChaves:

    chave = Chave(tupla[0], tupla[1])
    chaveTemp = Chave(tupla[0], tupla[1])
    chavePivor = Chave(tupla[0], tupla[1])
    procurandoAbaixo = True
    etapa1 = 0
    contaErro = 0
    continuarProcurando = True
    deuSalto = False
    chaveCancelada = 0
    saltoValido = False

    while continuarProcurando:
        
        encontrouXML = "nao"
        ini = time.time()

        if not os.path.exists('./Notas/'+chave.getCnpj()):
            os.mkdir ('./Notas/'+chave.getCnpj())
            os.mkdir ('./Notas/'+chave.getCnpj()+'/canceladas')
            print "----------------------------------------------------------------------"
            print "Diretorio criado - ", chave.getCnpj()
            print "----------------------------------------------------------------------"

        else:
            if not os.path.exists('./Notas/'+chave.getCnpj()+'/canceladas'):
                os.mkdir ('./Notas/'+chave.getCnpj()+'/canceladas')


        if chave.existeChave():
            print "Chave ja baixada - ",chave.getChave()
            encontrouXML = "sim"
            if int(chave.getNumero()) == 1:
                procurandoAbaixo = False
                chave = Chave(chavePivor.getChave(),chavePivor.getTipo())

        if chave.existeCanceladaChave():
            chaveTemp = Chave(chave.getChave(), tupla[1])
        if procurandoAbaixo:
        chaveTemp.decrementarData()
        if chaveTemp.existeCanceladaChave():
                    print "Chave cancelada confirmada - ",chave.getChave()
                    encontrouXML = "sim"
                    if etapa1 == 1:
                        chave.incrementarData()
                        etapa1 = 0
            else:
        chaveTemp.incrementarData()
        if chaveTemp.existeCanceladaChave():
                    print "Chave cancelada confirmada - ",chave.getChave()
                    encontrouXML = "sim"
                    if etapa1 == 1:
                        chave.decrementarData()
                        etapa1 = 0

        else:
            
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
                        etapa1 = 0
                        contaErro = 0
                        
                        if chave.existeChave():
                            print "Chave ja baixada - ",chave.getChave()
                            
                        else:
                            number = chave.getChave()
                            #print "Nova chave - "+number[0:25:]+'\033[40;33;1m'+number[25:34:]+'\033[m'+number[34::]
                            print "Nova chave - "+number
                            arquivo = open('./Notas/'+chave.getCnpj()+'/'+chave.getChave()+'.xml','w')
                            arquivo.write(resposta)
                            arquivo.close()

                        if int(chave.getNumero()) < 2:
                            procurandoAbaixo = False
                            chave = Chave(chavePivor.getChave(),chavePivor.getTipo())
                            
                        
                    elif "confere com a figura" in resposta:
                        print "Erro - Captcha"
                            
                    elif "existe na base" in resposta:
                        contaErro += 1
                        number = chave.getChave()
                        #print 'Erro Chave - '+number[0:25:]+'\033[40;31;1m'+number[25:34:]+'\033[m'+number[34::]+ '\t'+str(contaErro)
                        print 'Erro Chave - '+number+'\t'+str(contaErro)
                        if not chave.existeCanceladaChave():
                            if int(chave.getAno()) == int(str(data.year)[2:]):
                                if not int(chave.getMes()) == int(str(data.month)) or not int(chave.getMes()) == (int(str(data.month))+1):
                                    arquivo = open('./Notas/'+chave.getCnpj()+'/canceladas/'+chave.getChave()+'.txt','w')
                                    arquivo.close()
                            else:
                                arquivo = open('./Notas/'+chave.getCnpj()+'/canceladas/'+chave.getChave()+'.txt','w')
                                arquivo.close()
                        
                        if procurandoAbaixo:
                            if etapa1 == 0:
                                chave.decrementarData()
                                etapa1 = 1

                            else:
                                chave.incrementarData()
                                chave.decrementarChave()
                                etapa1 = 0

                        else:

                            if etapa1 == 0:
                                chave.incrementarData()
                                etapa1 = 1

                            else:
                                chave.decrementarData()
                                chave.incrementarChave()
                                etapa1 = 0

                        if int(chave.getNumero()) < 2:
                            procurandoAbaixo = False
                            chave = Chave(chavePivor.getChave(),chavePivor.getTipo())

                        if contaErro == 500:
                            if procurandoAbaixo:
                                procurandoAbaixo = False
                                chave = Chave(chavePivor.getChave(),chavePivor.getTipo())
                            else:
                                continuarProcurando = False
                break

                        if int(chave.getAno()) == int(str(data.year)[2:]):
                            if int(chave.getMes()) == int(str(data.month)) and contaErro > 30:
                                continuarProcurando = False
                break
            
            if int(chave.getAno()) < 12 and int(chave.getMes()) < 02 and contaErro > 200:
                procurandoAbaixo = False
                            chave = Chave(chavePivor.getChave(),chavePivor.getTipo())


    
                    else:
                        print "Erro desconhecido."
                        
                
                except IndexError:
                    print "Comunicacao com problemas."
                    
        if procurandoAbaixo:
            chave.decrementarChave()
        else:
            chave.incrementarChave()
