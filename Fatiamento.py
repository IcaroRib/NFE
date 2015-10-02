#!/usr/bin/python
# coding=utf-8
import os, sys
from PIL import Image

def separaDuasLetras(inicio,fim,imagem):
    meio = (fim+inicio)/2
    corte=0
    marcacao=100
    for x in range (meio-7,meio+7):
        somaPretos = 0
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))
            if b == 0:
                somaPretos +=1
        if somaPretos < marcacao:
            marcacao = somaPretos
            corte = x
    return corte,corte+1

def separaTresLetras(inicio,fim,imagem):
    meio = (fim+inicio)/2
    referencia1 = meio-((meio-inicio)/2)
    referencia2 = meio+((fim-meio)/2)
    corte1=0
    corte2=0
    marcacao1=100
    marcacao2=100
    for x in range (referencia1-7,referencia1+7):
        somaPretos = 0
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))
            if b == 0:
                somaPretos +=1
        if somaPretos < marcacao1:
            marcacao1 = somaPretos
            corte1 = x
    for x in range (referencia2-7,referencia2+7):
        somaPretos = 0
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))
            if b == 0:
                somaPretos +=1
        if somaPretos < marcacao2:
            marcacao2 = somaPretos
            corte2 = x
    return corte1,corte1+1,corte2,corte2+1

def separaQuatroLetras(inicio,fim,imagem):
    meio = (fim+inicio)/2
    corte=0
    marcacao=100
    for x in range (meio-7,meio+7):
        somaPretos = 0
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))
            if b == 0:
                somaPretos +=1
        if somaPretos < marcacao:
            marcacao = somaPretos
            corte = x
    P4=corte
    P5=corte+1
    P2,P3 = separaDuasLetras(0,P4,imagem)
    P6,P7 = separaDuasLetras(P5,fim,imagem)
    return P2,P3,P4,P5,P6,P7

def encontraIntervalos(imagem):

    tamanho = imagem.size[0]
    ajuste = tamanho/10

    intervalo1 = (tamanho/4 - ajuste, tamanho/4 + ajuste)
    intervalo2 = (tamanho/2 - ajuste, tamanho/2 + ajuste)
    intervalo3 = (tamanho/2 + tamanho/4 - ajuste, tamanho/2 + tamanho/4 +ajuste)

    dados = []
    intervalos = [0]
    listaBrancos1 = []
    for x in range (intervalo1[0],intervalo1[1]):
        somaPretos = 0
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))
            if b <= 10:
                somaPretos +=1
        if somaPretos < 2:
            listaBrancos1.append(x)

    if (len(listaBrancos1) > 0):
        intervalos.append(listaBrancos1[len(listaBrancos1)/2])

    listaBrancos2 = []
    for x in range (intervalo2[0],intervalo2[1]):
        somaPretos = 0
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))
            if b == 0:
                somaPretos +=1

        if somaPretos < 2:
            listaBrancos2.append(x)

    if (len(listaBrancos2) > 0):
        intervalos.append(listaBrancos2[len(listaBrancos2)/2])

    listaBrancos3 = []
    for x in range (intervalo3[0],intervalo3[1]):
        somaPretos = 0
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))
            if b == 0:
                somaPretos +=1
        if somaPretos < 2:
            listaBrancos3.append(x)

    if (len(listaBrancos3) > 0):            
        intervalos.append(listaBrancos3[len(listaBrancos3)/2])
    
    intervalos.append(tamanho)
    
    dados.append(intervalos)
    dados.append(listaBrancos1)
    dados.append(listaBrancos2)
    dados.append(listaBrancos3)
    dados.append(tamanho)
    
    return dados


def encontraPontos(imagem,intervalos,listaBrancos1,listaBrancos2,listaBrancos3,tamanho):

    ##Quando estiverem selecionados 5 pontos
    if len(intervalos) == 5:
        P1 = 0
        P2 = listaBrancos1[0]-1
        P3 = listaBrancos1[-1]+1
        P4 = listaBrancos2[0]-1
        P5 = listaBrancos2[-1]+1
        P6 = listaBrancos3[0]-1
        P7 = listaBrancos3[-1]+1
        P8 = tamanho

    ##Quando estiverem selecionados 4 pontos
    if len(intervalos) == 4:
        P1 = 0
        if len(listaBrancos1)==0:
            P2,P3 = separaDuasLetras(0,listaBrancos2[0]-1,imagem)
            P4 = listaBrancos2[0]-1
            P5 = listaBrancos2[-1]+1
            P6 = listaBrancos3[0]-1
            P7 = listaBrancos3[-1]+1
        if len(listaBrancos2)==0:
            P2 = listaBrancos1[0]-1
            P3 = listaBrancos1[-1]+1
            P4,P5 = separaDuasLetras(listaBrancos1[-1]+1,listaBrancos3[0]-1,imagem)
            P6 = listaBrancos3[0]-1
            P7 = listaBrancos3[-1]+1
        if len(listaBrancos3)==0:
            P2 = listaBrancos1[0]-1
            P3 = listaBrancos1[-1]+1
            P4 = listaBrancos2[0]-1
            P5 = listaBrancos2[-1]+1
            P6,P7 = separaDuasLetras(listaBrancos2[-1]+1,tamanho,imagem)
        P8 = tamanho

    ##Quando estiverem selecionados 3 pontos
    if len(intervalos) == 3:
        P1 = 0
        if len(listaBrancos1)!=0:
            P2 = listaBrancos1[0]-1
            P3 = listaBrancos1[-1]+1
            P4,P5,P6,P7 = separaTresLetras(listaBrancos1[-1]+1,tamanho,imagem)
        if len(listaBrancos3)!=0:
            P2,P3,P4,P5 = separaTresLetras(0,listaBrancos3[0]-1,imagem)
            P6 = listaBrancos3[0]-1
            P7 = listaBrancos3[-1]+1
        if len(listaBrancos2)!=0:
            P2,P3 = separaDuasLetras(0,listaBrancos2[0]-1,imagem)
            P4 = listaBrancos2[0]-1
            P5 = listaBrancos2[-1]+1
            P6,P7 = separaDuasLetras(listaBrancos2[-1]+1,tamanho,imagem)
        P8 = tamanho

    ##Quando estiverem selecionados 2 pontos    
    if len(intervalos) == 2:
        P1 = 0
        P2,P3,P4,P5,P6,P7 = separaQuatroLetras(0,tamanho,imagem)
        P8 = tamanho

    pontos = []
    pontos.append(P1)
    pontos.append(P2)
    pontos.append(P3)
    pontos.append(P4)
    pontos.append(P5)
    pontos.append(P6)
    pontos.append(P7)
    pontos.append(P8)

    return pontos

def fatiamento(imagem,inicioCaracter,fimCaracter):
    largura = fimCaracter-inicioCaracter
    caracter = Image.new("RGB",(largura,39))
    for x in range(inicioCaracter,fimCaracter):
        for y in range(0,39):
            r,g,b = imagem.getpixel((x,y))                        
            caracter.putpixel((x-inicioCaracter,y),(r,g,b))

    w = caracter.size[0]
    caracterAjustado = Image.new("RGB",(30,39))
    for x in range(30):
        for y in range(39):
            if x<w:
                r,g,b = caracter.getpixel((x,y))
                caracterAjustado.putpixel((x,y),(r,g,b))
            else:
                caracterAjustado.putpixel((x,y),(255,255,255))
    return caracterAjustado
