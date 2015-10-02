numero = "26111210975119000133550010000010001000010001"
nf = numero[25:34:1]
nf = str(int(nf))
tamanho = len(nf)
teste = numero[0:35-tamanho-1:1]+numero[34-tamanho:34:1]+numero[34:]
if teste == numero:
    print "ok"

print numero
print numero[0:25:]+numero[25:34:]+numero[34::]
