# -*- coding: cp1252 -*-
import time
import hashlib
import os, sys
from PIL import Image


tempo = 0
i=1
quantidadeX=0
quantidadeY=0

def mapeamento(im):
    soma = 0
    inicio=0
    fim = 0
    inicioEncontrado = False
    fimEncontrado = False
    linhas=[]
    colunas=[]
    w,h = im.size

    imnova = Image.new("RGB",(w,h))
    #Dimensao 30
    for x in range(w):
        soma = 0
        for y in range(h):
            r,g,b = im.getpixel((x,y))
            if b==0:
                soma = soma +1
        colunas.append(soma)
    #Dimensao 39
    for y in range(h):
        soma = 0
        for x in range(w):
            r,g,b = im.getpixel((x,y))
            if b==0:
                soma = soma +1
        linhas.append(soma)

    resultado=metricas(colunas,linhas)
    return resultado

def metricas(colunas,linhas):
    R1 = False
    R2 = False
    R3 = 0
    R4 = 0
    R5 = False
    R6 = False
    R7 = False
    R8 = 0
    R9 = False
    R10 = False
    R10a = 0.0
    R11 = False
    R12a = False
    R12b = False
    R12c = False
    R12d = False
    R12_ajuste = False
    R13 = False
    R14a = False
    R14c = False
    R14b = False
    R14d = False
    R15 = False
    R16a = False
    R16b = False
    R16_ajusteA = 0
    R16_ajusteB = False
    R17a = False
    R17b = False
    R18 = False
    R19 = False
    R20 = False
    R21 = False
    R22 = False
    R23a = False
    R23b = False
    R23c = 50
    R24a = 0
    R24b = False
    R25 = False
    R26b = 0.0
    R28 = False
    R30a = False
    R30b = False
    R31a = 0
    R31b = 0
    R32 = False
    R33 = False
    R34 = False
    R35 = False
    R36 = False
    R37 = False
    R38 = False
    R39 = False
    R40 = 0
    R41 = False
    R42a = False
    R42b = False
    R42c = False
    R43 = False
    R44 = False
    R45 = False
    R46a = False
    R46b = False
    R46c = False
    R47 = 0
    R48 = False
    R49 = False
    R50 = False
    R51a = False
    R51b = False
    R51b_aux1 = 0
    R51b_aux2 = 0
    R52 = False
    R53 = 0
    R54 = False
    R55 = False
    R56 = False
    R57 = False
    R58 = False
    R59 = 0
    R59A = False
    R60a = 0
    R60b = False
    R61 = False
    R62 = False
    R63 = False
    R64 = False
    R65 = False
    R66 = 0.0
    R67 = 0.0
    R68 = 0.0
    R70 = False
    R71 = False
    R71_ajuste = False
    R72 = False
    R72_ajuste = False
    R72_ajuste2 = False
    R72_ajuste3 = False
    R72_ajuste4 = False
    R73 = 0
    R74 = False
    R75 = False
    R76 = 0
    R77a = False
    R77b = False
    R78 = False
    R79a = False
    R79b = 0
    R80a = False
    R80b = False
    R81 = False
    R82 = False
    R83 = False
    R84 = False
    R85 = False
    R86 = False
    R87 = False
    R88 = False
    R89 = False
    R90 = False
    R91 = 0
    R92 = False
    R93 = 0
    R94 = False
    R95 = False
    R96a = False
    R96b = False
    R97 = False
    R98 = False
    R99 = False
    R100 = False
    R101 = False
    R102 = False
    R103 = False
    R104 = 0
    

    ##----------------------------------------------------------------------------------------------------------------------------------------------------
    ##----------------------------------------------------------------------------------------------------------------------------------------------------

    ##  R61: As colunas 17, 18 e 19 têm 25PP+ e as linhas 22 e 23 têm 20PP+ 
    if colunas[16]>=25 and colunas[17]>=25 and colunas[18]>=25  and linhas[21]>=20 and linhas[22]>=20:
        R61 = True
    
    ##  R66: A média das linhas 16 a 20 é 12PP+ ou (essa média é 10PP+ e a média das linhas 29 a 32 é 14PP+)
    R66 = (linhas[15]+linhas[16]+linhas[17]+linhas[18]+linhas[19])/5.0


    
    ##  R67: A média das linhas 29 a 32 é 14PP+
    R67 = (linhas[28]+linhas[29]+linhas[30]+linhas[31])/4.0
    
    ##  R68: A média das linhas 29 a 32 é no máximo 10,5PP+
    R68 = (linhas[28]+linhas[29]+linhas[30]+linhas[31])/4.0
    
    ##  R10-1: Entre as linhas 17 e 27, a média é maior que 21
    ##  R10-2: Entre as linhas 17 e 27, a média está entre 15 e 20
    R10a = (linhas[16]+linhas[17]+linhas[18]+linhas[19]+linhas[20]+linhas[21]+linhas[22]+linhas[23]+linhas[24]+linhas[25]+linhas[26])/11.0

    ##  R18: Entre as colunas 12 e 14 tem apenas valores 5PP-
    if colunas[11]>=1 and colunas[11]<=5 and colunas[12]>=1 and colunas[12]<=5 and colunas[13]>=1 and colunas[13]<=5:
        R18 = True

    ##  R25: Entre as linhas 30 e 32 tem apenas valores 13PP+
    if linhas[29]>=13 and linhas[30]>=13 and linhas[31]>=13:
        R25 = True

    ##  R26: Tem ao menos 3 colunas com 20PP+ e das linhas 10 a 14 tem média de 9,8PP+ (lembrar que vamos usar R24a)
    R26b = (linhas[9]+linhas[10]+linhas[11]+linhas[12]+linhas[13])/5.0

    ##  R28: A linha 5 é diferente de 0 e 1
    if linhas[4]>=2:
        R28 = True

    ##  R30: Entre as colunas 13 e 15 a soma delas tem 60PP+  ou uma sequência de 4 colunas com 20PP+
    if (colunas[12]+colunas[13]+colunas[14])>=60:
        R30a = True

    ##  R32: Entre as linhas 29 e 32 o somatório de pontos é 65PP+
    if (linhas[28]+linhas[29]+linhas[30]+linhas[31])>=65:
        R32 = True

    ##  R33: Tem valor 2PP+ na 5ª linha
    if linhas[4]>=2:
        R33 = True

    ##  R34: Termina até a coluna 18
    if colunas[18]<2:
        R34 = True

    ##  R41: A linha 32 tem 15PP+
    if linhas[31]>=15:
        R41 = True

    ##  R44: Entre as linhas 24 e 25  o menor valor é 7PP+
    if linhas[23]>=7 and linhas[24]>=7:
        R44 = True

    ##  R72: Entre as linhas 24 e 26 tem ao menos uma coluna com 15PP+
    if (linhas[23]>=15 or linhas[24]>=15 or linhas[25]>=15):
        R72 = True

    ##  R77: Entre as colunas 20 e 25 só tem valores entre 6PP+ e 9PP- e não tem 4 linhas seguidas com 5PP-
    if colunas[19]>=6 and colunas[19]<=9 and colunas[20]>=6 and colunas[20]<=9 and colunas[21]>=6 and colunas[21]<=9 and colunas[22]>=6 and colunas[22]<=9 and colunas[23]>=6 and colunas[23]<=9 and colunas[24]>=6 and colunas[24]<=9:
        R77a = True

    ##  R78: Entre as linhas 19 e 23 tem uma sequência de 4 linhas com 15PP+ e termina na coluna 22
    if ((linhas[18]>=15 and linhas[19]>=15 and linhas[20]>=15 and linhas[21]>=15) or (linhas[19]>=15 and linhas[20]>=15 and linhas[21]>=15 and linhas[22]>=15)) and colunas[21]<2:
        R78 = True

    ##  R79: Sempre termina até a coluna 17 e entre as colunas 5 e 7 tem ao menos duas com 20PP+
    if colunas[17]<2:
        R79a = True

    ##  R81: A linha 12 tem 0PP
    if linhas[11]<2:
        R81 = True

    ##  R82: Entre as colunas 10 e 11 tem alguma com 9PP-
    if (colunas[9]>=1 and colunas[9]<=9) or (colunas[10]>=1 and colunas[10]<=9):
        R82 = True

    ##  R83: Entre as linhas 20 e 22 só tem valores 10PP+
    if linhas[19]>=10 and linhas[20]>=10 and linhas[21]>=10:
        R83 = True

    ##  R84: Tem, nas linhas 24 e 26, ao menos uma delas com 15PP+
    if linhas[23]>=15 or linhas[25]>=15:
        R84 = True

    ##  R87: A linha 31 tem um 15PP+
    if linhas[30]>=15:
        R87 = True

    ##  R90: Linha 13 tem 1PP-
    if linhas[12]<2:
        R90 = True

    ##  R95: A coluna 22 é 0PP
    if colunas[21]<2:
        R95 = True

    ##  R98: A coluna 16 é 0PP
    if colunas[15]<2:
        R98 = True

    ##  R99: A linha 10 tem um 9PP+
    if linhas[9]>=9:
        R99 = True

    ##  R103: A linha 32 é 15PP+
    if linhas[31]>=15:
        R103 = True

    ##----------------------------------------------------------------------------------------------------------------------------------------------------
    ##----------------------------------------------------------------------------------------------------------------------------------------------------

    for x in range(len(linhas)):

        ##  R1:  Tem valor em uma das duas últimas duas linhas
        if x>36 and linhas[x]!=0:
            R1 = True

        ##  R52: Entre as linhas 14 e 18 tem apenas valores com 25PP+
        if x==13 and linhas[x]>=25 and linhas[x+1]>=25 and linhas[x+2]>=25 and linhas[x+3]>=25 and linhas[x+4]>=25:
            R52 = True

        ##  R10: Tem ao menos 25 PP numa linha
        if linhas[x]>=25:
            R10 = True
        
        ##  R11: Entre as linhas 22 e 32, tem uma sequência de 4 linhas com 5PP-
        if x>20 and x<32 and linhas[x]>=1 and linhas[x]<=5 and linhas[x+1]>=1 and linhas[x+1]<=5 and linhas[x+2]>=1 and linhas[x+2]<=5 and linhas[x+3]>=1 and linhas[x+3]<=5:
            R11 = True

        ##  R12_ajuste:: A coluna 11 tem 15PP+ ou entre as linhas 27 e 33 tem uma sequência de 5 linhas com 6PP+ e 9PP-
        if colunas[10]>=15 or colunas[11]>=15:
            R12_ajuste = True
        
        ##  R14: Entre as linhas 31 e 32 tem algum 16PP+ e coluna 13 é 15PP+ OU tem entre essas linhas uma com 15PP e até a 5ª coluna ter 14PP-
        if x==30 and (linhas[x]>=16 or linhas[x+1]>=16):
            R14a = True
        elif x==30 and (linhas[x]>=15 or linhas[x+1]>=15):
            R14c = True

        ##  R15: Tem uma sequência de 4 linhas com 20PP+ e termina ao menos na linha 36
        if x<35 and linhas[x]>=20 and linhas[x+1]>=20 and linhas[x+2]>=20 and linhas[x+3]>=20 and linhas[34]>1:
            R15 = True

        ##  R16_ajuste:: Até a linha 11 tem duas linhas com 15PP+
        if x<11 and linhas[x]>=15:
            R16_ajusteA = R16_ajusteA + 1
        if colunas[13]<20 and colunas[14]<15:
            R16_ajusteB = True
        
        ##  R22: Entre as linhas 22 e 25 só tem 16PP+
        if x==21 and linhas[x]>=16 and linhas[x+1]>=16 and linhas[x+2]>=16 and linhas[x+3]>=16:
            R22 = True

        ##  R37: Tem uma sequência de 6 linhas com 15PP+
        if x<34 and linhas[x]>=15 and linhas[x+1]>=15 and linhas[x+2]>=15 and linhas[x+3]>=15 and linhas[x+4]>=15 and linhas[x+5]>=15:
            R37 = True

        ##  R40: A partir da linha 28 tem ao menos duas linhas com 15PP+
        if x>26 and linhas[x]>=15:
            R40 = R40 + 1

        ##  R42: Tem uma sequência de 4 linhas com 15PP+  OU duas linhas com 15PP antes da linha 10 e 
        ##        não ter duas linhas sequidas com 5PP- entre as linhas 14 e 20"
        if x<36 and linhas[x]>=15 and linhas[x+1]>=15 and linhas[x+2]>=15 and linhas[x+3]>=15:
            R42a = True
        if x<10 and linhas[x]>=15 and linhas[x+1]>=15:
            R42b = True
        if x>12 and x<20 and linhas[x]>=1 and linhas[x]<=5 and linhas[x+1]>=1 and linhas[x+1]<=5:
            R42c = True

        ##  R43: Até a linha 13 tem uma sequência de 3 linhas com 10PP+
        if x<11 and linhas[x]>=10 and linhas[x+1]>=10 and linhas[x+2]>=10:
            R43 = True

        ##  R48: Até a linha 25 tem uma sequência de 3 linhas com 15PP+
        if x<23 and linhas[x]>=15 and linhas[x+1]>=15 and linhas[x+2]>=15:
            R48 = True

        ##  R70: Da linha 18 em diante, não tem qualquer linha com 11PP+
        if x>16 and linhas[x]>=11:
            R70 = True

        ## R72_ajuste:: Tem uma sequência de 4 linhas com 15PP+
        if x<36 and linhas[x]>=15 and linhas[x+1]>=15 and linhas[x+2]>=15 and linhas[x+3]>=15:
            R72_ajuste = True

        ## R72_ajuste3:: Da linha 28 em diante, tem uma coluna com 15PP+
        if x>26 and linhas[x]>=15:
            R72_ajuste3 = True

        ## R72_ajuste4:: Tem 15PP+ até a coluna 6 ou a linha 21
        if x<21 and linhas[x]>=15:
            R72_ajuste4 = True

        ##  R74: Entre as linhas 15 e 27 tem ao menos uma coluna com 5PP-
        if x>13 and x<27 and linhas[x]>=1 and linhas[x]<=5:
            R74 = True

        ##  R75: Entre as linhas 15 e 21 só tem valores 10PP+
        if x>13 and x<21 and linhas[x]<=9:
            R75 = True

        ##  R77: Entre as colunas 20 e 25 só tem valores entre 6PP+ e 9PP- e não tem 4 linhas seguidas com 5PP-
        if x<36 and linhas[x]>=1 and linhas[x]<=5 and linhas[x+1]>=1 and linhas[x+1]<=5 and linhas[x+2]>=1 and linhas[x+2]<=5 and linhas[x+3]>=1 and linhas[x+3]<=5:
            R77b = True

        ##  R80: Entre as colunas 12 e 15 tem uma sequência  de 3 colunas com 15PP+  e entre as linhas 15 e 20 não tem 5PP-
        if x>13 and x<20 and linhas[x]>=1 and linhas[x]<=5:
            R80b = True

        ##  R86: Entre as linhas 23 e 30 tem ao menos uma com 9PP-
        if x>21 and x<30 and linhas[x]>=1 and linhas[x]<=9:
            R86 = True

        ##  R88: Tem uma sequência de 4 linhas com 15PP+ e tem a linha 13 com 1PP-
        if x<36 and linhas[x]>=15 and linhas[x+1]>=15 and linhas[x+2]>=15 and linhas[x+3]>=15 and linhas[12]<2:
            R88 = True

        ##  R89: Entre as linhas 17 e 19 tem apenas valores 8PP-
        if x>15 and x<19 and linhas[x]>=9:
            R89 = True

        ##  R96: Tem duas linhas seguidas ou três colunas seguidas com 20PP+
        if x<38 and linhas[x]>=20 and linhas[x+1]>=20:
            R96a = True

        ##  R97: Entre as linhas 20 e 29 tem ao menos 3 linhas seguidas com 1PP+ e 5PP-
        if x>18 and x<27 and linhas[x]>=1 and linhas[x]<=5 and linhas[x+1]>=1 and linhas[x+1]<=5 and linhas[x+2]>=1 and linhas[x+2]<=5:
            R97 = True

        ##  R104: Entre as linhas 25 e 32 tem ao menos 7 linhas com 10PP+ e 14PP-
        if x>23 and x<32 and linhas[x]>=10 and linhas[x]<=14:
            R104 = R104 + 1

    
    ##----------------------------------------------------------------------------------------------------------------------------------------------------
    ##----------------------------------------------------------------------------------------------------------------------------------------------------

    for x in range(len(colunas)):
        
        ##  R2:  Depois do Pixel 15, tem alguma coluna com pelo menos 25 pontos
        if x>14 and colunas[x]>=25:
            R2 = True
        
        ##  R3:  Até coluna 10 tem ao menos 3 colunas com 25 PP em diante
        if x<10 and colunas[x]>=25:
            R3 = R3 + 1
        
        ##  R4:  Até coluna 7 tem 3 colunas com 20PP ou mais
        if x<7 and colunas[x]>=20:
            R4 = R4 + 1
        
        ##  R5:  Do Pixel 15 em diante, tem 3 colunas seguidas com 20PP ou +
        if x>13 and x<28 and colunas[x]>=20 and colunas[x+1]>=20 and colunas[x+2]>=20:
            R5 = True
        
        ##  R6:  Tem uma sequência de 6 colunas com 15 PP ou +
        if x<24 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15 and colunas[x+3]>=15 and colunas[x+4]>=15 and colunas[x+5]>=15:
            R6 = True
        
        ##  R7:  Até a 10ª coluna tem uma coluna com ao menos 20 PP
        if x<10 and colunas[x]>=20:
            R7 = True
        
        ##  R8:  Somando os PP das colunas 10 a 14 tem pelo menos 60 pontos
        if x>8 and x<14:
            R8 = R8 + colunas[x]
        
        ##  R9:  Tem ao menos 25 PP numa coluna
        if colunas[x]>=25:
            R9 = True
        
        ##  R50::  Até a coluna 10, tem uma coluna com 25PP ou mais
        if x<10 and colunas[x]>=25:
            R50 = True

        ##  R51::  Da coluna 10 a 14 tem 5 colunas com 25PP+ ou 4 colunas com 25PP+ e uma com ao menos 20PP
        if x==9 and colunas[x]>=25 and colunas[x+1]>=25 and colunas[x+2]>=25 and colunas[x+3]>=25 and colunas[x+4]>=25:
            R51a = True
        if x==9:
            if colunas[x]>=25:
                R51b_aux1 = R51b_aux1 +1
            if colunas[x+1]>=25:
                R51b_aux1 = R51b_aux1 +1
            if colunas[x+2]>=25:
                R51b_aux1 = R51b_aux1 +1
            if colunas[x+3]>=25:
                R51b_aux1 = R51b_aux1 +1
            if colunas[x+4]>=25:
                R51b_aux1 = R51b_aux1 +1
            if colunas[x]>=20 and colunas[x]<25:
                R51b_aux2 = R51b_aux2 +1
            if colunas[x+1]>=20 and colunas[x]<25:
                R51b_aux2 = R51b_aux2 +1
            if colunas[x+2]>=20 and colunas[x]<25:
                R51b_aux2 = R51b_aux2 +1
            if colunas[x+3]>=20 and colunas[x]<25:
                R51b_aux2 = R51b_aux2 +1
            if colunas[x+4]>=20 and colunas[x]<25:
                R51b_aux2 = R51b_aux2 +1
            if R51b_aux1>=4 and R51b_aux2>=1:
                 R51b = True
        
        
        ##  R53: Da coluna 13 em diante, tem ao menos duas colunas com 25PP+
        if x>11 and colunas[x]>=25:
            R53 = R53 + 1

        ##  R54: Até a coluna 8, tem uma coluna com 25PP, coluna 14 é abaixo de 20 e colunas 18 e 19 são 0PP
        if x<8 and colunas[x]>=25 and colunas[13]<20 and colunas[17]<2 and colunas[18]<2:
            R54 = True

        ##  R55: Tem ao menos 25 PP na coluna 3
        if x<3 and colunas[x]>=25:
            R55 = True
        
        ##  R56: Até a coluna 8, não se tem qualquer coluna com 20PP+
        if x<8 and colunas[x]>=20:
            R56 = True
        
        ##  R57: A coluna 10 tem 25PP+
        if x==9 and colunas[x]>=25:
            R57 = True
        
        ##  R58: A coluna 13 ou 16 tem 25PP+
        if x==13 and colunas[x]>=25:
            R58 = True
        if x==16 and colunas[x]>=25:
            R58 = True
        
        ##  R59: Até a coluna 10 tem ao menos 5 colunas com 25PP+
        if x<10 and colunas[x]>=25:
            R59 = R59 + 1
        
        ##  R59A: Da coluna 14 em diante, tem alguma coluna com 20PP+
        if x>12 and colunas[x]>=20:
            R59A = True
        
        ##  R60: Tem no máximo 3 colunas com 20PP+ e no mínimo 4 colunas seguidas com 1PP+ e 5PP-
        if colunas[x]>=20:
            R60a = R60a + 1
        if x< 27 and colunas[x]>=1 and colunas[x]<=5 and colunas[x+1]>=1 and colunas[x+1]<=5 and colunas[x+2]>=1 and colunas[x+2]<=5 and colunas[x+3]>=1 and colunas[x+3]<=5:
            R60b = True
        
        ##  R62: Da coluna 19 em diante, tem ao menos uma coluna com 25 PP
        if x>17 and colunas[x]>=25:
            R62 = True
        
        ##  R63:  Todas colunas têm 9PP+
        if not(colunas[x]==0 or colunas[x]==1) and colunas[x]<=9:
            R63 = True
        
        ##  R64: Tem ao menos 28PP entre as colunas 11 e 15 ou as colunas 11,12,13 tem 25PP+
        if (x>9 and x<15 and colunas[x]>=28) or (colunas[10]>=25 and colunas[11]>=25 and colunas[12]>=25):
            R64 = True
        
        ##  R65: Até a coluna 5, tem ao menos uma coluna com 20PP+
        if x<5 and colunas[x]>=20:
            R65 = True
        
        ##  R12: Até a coluna 8 tem ao menos duas colunas seguidas com 20PP+ e após coluna 10 não tem nenhuma coluna com 20PP+
        ##       OU tem entre as colunas 6 e 8 três colunas com valor 15PP+ e depois da coluna 11 mais nenhuma coluna com 20PP+
        if x<8 and colunas[x]>=20 and colunas[x+1]>=20:
            R12a = True
        if x>8 and colunas[x]>=20:
            R12b = True
        if x==5 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15:
            R12c = True
        if x>9 and colunas[x]>=20:
            R12d = True

        ##  R13: Até a coluna 6 tem alguma com 20PP+
        if x<6 and colunas[x]>=20:
            R13 = True
        
        ##  R14: Entre as linhas 31 e 32 tem algum 16PP+ e coluna 13 é 15PP+ OU tem entre essas linhas uma com 15PP e até a 5ª coluna ter 14PP-
        if x==12 and colunas[x]>=15:
            R14b = True
        if x<5 and colunas[x]>=15:
            R14d = True
        
        ##  R16: Entre as colunas 10 e 15 ter uma com 20PP+ e até coluna 5 ter no máximo 12PP
        ##       OU entre colunas 10 e 15 ter uma sequência de 4 colunas com 15PP+ e e até coluna 5 ter no máximo 12PP
        if (colunas[9]>=20 or colunas[10]>=20 or colunas[11]>=20 or colunas[12]>=20 or colunas[13]>=20 or colunas[14]>=20) and colunas[0]<=12 and colunas[1]<=12 and colunas[2]<=12 and colunas[3]<=12 and colunas[4]<=12:
            R16a = True
        if x>8 and x<12 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15 and colunas[x+3]>=15 and colunas[0]<=12 and colunas[1]<=12 and colunas[2]<=12 and colunas[3]<=12 and colunas[4]<=12:
            R16b = True
        
        ##  R17: Tem uma coluna com 17PP+ após a coluna 10 ou não possuir uma sequência de 5 colunas com 9PP- dif de zero
        if x>8 and colunas[x]>=17:
            R17a = True
        if x<26 and colunas[x]>=1 and colunas[x]<=9 and colunas[x+1]>=1 and colunas[x+1]<=9 and colunas[x+2]>=1 and colunas[x+2]<=9 and colunas[x+3]>=1 and colunas[x+3]<=9 and colunas[x+4]>=1 and colunas[x+4]<=9:
            R17b = True

        ##  R19: Tem um sequência de 3 colunas com 15PP+
        if x<28 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15:
            R19 = True

        ##  R20: Tem uma sequência de 5 colunas com 9PP-
        if x<26 and colunas[x]>=1 and colunas[x]<=9 and colunas[x+1]>=1 and colunas[x+1]<=5 and colunas[x+2]>=1 and colunas[x+2]<=5 and colunas[x+3]>=1 and colunas[x+3]<=5 and colunas[x+4]>=1 and colunas[x+4]<=5:
            R20 = True

        ##  R21: Da coluna 16 em diante, tem ao menos uma coluna com 20PP+
        if x>14 and colunas[x]>=20:
            R21 = True

        ##  R23: Até a coluna 12 não tem qualquer coluna com 17PP+ e da coluna 14 a 20 tem uma sequência de 3 colunas com 20PP 
        ##       e entre as colunas 7 e 12 o menor valor de coluna é 9PP-"
        if x<12 and colunas[x]>=17:
            R23a = True
        if x>12 and x<20 and colunas[x]>=20 and colunas[x+1]>=20 and colunas[x+2]>=20:
            R23b = True
        if x>5 and x<12 and R23c>colunas[x]:
            R23c = colunas[x]

        ##  R24: Tem no mínimo 7 colunas com 20PP+ e uma sequência de 4 colunas com 9PP- 
        ##  R26: Tem no mínimo 3 colunas com 20PP+ e das linhas 10 a 14 tem média de 9,8PP+ (usar R24a)
        ##  R27: Tem no máximo 2 colunas com 20PP+ (usar R24a)
        ##  R29: Tem no mínimo 5 colunas com 20PP+ (usar R24a)



        if colunas[x]>=20:
            R24a = R24a + 1
        if x<27 and colunas[x]>=1 and colunas[x]<=9 and colunas[x+1]>=1 and colunas[x+1]<=9 and colunas[x+2]>=1 and colunas[x+2]<=9 and colunas[x+3]>=1 and colunas[x+3]<=9:
            R24b = True

        ##  R30: Entre as colunas 13 e 15 a soma delas tem 60PP+  ou uma sequência de 4 colunas com 20PP+
        if x<27 and colunas[x]>=20 and colunas[x+1]>=20 and colunas[x+2]>=20 and colunas[x+3]>=20:
            R30b = True

        ##  R31: Até a coluna 7 tem ao menos duas colunas com 20PP+ e da coluna 13 em diante tem ao menos duas colunas com 20PP+
        if x<7 and colunas[x]>=20:
            R31a = R31a + 1
        if x>11 and colunas[x]>=20:
            R31b = R31b + 1

        ##  R35: Entre as colunas 5 e 11 tem uma sequência de 4 colunas com 20PP+ e linha 4 sempre tem 2PP+ 
        if x>3 and x<8 and colunas[x]>=20 and colunas[x+1]>=20 and colunas[x+2]>=20 and colunas[x+3]>=20 and linhas[3]>=2:
            R35 = True

        ##  R36: Até a coluna 9 tem uma sequência de 4 colunas com 20PP+
        if x<6 and colunas[x]>=20 and colunas[x+1]>=20 and colunas[x+2]>=20 and colunas[x+3]>=20:
            R36 = True

        ##  R38: Da coluna 10 em diante, tem uma sequência de 3 colunas com 15PP+
        if x>8 and x<28 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15:
            R38 = True

        ##  R39: Tem uma sequência de 4 colunas com pontos entre 5 e 9
        if x<27 and colunas[x]>=5 and colunas[x]<=9 and colunas[x+1]>=5 and colunas[x+1]<=9 and colunas[x+2]>=5 and colunas[x+2]<=9 and colunas[x+3]>=5 and colunas[x+3]<=9:
            R39 = True

        ##  R45: Tem ao menos 3 colunas seguidas com 20PP+
        if x<28 and colunas[x]>=20 and colunas[x+1]>=20 and colunas[x+2]>=20:
            R45 = True

        ##  R46: Entre as colunas 4,5,6 ... 12,13,14 ... 19,20,21,22 tem ao menos um 15PP+ em cada trecho
        if x==3 and (colunas[x]>=15 or colunas[x+1]>=15 or colunas[x+2]>=15):
            R46a = True
        if x==11 and (colunas[x]>=15 or colunas[x+1]>=15 or colunas[x+2]>=15):
            R46b = True
        if x==18 and (colunas[x]>=15 or colunas[x+1]>=15 or colunas[x+2]>=15 or colunas[x+3]>=15):
            R46c = True

        ##  R47: Entre as colunas 5 e 19 tem ao menos duas colunas com 10PP-
        if x>3 and x<19 and colunas[x]>=1 and colunas[x]<=10:
            R47 = R47 + 1

        ##  R49: Tem uma sequência de 10 colunas com 15PP+
        if x<21 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15 and colunas[x+3]>=15 and colunas[x+4]>=15 and colunas[x+5]>=15 and colunas[x+6]>=15 and colunas[x+7]>=15 and colunas[x+8]>=15 and colunas[x+9]>=15:
            R49 = True

        ##  R71: Até a 5ª coluna tem uma coluna com 20PP+
        if x<5 and colunas[x]>=20:
            R71 = True

        ## R71_ajuste:: A partir da coluna 9, tem alguma coluna com 20PP+
        if x>8 and colunas[x]>=20:
            R71_ajuste = True

        ## R72_ajuste2:: Da coluna 18 em diante, tem 3 colunas seguidas com 15PP+
        if x>16 and x<28 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15:
            R72_ajuste2 = True

        ## R72_ajuste4:: Tem 15PP+ até a coluna 6 ou a linha 21
        if x<6 and colunas[x]>=15:
            R72_ajuste4 = True

        ##  R73: Entre as colunas 11 e 14 tem ao menos 2 colunas com 20PP+
        if x>9 and x<14 and colunas[x]>=20:
            R73 = R73 + 1

        ##  R76: Até a coluna 7 tem ao menos duas colunas com 20PP+
        if x<7 and colunas[x]>=20:
            R76 = R76 + 1

        ##  R79: Sempre termina até a coluna 17 e entre as colunas 5 e 7 tem ao menos duas com 20PP+
        if x>3 and x<7 and colunas[x]>=20:
            R79b = R79b + 1

        ##  R80: Entre as colunas 12 e 15 tem uma sequência  de 3 colunas com 15PP+  e entre as linhas 15 e 20 não tem 5PP-
        if x>10 and x<13 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15:
            R80a = True

        ##  R85: Da coluna 20 em diante, tem ao menos uma coluna com 15PP+
        if x>18 and colunas[x]>=15:
            R85 = True

        ##  R91: Após a coluna 11 tem ao menos duas colunas com 15PP+
        if x>9 and colunas[x]>=15:
            R91 = R91 + 1

        ##  R92: Tem uma sequência de 4 colunas com 15PP+ e termina até a coluna 21
        if x<27 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15 and colunas[x+3]>=15 and colunas[20]<2:
            R92 = True

        ##  R93: Entre as colunas 7 e 17 tem ao menos 2 colunas com 5PP- e 1PP+
        if x>5 and x<17 and colunas[x]>=1 and colunas[x]<=5:
            R93 = R93 + 1

        ##  R94: Da coluna 11 em diante, tem alguma coluna com 15PP+
        if x>9 and colunas[x]>=15:
            R94 = True

        ##  R96: Tem duas linhas seguidas ou três colunas seguidas com 20PP+
        if x<28 and colunas[x]>=20 and colunas[x+1]>=20 and colunas[x+2]>=20:
            R96b = True

        ##  R100: Após a coluna 12 tem alguma coluna com 20PP+ ou a coluna 23 é 2PP+
        if (x>11 and colunas[x]>=20) or colunas[22]>=2:
            R100 = True

        ##  R101:  Entre as colunas 12 e 16 tem ao menos 4 colunas seguidas com 15PP+
        if x>10 and x<16 and colunas[x]>=15 and colunas[x+1]>=15 and colunas[x+2]>=15 and colunas[x+3]>=15:
            R101 = True

        ##  R102:  Tem uma sequência de 6 colunas com 4PP+ e 9PP- ou 10 linhas seguidas com esses mesmos pontos
        if x<25 and colunas[x]>=4 and colunas[x]<=9 and colunas[x+1]>=4 and colunas[x+1]<=9 and colunas[x+2]>=4 and colunas[x+2]<=9 and colunas[x+3]>=4 and colunas[x+3]<=9 and colunas[x+4]>=4 and colunas[x+4]<=9 and colunas[x+5]>=4 and colunas[x+5]<=9:
            R102 = True

    
    resultado=identify(R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R10a, R11, R12a, R12b, R12c, R12d, R12_ajuste, R13, R14a, R14c, R14b, R14d, R15, R16a, R16b, R16_ajusteA, R16_ajusteB, R17a, R17b, R18, R19, R20, R21, R22, R23a, R23b, R23c, R24a, R24b, R25, R26b, R28, R30a, R30b, R31a, R31b, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42a, R42b, R42c,
    R43, R44, R45, R46a, R46b, R46c, R47, R48, R49, R50, R51a, R51b, R51b_aux1, R51b_aux2, R52, R53, R54, R55, R56, R57, R58, R59, R59A, R60a, R60b, R61, R62, R63, R64, R65, R66, R67, R68, R70, R71, R71_ajuste, R72, R72_ajuste, R72_ajuste2, R72_ajuste3, R72_ajuste4, R73, R74, R75, R76, R77a, R77b, R78, R79a, R79b, R80a, R80b, R81, R82, R83, R84, R85, R86, R87, R88, R89,
    R90, R91, R92, R93, R94, R95, R96a, R96b, R97, R98, R99, R100, R101, R102, R103, R104)
    return resultado

def identify(R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R10a, R11, R12a, R12b, R12c, R12d, R12_ajuste, R13, R14a, R14c, R14b, R14d, R15, R16a, R16b, R16_ajusteA, R16_ajusteB, R17a, R17b, R18, R19, R20, R21, R22, R23a, R23b, R23c, R24a, R24b, R25, R26b, R28, R30a, R30b, R31a, R31b, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42a, R42b, R42c,
    R43, R44, R45, R46a, R46b, R46c, R47, R48, R49, R50, R51a, R51b, R51b_aux1, R51b_aux2, R52, R53, R54, R55, R56, R57, R58, R59, R59A, R60a, R60b, R61, R62, R63, R64, R65, R66, R67, R68, R70, R71, R71_ajuste, R72, R72_ajuste, R72_ajuste2, R72_ajuste3, R72_ajuste4, R73, R74, R75, R76, R77a, R77b, R78, R79a, R79b, R80a, R80b, R81, R82, R83, R84, R85, R86, R87, R88, R89,
    R90, R91, R92, R93, R94, R95, R96a, R96b, R97, R98, R99, R100, R101, R102, R103, R104):

    letra = ""

    if R1==True:
        if R2==True:
            letra="G"
        else:
            if R3>=3:
                letra="P"
            else:
                if R4>=3:
                    letra="P"
                else:
                    if R5==True:
                        letra="G"
                    else:
                        if R6==True:
                            letra="Y"
                        else:
                            if R7==True:
                                letra="P"
                            else:
                                if R8>=60:
                                    letra="Y"
                                else:
                                    letra="Desconhecida"
    else:
        if R9==True:
            if R50==True:
                if R51a==True or R51b==True:
                    letra="3"
                else:
                    if R52==True:
                        letra="M"
                    else:
                        if R53>=2:
                            letra="8"
                        else:
                            if R54==True:
                                letra="F"
                            else:
                                if R55==True:
                                    letra="B"
                                else:
                                    if R56==False:
                                        letra="4"
                                    else:
                                        if R57==True:
                                            letra="5"
                                        else:
                                            if R58==True:
                                                letra="8"
                                            else:
                                                if R59>=5:
                                                    letra="B"
                                                else:
                                                    if R59A==True:
                                                        letra="6"
                                                    else:
                                                        letra="B"
            else:
                if R60a<=3 and R60b==True:
                    letra="7"
                else:
                    if R61==True:
                        letra="4"
                    else:
                        if R62==True:
                            letra="D"
                        else:
                            if R63==False:
                                letra="5"
                            else:
                                if R64==True:
                                    letra="3"
                                else:
                                    if R65==True:
                                        letra="8"
                                    else:
                                        if R66>=12 or (R66>=10 and R67>=14):
                                            letra="D"
                                        else:
                                            if R67>=14:
                                                letra="2"
                                            else:
                                                if R68<10.5:
                                                    letra="4"
                                                else:
                                                    letra="Desconhecida"
        else:
            if R10==True:
                if R10a>=21:
                    letra="W"
                else:
                    if R10a>=15 and R10a<=20:
                        letra="M"
                    else:
                        letra="Desconhecida"
            else:
                if R11==True:
                    if (R12a==True and R12b==False) or (R12c==True and R12d==False):
                        if R12_ajuste==True:
                            letra="7"
                        else:
                            letra="F"
                    else:
                        if R13==True:
                            letra="5"
                        else:
                            if (R14a==True and R14b==True) or (R14c==True and R14d==True):
                                letra="2"
                            else:
                                if R15==True:
                                    letra="4"
                                else:
                                    if R16a==True or R16b==True:
                                        if R16_ajusteA>=2:
                                            letra="7"
                                        else:
                                            if R16_ajusteB==True:
                                                letra="7"
                                            else:
                                                letra="3"
                                    else:
                                        if R17a==True or R17b==False:
                                            letra="5"
                                        else:
                                            if R18==True:
                                                letra="N"
                                            else:
                                                if R19==True:
                                                    letra="B"
                                                else:
                                                    if R20==True:
                                                        letra="C"
                                                    else:
                                                        letra="C"
                else:
                    if R21==True:
                        if R22==True:
                            letra="W"
                        else:
                            if R23a==False and R23b==True and R23c<=9 and R23c>1:
                                letra="D"
                            else:
                                if R24a>=7 and R24b==True:
                                    letra="N"
                                else:
                                    if R25==True:
                                        letra="2"
                                    else:
                                        if R24a>=3 and R26b<=9.8:
                                            letra="6"
                                        else:
                                            if R24a<=2:
                                                letra="X"
                                            else:
                                                if R28==True:
                                                    letra="5"
                                                else:
                                                    if R24a>=5:
                                                        letra="8"
                                                    else:
                                                        letra="Desconhecida"
                    else:
                        if R30a==True or R30b==True:
                            if R31a>=2 and R31b>=2:
                                if R32==True:
                                    letra="2"
                                else:
                                    if R33==True:
                                        letra="5"
                                    else:
                                        if R34==True:
                                            letra="8"
                                        else:
                                            letra="Desconhecida"
                            else:
                                if R35==True:
                                    letra="7"
                                else:
                                    if R36==True:
                                        if R37==True:
                                            letra="N"
                                        else:
                                            if R38==True:
                                                letra="E"
                                            else:
                                                if R39==True:
                                                    letra="B"
                                                else:
                                                    letra="Desconhecida"
                                    else:
                                        if R40>=2:
                                            if R41==True:
                                                letra="2"
                                            else:
                                                if R42a==True or (R42b==True and R42c==False):
                                                    letra="5"
                                                else:
                                                    if R43==True:
                                                        letra="2"
                                                    else:
                                                        letra="Desconhecida"
                                        else:
                                            if R44==True:
                                                letra="4"
                                            else:
                                                if R45==True:
                                                    letra="3"
                                                else:
                                                    letra="Desconhecida"
                        else:
                            if R46a==True and R46b==True and R46c==True:
                                if R47>=2:
                                    letra="M"
                                else:
                                    if R48==True:
                                        letra="E"
                                    else:
                                        if R49==True:
                                            letra="2"
                                        else:
                                            letra="Desconhecida"
                            else:
                                if R70==False:
                                    letra="7"
                                else:
                                    if R71==True:
                                        if R71_ajuste==True:
                                            letra="5"
                                        else:
                                            letra="B"
                                            
                                    else:
                                        if R72==True:
                                            if R72_ajuste==True:
                                                if R72_ajuste2==True:
                                                    letra="W"
                                                else:
                                                    letra="E"
                                            else:
                                                if R72_ajuste3==True:
                                                    letra="E"
                                                else:
                                                    if R72_ajuste4==True:
                                                        letra="E"
                                                    else:
                                                        letra="4"
                                                    
                                        else:
                                            if R73>=2:
                                                if R74==True:
                                                    letra="2"
                                                else:
                                                    if R75==False:
                                                        letra="X"
                                                    else:
                                                        letra="Desconhecida"
                                            else:
                                                if R76>=2:
                                                    if R77a==True and R77b==False:
                                                        letra="C"
                                                    else:
                                                        if R78==True:
                                                            letra="E"
                                                        else:
                                                            if R79a==True and R79b>=2:
                                                                letra="6"
                                                            else:
                                                                if R80a==True and R80b==False:
                                                                    letra="X"
                                                                else:
                                                                    if R81==True:
                                                                        letra="N"
                                                                    else:
                                                                        if R82==True:
                                                                            letra="B"
                                                                        else:
                                                                            if R83==True:
                                                                                letra="6"
                                                                            else:
                                                                                letra="C"
                                                else:
                                                    if R84==True:
                                                        if R85==True:
                                                            letra="W"
                                                        else:
                                                            if R86==True:
                                                                letra="E"
                                                            else:
                                                                if R87==True:
                                                                    letra="E"
                                                                else:
                                                                    if R88==True:
                                                                        letra="W"
                                                                    else:
                                                                        letra="Desconhecida"
                                                    else:
                                                        if R89==False:
                                                            if R90==True:
                                                                letra="N"
                                                            else:
                                                                if R91>=2:
                                                                    letra="2"
                                                                else:
                                                                    if R92==True:
                                                                        letra="C"
                                                                    else:
                                                                        letra="Desconhecida"
                                                        else:
                                                            if R93>=2:
                                                                if R94==True:
                                                                    letra="N"
                                                                else:
                                                                    if R95==True:
                                                                        letra="C"
                                                                    else:
                                                                        letra="Desconhecida"
                                                            else:
                                                                if R96a==True or R96b==True:
                                                                    letra="E"
                                                                else:
                                                                    if R97==True:
                                                                        letra="C"
                                                                    else:
                                                                        if R98==True:
                                                                            letra="N"
                                                                        else:
                                                                            if R99==True:
                                                                                letra="6"
                                                                            else:
                                                                                if R100==True:
                                                                                    letra="X"
                                                                                else:
                                                                                    if R101==True:
                                                                                        letra="X"
                                                                                    else:
                                                                                        if R102==True:
                                                                                            letra="C"
                                                                                        else:
                                                                                            if R103==True:
                                                                                                letra="X"
                                                                                            else:
                                                                                                if R104>=7:
                                                                                                    letra="X"
                                                                                                else:
                                                                                                    letra="C"
            
    return letra
