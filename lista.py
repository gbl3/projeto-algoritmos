class No:
    def __init__(self,item=None,ant=None,prox=None):
        self.item = item
        self.ant = ant
        self.prox = prox
    
class Lista:

    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanho = 0
    
    def size(self):
        return self.tamanho
    
    #TODO: implemente
    def inserirOrdenado(self, item, cmp): 
        if self.tamanho == 0:
            node = No(item)
            self.primeiro = self.ultimo = node
            self.tamanho += 1
        else:
            if cmp(item , self.primeiro.item) > 0:
                node = No(item)
                node.prox = self.primeiro
                self.primeiro.ant = node
                self.primeiro = node
                self.tamanho +=1

            elif cmp(item , self.ultimo.item) < 0:
                node = No(item)
                node.ant = self.ultimo
                self.ultimo.prox = node
                self.ultimo = node
                self.tamanho +=1
            else:
                node = No(item)
                ante = self.primeiro
                atual = self.primeiro.prox
                while atual != None and cmp(node.item , atual.item) < 0:
                    ante = atual
                    atual = atual.prox
                node.ant = ante
                ante.prox = node

                if atual != None:
                    node.prox = atual
                    atual.ant = node
                ante.prox = node
                node.ant = ante
                self.tamanho += 1


        '''
        Insere ordenado conforme funcao de comparacao passada como parametro.
        cmp: funcao de comparacao que retorna <0, 0 ou >0 se primeiro valor
            for menor, igual ou maior que o segundo valor 
        '''
    
    #TODO: implemente    
    def ultimo_item(self):
        if self.ultimo != None:
            return (self.ultimo.item.peso)
    def removerFim(self):
        
        if self.tamanho == 1:
            self.primeiro = self.ultimo = No()
        else:
            auxiliar = self.ultimo.ant
            if auxiliar != None:
                auxiliar.prox = None
            self.ultimo.ant = None
            self.ultimo = auxiliar
        self.tamanho -= 1
    
    #TODO: implemente        
    def __str__(self):
        if self.primeiro == None:
            return ""
        else:
            actual = self.primeiro
            termos = ""
            while actual != None:
                termos += actual.item.termo +"\n"
                actual = actual.prox

            return termos
                
    def __repr__(self):
        return str(self)
