from mainwindow import Ui_MainWindow
from controle import Controle
from controle_list import ControleList
class GUI(Ui_MainWindow):
    def __init__(self):
        self.controle = Controle()
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.inputFileText.textChanged.connect(self.inputFileChanged)
        self.botaoOK.clicked.connect(self.carregarDados)
        self.qtdPalavraText.textChanged.connect(self.autocompletar)
        self.palavraText.textChanged.connect(self.autocompletar)
        self.palavraText.textChanged.connect(self.searchFieldChanged)
        self.TrieButton.clicked.connect(self.mudaEstrutura)
        self.ListButton.clicked.connect(self.mudaEstrutura)
    def inputFileChanged(self):
        self.botaoOK.setEnabled(self.inputFileText.text().strip() != "")
    def searchFieldChanged(self):
        if self.palavraText.text().strip() == "":
            if self.TrieButton.isChecked():
                self.ListButton.setEnabled(True)
            elif self.ListButton.isChecked():
                self.TrieButton.setEnabled(True)
        else:
            self.showTime(self.controle.tempo())
            if self.TrieButton.isChecked():
                self.ListButton.setDisabled(self.palavraText.text().strip() != "")
            elif self.ListButton.isChecked():
                self.TrieButton.setDisabled(self.palavraText.text().strip() != "")
    def mudaEstrutura(self):
        if self.TrieButton.isChecked():
            print("Trie")
            self.outputText.clear()
            #self.controle = ControleTrie()
            #mudar controle para Controle da Trie
        elif self.ListButton.isChecked():
            controle = ControleList()
            self.outputText.clear()
    def carregarDados(self):
        self.controle.carregarDados(self.inputFileText.text())
        if self.TrieButton.isChecked() or self.ListButton.isChecked():
            self.palavraText.setEnabled(True)
        else:
            self.outputText.setText("Selecione uma das duas estruturas.")
    def showTime(self,tempo):
        self.ExibeTempo.display(tempo)
    def autocompletar(self):
        texto = self.palavraText.text()
        qtd = self.qtdPalavraText.text()
        if texto != "" and qtd != "":
            lista = self.controle.find(texto,int(qtd))
            self.outputText.setText(str(lista))
        else:
            self.outputText.clear()
