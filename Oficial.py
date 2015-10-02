#!/usr/bin/python
# coding=utf-8
import time
import os, sys
from PIL import Image
from pytesser import *
from Cores import *
from Fatiamento import *
from Analise import *
from Parametros import *

def resolve_captcha(image):

    alfabeto    = ['2','3','4','5','6','7','8','b','c','d','e','f','g','m','n','p','w','x','y']
    
    try:
        w,h = image.size
        captchaEncontrado = False
        
        tratada = removeCores(image,w,h)
        imagem  = redimensionamento(tratada,w,h)

        dados = encontraIntervalos(imagem)
        intervalos      = dados[0]
        listaBrancos1   = dados[1]
        listaBrancos2   = dados[2]
        listaBrancos3   = dados[3]
        tamanho         = dados[4]
        
        pontos  = encontraPontos(imagem,intervalos,listaBrancos1,listaBrancos2,listaBrancos3,tamanho)

        c1 = fatiamento(imagem,pontos[0],pontos[1])
        c2 = fatiamento(imagem,pontos[2],pontos[3])
        c3 = fatiamento(imagem,pontos[4],pontos[5])
        c4 = fatiamento(imagem,pontos[6],pontos[7])

        #------------------------------------------------------------------------------------

        #Fourier
        opcoes1 = fourier(c1)
        opcoes2 = fourier(c2)
        opcoes3 = fourier(c3)
        opcoes4 = fourier(c4)
        
        #OCR Individual
        ocr1 = image_to_string(c1).rstrip().lower()
        ocr2 = image_to_string(c2).rstrip().lower()
        ocr3 = image_to_string(c3).rstrip().lower()
        ocr4 = image_to_string(c4).rstrip().lower()
        tamanho1=len(ocr1)
        tamanho2=len(ocr2)
        tamanho3=len(ocr3)
        tamanho4=len(ocr4)
        if tamanho1==1:
            ocr1 = conversao(ocr1[0])
        if tamanho2==1:
            ocr2 = conversao(ocr2[0])
        if tamanho3==1:
            ocr3 = conversao(ocr3[0])
        if tamanho4==1:
            ocr4 = conversao(ocr4[0])

        #OCR Total
        conteudo = image_to_string(imagem).rstrip().lower()
        tamanho=len(conteudo)

        t1=""
        t2=""
        t3=""
        t4=""
        
        if tamanho==4 :
            t1 = conversao(conteudo[0])
            t2 = conversao(conteudo[1])
            t3 = conversao(conteudo[2])
            t4 = conversao(conteudo[3])

        #Heuristicas
        letra1=mapeamento(c1).lower()
        letra2=mapeamento(c2).lower()
        letra3=mapeamento(c3).lower()
        letra4=mapeamento(c4).lower()

        #------------------------------------------------------------------------------------

        caracter1=""
        caracter2=""
        caracter3=""
        caracter4=""

        #------------------------------------------------------------------------------------

        #Heuristicas + OCR + Fourier
        if letra1==ocr1 and letra1 in opcoes1:
            caracter1=letra1
        if letra2==ocr2 and letra2 in opcoes2:
            caracter2=letra2
        if letra3==ocr3 and letra3 in opcoes3:
            caracter3=letra3
        if letra4==ocr4 and letra4 in opcoes4:
            caracter4=letra4

        #Heuristicas + OCR Individual
        if letra1==ocr1 and caracter1=="":
            caracter1=letra1
        if letra2==ocr2 and caracter2=="":
            caracter2=letra2
        if letra3==ocr3 and caracter3=="":
            caracter3=letra3
        if letra4==ocr4 and caracter4=="":
            caracter4=letra4

        #Heuristicas + OCR Total
        if letra1==t1 and caracter1=="":
            caracter1=letra1
        if letra2==t2 and caracter2=="":
            caracter2=letra2
        if letra3==t3 and caracter3=="":
            caracter3=letra3
        if letra4==t4 and caracter4=="":
            caracter4=letra4

        #OCR Total + Fourier
        if len(t1)==1 and t1 in alfabeto and t1 in opcoes1 and caracter1=="":
            caracter1=t1
        if len(t2)==1 and t2 in alfabeto and t2 in opcoes2 and caracter2=="":
            caracter2=t2
        if len(t3)==1 and t3 in alfabeto and t3 in opcoes3 and caracter3=="":
            caracter3=t3
        if len(t4)==1 and t4 in alfabeto and t4 in opcoes4 and caracter4=="":
            caracter4=t4

        #Heuristicas + Fourier
        if letra1 in opcoes1 and caracter1=="":
            caracter1=letra1
        if letra2 in opcoes2 and caracter2=="":
            caracter2=letra2
        if letra3 in opcoes3 and caracter3=="":
            caracter3=letra3
        if letra4 in opcoes4 and caracter4=="":
            caracter4=letra4

        #OCR Total
        if len(t1)==1 and t1 in alfabeto and caracter1=="":
            caracter1=t1
        if len(t2)==1 and t2 in alfabeto and caracter2=="":
            caracter2=t2
        if len(t3)==1 and t3 in alfabeto and caracter3=="":
            caracter3=t3
        if len(t4)==1 and t4 in alfabeto and caracter4=="":
            caracter4=t4

        #OCR nas partes
        if len(ocr1)==1 and ocr1 in alfabeto and caracter1=="":
            caracter1=ocr1
        if len(ocr2)==1 and ocr2 in alfabeto and caracter2=="":
            caracter2=ocr2
        if len(ocr3)==1 and ocr3 in alfabeto and caracter3=="":
            caracter3=ocr3
        if len(ocr4)==1 and ocr4 in alfabeto and caracter4=="":
            caracter4=ocr4

        #Heuristica
        if letra1!="desconhecida" and caracter1=="":
            caracter1=letra1
        if letra2!="desconhecida" and caracter2=="":
            caracter2=letra2
        if letra3!="desconhecida" and caracter3=="":
            caracter3=letra3
        if letra4!="desconhecida" and caracter4=="":
            caracter4=letra4

        #------------------------------------------------------------------------------------

        if caracter1=="":
            caracter1="n"
        if caracter2=="":
            caracter2="n"
        if caracter3=="":
            caracter3="n"
        if caracter4=="":
            caracter4="n"


        captcha = caracter1+caracter2+caracter3+caracter4
        return captcha
        

            
    except Exception:
        captcha = "nada"
        return captcha
    
