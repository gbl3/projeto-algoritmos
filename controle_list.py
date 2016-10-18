from palavra import *
from lista import Lista
from controle import Controle
import time

class ControleList(Controle):
    def __init__(self):
        self.numeroTermos = 0
        self.termos = list()
        self.dadosCarregados = True
        self.tempoinicial = time.clock()
    def tempo(self):
        self.cronometro = time.clock() - self.tempoinicial
        return self.cronometro

    def __apagarTermos(self):
        self.termos = []
        self.numeroTermos = 0
        self.dadosCarregados = False

    #TODO: implemente
    def __firstIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1
        pos = -1
        #TODO: seu codigo aqui
        meio = (fim+1) // 2
        lista_aux = self.termos[inicio:fim+1]
        while True:
            if comparaPorPrefixo(lista_aux[meio],prefixo) == 0:
                if meio - 1 != -1 :
                    while comparaPorPrefixo(lista_aux[meio - 1],prefixo) == 0:
                        meio = meio - 1
                        if meio == 0:
                            break
                primeiro_valor_correspondente = lista_aux[meio]
                pos = self.termos.index(primeiro_valor_correspondente)
                break
            elif (meio == 1 and fim == 2) or (meio == 0 and fim == 1):
                break
            elif comparaPorPrefixo(lista_aux[meio],prefixo) > 0:
                lista_aux = lista_aux[0:meio]
                fim = len(lista_aux)
                meio = (fim // 2)
            else:
                lista_aux = lista_aux[meio:fim+1]
                fim = len(lista_aux)
                meio = fim // 2


        return pos

    #TODO: implemente
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1
        pos = -1

        #TODO: seu codigo aqui

        meio = (fim+1) // 2
        lista_aux = self.termos[inicio:fim+1]
        while True:
            if comparaPorPrefixo(lista_aux[meio],prefixo) == 0:
                if meio + 1 != len(lista_aux):
                    while comparaPorPrefixo(lista_aux[meio + 1],prefixo) == 0:
                        meio = meio + 1
                        if meio == len(lista_aux) - 1:
                            break
                ultimo_valor_correspondente = lista_aux[meio]
                pos = self.termos.index(ultimo_valor_correspondente)
                break
            elif (meio == 1 and fim == 2) or (meio == 0 and fim == 1):
                break
            elif comparaPorPrefixo(lista_aux[meio],prefixo) > 0:
                lista_aux = lista_aux[0:meio]
                fim = len(lista_aux)
                meio = (fim // 2)
            else:
                lista_aux = lista_aux[meio:fim+1]
                fim = len(lista_aux)
                meio = fim // 2

        return pos

    #TODO: implemente
    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()

        #TODO: seu codigo aqui
        consultas = open(filename,"r")
        linhas = consultas.readlines()
        aux_pulo = 0
        for line in linhas:
            if aux_pulo > 0:
                linha = line.split("\t")
                linha_aux = linha[0].replace(" ","")
                linha_aux2 = linha[1].replace("\n","")
                linha[0] = linha_aux
                linha[1] = linha_aux2
                palavra = Palavra(linha[1],linha[0])
                self.termos.append(palavra)
                self.numeroTermos += 1

            aux_pulo = 1

        self.termos.sort()
        self.dadosCarregados = True

    #TODO: implemente
    def find(self, prefixo, qtd):
        self.tempoinicial = time.clock()
        self.inicio = self._Controle__firstIndexOf(prefixo)
        self.fim = self._Controle__lastIndexOf(prefixo)
        lista = Lista()
        erro = False
        for x in range(self.inicio,self.fim + 1):
            if self.inicio and self.fim == - 1:
                erro = True
                break
            if lista.size()  >= qtd :
                ultimo = lista.ultimo_item()
                if ultimo != None:
                    if ultimo < self.termos[x].peso:
                        lista.removerFim()
                        lista.inserirOrdenado(self.termos[x],comparaPorPeso)
            else:
                lista.inserirOrdenado(self.termos[x],comparaPorPeso)
        if erro:
            return ""
        else:
            return lista
