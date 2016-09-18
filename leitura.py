
f = open("auxiliar.txt", "r")
lista = f.readlines()
lista_aux = []
lista_palavras = []
a = 0
for x in lista:
    a += 1
    if a > 1:
        
        tupla = x.split()
        palavra = Palavra(tupla[1],tupla[0])
       listwa.add(0  lista_palavras.append(tupla[1])
        
'''
for x in lista:
    x.split()
print(lista[2].split())
'''
f.close()
