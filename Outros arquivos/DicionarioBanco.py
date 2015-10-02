from commands import getoutput
from xml.dom.minidom import parse
import types

def criarDicionario(xml):
    dic = {}
    for elemento in xml.childNodes:
        nome = str(elemento)[14:-14]
        if len(xml.getElementsByTagName(nome)[0].childNodes) == 1:
            xmlValor = xml.getElementsByTagName(nome)[0].toxml()
            valor = xmlValor[len(nome)+2:-(len(nome)+3)]
            dic[nome] = valor
        else:
            dic[nome] = criarDicionario(xml.getElementsByTagName(nome)[0])
    return dic

def printarDicionario(dic, espaco):
    for chave,valor in dic.iteritems():
        if type (valor) is type(dic):
            print espaco + chave + ": "
            printarDicionario(valor, espaco + "     ")
        else:
            print espaco + chave + " = " + valor


def ManipulaXML(chave):
    endereco = 'Notas/'+chave+'.xml'
    doc = parse(endereco)
    xml = doc.documentElement.getElementsByTagName("NFe")[0]
    xmlNota = xml.getElementsByTagName("infNFe")[0]

    #####elementos do IDE #########
    print "--------------elementos do IDE--------------"
    ide = xmlNota.getElementsByTagName("ide")[0]
    resultadoIDE = criarDicionario(ide)
    printarDicionario(resultadoIDE, "")

    #####elementos do EMIT #########
    print "--------------elementos do EMIT--------------"
    emit = xmlNota.getElementsByTagName("emit")[0]
    resultadoEMIT = criarDicionario(emit)
    printarDicionario(resultadoEMIT, "")

    #####elementos do DEST #########
    print "--------------elementos do DEST--------------"
    dest = xmlNota.getElementsByTagName("dest")[0]
    resultadoDEST = criarDicionario(dest)
    printarDicionario(resultadoDEST, "")

    ####elementos dos ITEMS#########
    print "--------------elementos dos ITEMS --------------"
    items = {}
    for i in range (0, len(xmlNota.getElementsByTagName("det"))):
        print "     ---- ITEM %i -------" %(i+1)
        det = xmlNota.getElementsByTagName("det")[i]
        resultadoDET = criarDicionario(det)
        printarDicionario(resultadoDET, "     ")
        items["numero" +str(i+1)] = resultadoDET

    #####elementos do TOTAL #########
    print "--------------elementos do TOTAL--------------"
    total = xmlNota.getElementsByTagName("total")[0]
    resultadoTOTAL = criarDicionario(total)
    printarDicionario(resultadoTOTAL, "")

    #####elementos do TRANSP #########
    transp = xmlNota.getElementsByTagName("transp")    
    if len(transp) > 0:
        print "--------------elementos da TRANSPORTADORA --------------"
        resultadoTRANSP = criarDicionario(transp[0])
        printarDicionario(resultadoTRANSP, "")

    ###elementos da COBR #########
    cobr = xmlNota.getElementsByTagName("cobr")
    if len(cobr) > 0:
        print "--------------elementos da COBR --------------"
        resultadoCOBR = criarDicionario(cobr[0])
        printarDicionario(resultadoCOBR, "")
