#!/usr/bin/python
# coding=utf-8
import math, operator
import os, sys
from PIL import Image


def compare(file1,file2):
    h1 = file1.histogram()
    h2 = file2.histogram()
    
    #rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    #rms = math.sqrt(sum((a-b)**2 for a,b in zip(h1, h2))/len(h1))
    diff_squares = [(h1[i] - h2[i])**2 for i in xrange(len(h1))];
    rms = math.sqrt(sum(diff_squares) / len(h1));
    return rms

def pegaMaior(contador,opcoes,alfabeto):
    maior = 0
    indice = 0
    for a in range (len(contador)):
        if maior < contador[a]:
            maior = contador[a]
            indice = a
    opcoes.append(alfabeto[indice])
    alfabeto.pop(indice)
    contador.pop(indice)

def fourier(imagem):
    contador    = []
    opcoes      = []
    parcial     = 0
    indice      = 0
    menor       = 100
    alfabeto    = ['2','3','4','5','6','7','8','b','c','d','e','f','g','m','n','p','w','x','y']

    endereco = './Base_Estatistica/'
    for carac in os.listdir(endereco):
        parcial = 0
        for img in os.listdir(endereco+carac):
            extensao = img[-3]+img[-2]+img[-1]
            if extensao=="png":
                im = Image.open(endereco+carac+"/"+img)
                resultado = compare(imagem,im)
                if resultado<=1:
                    parcial+=1
        contador.append(parcial)
    pegaMaior(contador,opcoes,alfabeto)
    pegaMaior(contador,opcoes,alfabeto)
    pegaMaior(contador,opcoes,alfabeto)
    pegaMaior(contador,opcoes,alfabeto)
    pegaMaior(contador,opcoes,alfabeto)

    return opcoes

def conversao(caracter):
    if caracter=="h":
        caracter="n"
    if caracter=="q":
        caracter="g"
    if caracter=="?":
        caracter="7"
    if caracter=="z":
        caracter="2"
    
    return caracter
    
