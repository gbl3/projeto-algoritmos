class Palavra:
    def __init__(self,termo="",peso=-1):
        self.termo = termo
        self.peso = peso

    #TODO: implemente
    def __lt__(self,other):
        return self.termo < other.termo

    def __str__(self):
        return "{0}, {1}".format(self.termo,self.peso)

    def __repr__(self):
        return self.__str__()

#TODO: implemente
def comparaPorPrefixo(palavra, prefixo):
    tamanho_prefixo = len(prefixo)
    if palavra.termo.lower()[0:tamanho_prefixo] == prefixo.lower():
        return 0
    elif palavra.termo.lower()[0:tamanho_prefixo] > prefixo.lower():
        return 1
    else:
        return -1

#TODO: implemente
def comparaPorPeso(palavra1, palavra2):
    if int(palavra1.peso) > int(palavra2.peso):
        return 1
    elif int(palavra1.peso) < int(palavra2.peso):
        return -1
    else:
        return 0
