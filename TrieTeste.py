class No():
    def __init__(self,valor=None,filho=None,esquerda=None,direita=None,peso=None):
        self.valor= valor
        self.filho= filho
        self.esquerda = esquerda
        self.direita = direita
        self.peso=peso
class TrieTernaria():
    def __init__(self):
        self.raiz = No()
        self.lista = []
        
        
    def adcionar(self,palavra,tupla,auxiliar):
        contador = 0
        for x in palavra:
            auxiliar.valor = x
            auxiliar.peso = None
            if contador == len(palavra) - 1:
                auxiliar.peso = tupla
            auxiliar.filho = No()
            auxiliar = auxiliar.filho
            
            
            contador += 1
    def inserir(self,palavra,tupla,auxiliar=None,bandeira=0):
        if self.raiz.valor == None:
            auxiliar = No()
            self.raiz = No(palavra[0])
            self.raiz.peso = None
            self.raiz.filho = auxiliar
            palavra = palavra[1:len(palavra)]
            self.adcionar(palavra,tupla,auxiliar)
        elif bandeira ==0:
            bandeira=1
            auxiliar = self.raiz
            self.inserir(palavra,tupla,auxiliar,bandeira)
        else:
            if palavra[0] < auxiliar.valor:
                if auxiliar.esquerda==None:
                    auxiliar.esquerda = No()
                    auxiliar = auxiliar.esquerda
                    self.adcionar(palavra,tupla,auxiliar)
                
                else:
                    auxiliar = auxiliar.esquerda
                    self.inserir(palavra,tupla,auxiliar,bandeira)
            elif palavra[0] > auxiliar.valor:
                if auxiliar.direita==None:
                    auxiliar.direita = No()
                    auxiliar = auxiliar.direita
                    self.adcionar(palavra,tupla,auxiliar)
                else:
                    auxiliar = auxiliar.direita
                    self.inserir(palavra,tupla,auxiliar,bandeira)
            elif palavra[0] == auxiliar.valor:
                palavra = palavra[1:len(palavra)]
                if palavra == "":
                    auxiliar.peso = tupla
                    
                elif auxiliar.filho.valor !=None:
                    auxiliar = auxiliar.filho
                    self.inserir(palavra,tupla,auxiliar,bandeira)
                else:
                    auxiliar = auxiliar.filho
                    self.adcionar(palavra,tupla,auxiliar)
                    
                    



    def find(self,prefixo):
        nod = self.__find(self.raiz,prefixo,0)
        self.lista = []
        if nod == None:
            return ""
        return self.buscador(nod.filho,prefixo,self.lista)
    def __find(self,no,prefixo,c):
        letra = prefixo[c]
        if no == None:
            return None
        if letra < no.valor:
            return self.__find(no.esquerda,prefixo,c)
        elif letra > no.valor:
            return self.__find(no.direita,prefixo,c)
        elif c < len(prefixo)-1:
            return self.__find(no.filho,prefixo,c+1)
        else:
            return no


    def buscador(self,caminho,prefixo,lista):
        if caminho == None:
            return None
        if caminho.peso:
            self.lista.append((int(caminho.peso[1]),caminho.peso[0]))
        if caminho.esquerda:
            self.buscador(caminho.esquerda,prefixo,self.lista)
        if caminho.direita:
            self.buscador(caminho.direita,prefixo,self.lista)
        if caminho.filho:
            self.buscador(caminho.filho,prefixo,self.lista)
 
      
