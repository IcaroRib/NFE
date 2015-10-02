arquivo = open('cnpjs.txt',"r")
cont = 0
for i in (arquivo.readlines()):
    if len(i) == 19 or len(i) == 20:
        cont = cont + 1
        i = i.replace("-","")
        i = i.replace("/","")
        i = i.replace(".","")
        i = i.replace(" ","")
        temp = open('./cnpj/'+i[0:14]+'.txt','w')
        temp.close()
arquivo.close()
print "Empresas inseridas: ",cont
