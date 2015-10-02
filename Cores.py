#!/usr/bin/python
# coding=utf-8
import os, sys
from PIL import Image

def removeCores(im,w,h):
    
    imnova = Image.new("RGB",(w,h))
    imnovas = Image.new("RGB",(w,h))

    for x in range(w):
        for y in range(h):
            r,g,b = im.getpixel((x,y))

            #Tornando azul em preto
            if b>200 and r<20 and g<20:
                r=0
                g=0
                b=0

            #Tornando azul escuro em preto
            if r<55 and g<55 and b>84:
                r=0
                g=0
                b=0

            #Tornando do cinza claro em branco
            if r==g and g==b and r>195:
                r=255
                g=255
                b=255

            #Tornando azul escuro em preto
            if r<91 and g<91 and b>150:
                r=0
                g=0
                b=0

            if b>180 and r>180 and g>180:
                r=255
                g=255
                b=255

            if b<125 and r>180 and g>180:
                r=255
                g=255
                b=255

            #Ajuste da linha que passa por cima das letras
            if b>150 and r<150 and g<150:
                r=0
                g=0
                b=0
                
            #Tornando o que não for preto em branco
            if r!=0 and g!=0 and b!=0:
                r=255
                g=255
                b=255

            imnova.putpixel((x,y),(r,g,b))
            imnovas.putpixel((x,y),(r,g,b))

    
    # Limpeza de pontos isolados e tornar em preto pontos que deveriam ser pontos pretos(PP)        
    for x in range(w):
        for y in range(h):
            soma=0
            if x>0 and y>0 and x<w-1 and y<h-1:
                r,g,b = imnova.getpixel((x,y))
                r1,b1,g1 = imnova.getpixel((x-1,y-1))
                r2,b2,g2 = imnova.getpixel((x-1,y))
                r3,b3,g3 = imnova.getpixel((x-1,y+1))
                r4,b4,g4 = imnova.getpixel((x,y-1))
                r5,b5,g5 = imnova.getpixel((x,y+1))
                r6,b6,g6 = imnova.getpixel((x+1,y-1))
                r7,b7,g7 = imnova.getpixel((x+1,y))
                r8,b8,g8 = imnova.getpixel((x+1,y+1))
                if b1==0: soma+=1
                if b2==0: soma+=1
                if b3==0: soma+=1
                if b4==0: soma+=1
                if b5==0: soma+=1
                if b6==0: soma+=1
                if b7==0: soma+=1
                if b8==0: soma+=1
                if soma<4:
                    imnovas.putpixel((x,y),(255,255,255))
                if soma>5:
                    imnovas.putpixel((x,y),(0,0,0))

    return imnovas


def redimensionamento(imnovas,w,h):

    inicio=0
    fim = 0
    inicioEncontrado = False
    fimEncontrado = False
    contagem=[]
    for x in range(w):
        soma = 0
        for y in range(h):
            r,g,b = imnovas.getpixel((x,y))
            if b==0:
                soma = soma +1

        if x<40 and soma!=0 and inicioEncontrado==False:
            inicio=x
            inicioEncontrado=True
        if x>112 and soma==0 and fimEncontrado==False:
            soma2 = 0 
            for a in range(x,140):
                for y in range(h):
                    r1,g1,b1 = imnovas.getpixel((a,y))
                    if b1==0:
                        soma2 = soma2 +1
            if soma2==0:
                fim = x-1
                fimEncontrado = True
        contagem.append(soma)

    largura = fim-inicio
    imnova2 = Image.new("RGB",(largura,h))
    for x in range(inicio,fim):
        for y in range(h):
            r,g,b = imnovas.getpixel((x,y))
            imnova2.putpixel((x-inicio,y),(r,g,b))

    lar,alt = imnova2.size
    cima = 10
    baixo = 49

    altura = baixo-cima
    imnova3 = Image.new("RGB",(largura,altura))
    for x in range(largura):
        for y in range(cima,baixo):
            r,g,b = imnova2.getpixel((x,y))
            imnova3.putpixel((x,y-cima),(r,g,b))

    return imnova3
