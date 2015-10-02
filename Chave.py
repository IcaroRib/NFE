from datetime import date
import os

##A parte comentada do construtor foi pela tentativa de buscar a primeira chave
##porem descobrimos que pode ser que nao exista a chave de numero "1", entao
##tomamos a decisao de nao usar esse metodo e utilizar um pivor.
##
##Ao criar a uma chave, ela deve ter os 44 digitos e o seu tipo, ou o CNPJ por exemplo:
##    Se for do tipo "SOMADOR": Que utiliza um numero somado no codigo numerico.
##        chave = Chave("26130610912293001966550000000007301000008600", "somador")
##    Se for do tipo "CNREPETIDO": Que utiliza o numero da nota no codigo numerico.
##        chave = Chave("26141024269417000112550010000035521000035525", "cnRepetico")
##    Se for do tipo "MULTIPLICADOR": Que utiliza o numero multiplicador por um determinado fator no codigo numerico.
##        chave = Chave("26140907556072000169550010000004561000036482", "multiplicador")
##    Se for do tipo "FIXO": Que utiliza o codigo numerico como numero fixo.
##        chave = Chave("26130943708379010598550010000257251000000017", "fixo")
##    Se for USAR O CNPJ para fazer busca de padrao, devemos classificar o tipo como buscaPadrao.
##        chave = Chave("43708379010598","buscarPadrao")

class Chave:

    def __init__(self, chave, tipo):

        self.__tipo = tipo
        self.__modelo = "55"
        self.__chave = ""
        self.__digitoVerificador = ""

        if len(chave) == 44:
            
            self.__uf = chave[0:2]
            self.__ano = chave[2:4]
            self.__mes = chave[4:6]
            self.__cnpj = chave[6:20]
            self.__serie = chave[22:25]
            self.__numero = chave[25:34]
            self.__separador = chave[34:35]
            self.__codNumerico = chave[35:43]

        elif len(chave) == 14:
            self.__uf = "26"
            self.__ano = "10"
            self.__mes = "04"
            self.__cnpj = chave
            self.__serie = "001"
            self.__numero = "000001000"
            self.__separador = "1"
            self.__codNumerico = "00001000"

        else:
            print "Formato Invalido"
            return

        self.__multiplicador = int(self.__codNumerico)/int(self.__numero)

        self.montarChave()
        
    def calcularDigitoVerificador(self, dado):        
        
        somatorio = 0
        peso = 2
        produto = 0
        for index in range(len(dado), 0, -1):
            charAux = dado[index-1]
            produto = int(charAux) * peso
            somatorio += produto
            
            if peso < 9:
                peso +=1

            else:
                peso = 2

        restoDivisao = somatorio%11
        digitoVerificador = 11 - restoDivisao
        if digitoVerificador == 11 or digitoVerificador == 10:
            digitoVerificador = 0

        self.__digitoVerificador = str(digitoVerificador)

    def montarChave(self):
        
        self.__chave = self.__uf + self.__ano + self.__mes + self.__cnpj + self.__modelo + self.__serie + self.__numero + self.__separador + self.__codNumerico
        self.calcularDigitoVerificador(self.__chave)
        self.__chave = self.__chave + self.__digitoVerificador

    def getDigitoVerificador(self):
        return self.__digitoVerificador

    def existeChave(self):
        existe = False
        if os.path.exists('../Final/Notas/'+self.getCnpj()+'/'+self.getChave()+'.xml'):
            existe = True
        return existe
    
    def existeCanceladaChave(self):
        existe = False
        if os.path.exists('../Final/Notas/'+self.getCnpj()+'/canceladas/'+self.getChave()+'.txt'):
            existe = True
        return existe


    def getUf(self):
        return self.__uf

    def getAno(self):
        return self.__ano

    def getMes(self):
        return self.__mes

    def setAno(self, ano):
        self.__ano = ano

    def setMes(self, mes):
        self.__mes = mes

    def getCnpj(self):
        return self.__cnpj

    def getSerie(self):
        return self.__serie

    def getNumero(self):
        return self.__numero

    def getCodNumerico(self):
        return self.__codNumerico

    def getModelo(self):
        return self.__modelo

    def getChave(self):
        return self.__chave

    def getTipo(self):
        return self.__tipo

    def getMultiplicador(self):
        return self.__multiplicador


    def incrementarData(self):

        if self.__mes == str("12"):

            self.__mes = "01"

            if int(self.__ano) >= 9:
                novoAno = int(self.__ano)+1
                self.__ano = str(novoAno)
            else:
                novoAno = int(self.__ano)+1
                self.__ano = "0"+ str(novoAno)

        else:
            if int(self.__mes) >= 9:
                novoMes = int(self.__mes)+1
                self.__mes = str(novoMes)
            else:
                novoMes = int(self.__mes)+1
                self.__mes = "0"+ str(novoMes)


        self.montarChave()


    def decrementarData(self):
        if self.__mes == str("01"):

            self.__mes = "12"

            if int(self.__ano) > 10:
                novoAno = int(self.__ano)-1
                self.__ano = str(novoAno)
            else:
                novoAno = int(self.__ano)-1
                self.__ano = "0"+ str(novoAno)

        else:
            if int(self.__mes) > 10:
                novoMes = int(self.__mes)-1
                self.__mes = str(novoMes)
            else:
                novoMes = int(self.__mes)-1
                self.__mes = "0"+ str(novoMes)


        self.montarChave()
        

    def decrementarChave(self):
        self.decrementarNumero()
        self.decrementarCodNumerico()
        self.montarChave()

    def decrementarChaveComPulo(self, numero):
        self.decrementarNumeroComPulo(numero)
        self.decrementarCNComPulo(numero)
        self.montarChave()

    def decrementarNumeroComPulo(self, valor):

        numero = int(self.__numero)
        demarcarQtnDigtidos = str(numero)
        numero -= valor
        numAuxiliar = str(numero)

        if len(demarcarQtnDigtidos) > len(numAuxiliar):
            novoNum = self.__numero[0:len(self.__numero) - (len(numAuxiliar)+1)]
            a = len(demarcarQtnDigtidos)
            while a > 0:
                novoNum += "0"
                a-=1
        else:
            novoNum = self.__numero[0:len(self.__numero) - len(numAuxiliar)]

        novoNum = novoNum + numAuxiliar
        self.__numero = novoNum

    def decrementarCNComPulo(self, valor):

        codigoNum = int(self.__codNumerico)
        demarcarQtnDigtidos = str(codigoNum)
        codigoNum -= valor
        cnAuxiliar = str(codigoNum)
        
        if len(demarcarQtnDigtidos) > len(cnAuxiliar):
            novoCN = self.__codNumerico[0:len(self.__codNumerico) - (len(cnAuxiliar)+1)]
            a = len(demarcarQtnDigtidos)
            while a > 0:
                novoCN += "0"
                a-=1
        else:
            novoCN = self.__codNumerico[0:len(self.__codNumerico) - len(cnAuxiliar)]
            
        novoCN = novoCN + cnAuxiliar
        self.__codNumerico = novoCN
        

    def decrementarNumero(self):

        numero = int(self.__numero)
        demarcarQtnDigtidos = str(numero)
        numero -= 1
        numAuxiliar = str(numero)

        if len(demarcarQtnDigtidos) > len(numAuxiliar):
            novoNum = self.__numero[0:len(self.__numero) - (len(numAuxiliar)+1)]
            novoNum += "0"
        else:
            novoNum = self.__numero[0:len(self.__numero) - len(numAuxiliar)]

        novoNum = novoNum + numAuxiliar
        self.__numero = novoNum
        
    def decrementarCodNumerico(self):

        if self.getTipo().upper() == "CNREPETIDO" or self.getTipo().upper() == "SOMADOR":   

            codigoNum = int(self.__codNumerico)
            demarcarQtnDigtidos = str(codigoNum)
            codigoNum -=1
            cnAuxiliar = str(codigoNum)
            
            if len(demarcarQtnDigtidos) > len(cnAuxiliar):
                novoCN = self.__codNumerico[0:len(self.__codNumerico) - (len(cnAuxiliar)+1)]
                novoCN += "0"
            else:
                novoCN = self.__codNumerico[0:len(self.__codNumerico) - len(cnAuxiliar)]
                
            novoCN = novoCN + cnAuxiliar
            self.__codNumerico = novoCN

        elif self.getTipo().upper() == "MULTIPLICADOR":
            
            codigoNum = int(self.__codNumerico)
            demarcarQtnDigtidos = str(codigoNum)
            
            codigoNum = int(self.__numero)*self.getMultiplicador()
            cnAuxiliar = str(codigoNum)

            if len(demarcarQtnDigtidos) > len(cnAuxiliar):
                novoCN = self.__codNumerico[0:len(self.__codNumerico) - (len(cnAuxiliar)+1)]
                novoCN += "0"
            else:
                novoCN = self.__codNumerico[0:len(self.__codNumerico) - len(cnAuxiliar)]
                
            novoCN = novoCN + cnAuxiliar
            self.__codNumerico = novoCN

        elif self.getTipo().upper() == "FIXO":

            self.__codNumerico = self.__codNumerico

        
    def incrementarChave(self):
        self.incrementarNumero()
        self.incrementarCodNumerico()
        self.montarChave()

    def incrementarNumero(self):

        if self.getTipo().upper() == "CNREPETIDO" or self.getTipo().upper() == "SOMADOR" or self.getTipo().upper() == "ALEATORIO" or self.getTipo().upper() == "MULTIPLICADOR":

            numero = int(self.__numero)
            numero += 1

            numAuxiliar = str(numero)
            novoNum = self.__numero[0:len(self.__numero) - len(numAuxiliar)]

            novoNum = novoNum + numAuxiliar
            self.__numero = novoNum

        elif self.getTipo().upper() == "BUSCARPADRAO":

            numero = int(self.__numero)
            numero += 1000

            numAuxiliar = str(numero)
            novoNum = self.__numero[0:len(self.__numero) - len(numAuxiliar)]

            novoNum = novoNum + numAuxiliar
            self.__numero = novoNum
        
    def incrementarCodNumerico(self):

        if self.getTipo().upper() == "CNREPETIDO" or self.getTipo().upper() == "SOMADOR" or self.getTipo().upper() == "ALEATORIO":

            codigoNum = int(self.__codNumerico)
            codigoNum +=1

            cnAuxiliar = str(codigoNum)
            novoCN = self.__codNumerico[0:len(self.__codNumerico) - len(cnAuxiliar)]

            novoCN = novoCN + cnAuxiliar
            self.__codNumerico = novoCN

        elif self.getTipo().upper() == "MULTIPLICADOR":
        
            codigoNum = int(self.__codNumerico)
            demarcarQtnDigtidos = str(codigoNum)
            
            codigoNum = int(self.__numero)*self.getMultiplicador()
            cnAuxiliar = str(codigoNum)

            if len(demarcarQtnDigtidos) > len(cnAuxiliar):
                novoCN = self.__codNumerico[0:len(self.__codNumerico) - (len(cnAuxiliar)+1)]
                novoCN += "0"
            else:
                novoCN = self.__codNumerico[0:len(self.__codNumerico) - len(cnAuxiliar)]
                
            novoCN = novoCN + cnAuxiliar
            self.__codNumerico = novoCN

        elif self.getTipo().upper() == "FIXO":

            self.__codNumerico = self.__codNumerico

        elif self.getTipo().upper() == "BUSCARPADRAO":

            codigoNum = int(self.__codNumerico)
            codigoNum += 1000

            cnAuxiliar = str(codigoNum)
            novoCN = self.__codNumerico[0:len(self.__codNumerico) - len(cnAuxiliar)]

            novoCN = novoCN + cnAuxiliar
            self.__codNumerico = novoCN

    def incrementarChaveComPulo(self, numero):

        self.incrementarNumeroComPulo(numero)
        self.incrementarCNComPulo(numero)
        self.montarChave()

    def incrementarNumeroComPulo(self, valor):

        numero = int(self.__numero)
        numero += valor

        numAuxiliar = str(numero)
        novoNum = self.__numero[0:len(self.__numero) - len(numAuxiliar)]

        novoNum = novoNum + numAuxiliar
        self.__numero = novoNum

    def incrementarCNComPulo(self, valor):
        
        codigoNum = int(self.__codNumerico)
        codigoNum += valor

        cnAuxiliar = str(codigoNum)
        novoCN = self.__codNumerico[0:len(self.__codNumerico) - len(cnAuxiliar)]

        novoCN = novoCN + cnAuxiliar
        self.__codNumerico = novoCN


##    def notasCodNumericoAleatorioAAMM(self):
##
##        pivor = Chave(self.getChave(), self.getTipo())
##
##        possiveisNotasAAMM = []
##        possiveisNotasNumeroX = []
##
##        while int(self.__numero) < 999999: #coloquei ate o numero 999.999 para diminuir 
##        #o processamento pois nao temos empresas na nossa base de notas que tem mais 
##        #que essa quantidade de notas
##
##            self.__codNumerico = "00000000"
##
##            while int(self.__codNumerico) < 99999999:
##
##                self.incrementarCodNumerico()
##                self.montarChave()
##
##                chaveAuxiliar = Chave(self.getChave(), self.getTipo())
##
##                possiveisNotasNumeroX.append(chaveAuxiliar)
##
##
##            possiveisNotasAAMM.append(possiveisNotasNumeroX)
##            possiveisNotasNumeroX = []
##            self.incrementarNumero()
##
##        return possiveisNotasAAMM, pivor
