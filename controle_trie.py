from palavra import Palavra
from TrieTeste import TrieTernaria
from controle import Controle
import time

class ControleTrie(Controle):
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
    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()

        #TODO: seu codigo aqui
        consultas = open(filename,"r")
        self.trie = TrieTernaria()
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
                self.trie.inserir(palavra.termo,(palavra.termo,palavra.peso))
                self.numeroTermos += 1

            aux_pulo = 1

        self.dadosCarregados = True

    def find(self, prefixo, qtd):
        self.tempoinicial = time.clock()
        self.trie.find(prefixo)
        self.termos = self.trie.lista
        self.termos.sort(reverse = True)
        palavras = ""
        for x in range(0,qtd):
            if x < len(self.termos):
                palavras += self.termos[x][1]+"\n"
        return palavras
