from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QLabel,

)
from gerenciaPessoa import Gerenciapessoa
from pessoa import Pessoa

app = QApplication([])

class Widget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(300, 300)
        self.setContentsMargins(200, 200, 200, 200)
        
        self.cabeNome = QLabel(self)
        self.cabeNome.setText("Nome:")
        self.cabeNome.move(50, 50)
        self.caixaNome = QLineEdit(self)
        self.caixaNome.move(50, 75) 

        self.cabeIdade = QLabel(self)
        self.cabeIdade.setText("Idade:")
        self.cabeIdade.move(50, 110)
        self.caixaIdade = QLineEdit(self)
        self.caixaIdade.move(50, 135)

        self.cabeEmail = QLabel(self)
        self.cabeEmail.setText("E-mail:")
        self.cabeEmail.move(50, 170)
        self.caixaEmail = QLineEdit(self)
        self.caixaEmail.move(50, 195)

        self.armazenaDados = QPushButton("Armazenar dados", self)
        self.armazenaDados.move(50, 230)

        self.botaoImprimir = QPushButton("Imprimir dados", self)
        self.botaoImprimir.move(200, 125)

        self.caixaImpressao = QLabel(self)
        self.caixaImpressao.move(300, 125)

        self.botaoTelaRemover = QPushButton("Remover/Editar pessoa", self)
        self.botaoTelaRemover.move(500, 125)

        self.caixaRemover = QLineEdit(self)
        self.caixaRemover.move(150, 150)
        self.caixaRemover.hide()

        self.textoCaixaRemover = QLabel(self)
        self.textoCaixaRemover.setText("Digite o nome de cadastro para remover/editar")
        self.textoCaixaRemover.adjustSize()
        self.textoCaixaRemover.move(150, 100)
        self.textoCaixaRemover.hide()

        self.botaoConfirmaRemocao = QPushButton("Remover", self)
        self.botaoConfirmaRemocao.move(150, 200)
        self.botaoConfirmaRemocao.hide()

        self.botaoRetornarTelaInicio = QPushButton("Retornar", self)
        self.botaoRetornarTelaInicio.move(50, 400)
        self.botaoRetornarTelaInicio.hide()

        self.botaoEditar = QPushButton("Editar", self)
        self.botaoEditar.move(50, 300)
        self.botaoEditar.hide()

        self.botaoSalvaEdit = QPushButton("Salvar", self)
        self.botaoSalvaEdit.move(50, 300)
        self.botaoSalvaEdit.hide()

        self.armazenaDados.clicked.connect(self.adicionaPessoa)
        self.botaoImprimir.clicked.connect(self.imprimeDados)
        self.botaoTelaRemover.clicked.connect(self.trocaTelaRemover)
        self.botaoRetornarTelaInicio.clicked.connect(self.retornaTelaInicial)
        self.botaoConfirmaRemocao.clicked.connect(self.excluiPessoa)
        self.botaoEditar.clicked.connect(self.editarPessoa)
        self.botaoSalvaEdit.clicked.connect(self.salvaEdit)

    def adicionaPessoa(self):
        p1 = Pessoa()
        if(self.caixaNome.text() == None):
            p1.nome = "Em branco"
        else:
            p1.nome = self.caixaNome.text()
        if(self.caixaEmail.text() == None):
            p1.idade = "Em branco"
        else:
            p1.idade = self.caixaIdade.text()
        if(self.caixaIdade.text()== None):
            p1.email  = "Em branco"
        else:
            p1.email = self.caixaEmail.text()

        gerenciaPessoa.pessoas.append(p1)

        self.caixaNome.clear()
        self.caixaIdade.clear()
        self.caixaEmail.clear()
        print(p1.email)

    def imprimeDados(self):
        self.caixaImpressao.show()
        pessoas = ""
        for i in range(len(gerenciaPessoa.pessoas)):
            pessoas += gerenciaPessoa.pessoas[i].nome + "\n"
        self.caixaImpressao.setText(pessoas)
        self.caixaImpressao.adjustSize()

    def trocaTelaRemover(self):
        pessoas = ""
        for i in range(len(gerenciaPessoa.pessoas)):
            pessoas += gerenciaPessoa.pessoas[i].nome + "\n"
        self.caixaImpressao.setText(pessoas)

        self.caixaImpressao.adjustSize()
        self.botaoImprimir.hide()
        self.armazenaDados.hide()
        self.cabeNome.hide()
        self.cabeIdade.hide()
        self.cabeEmail.hide()
        self.caixaNome.hide()
        self.caixaIdade.hide()
        self.caixaEmail.hide()
        self.botaoTelaRemover.hide()

        self.caixaImpressao.move(50, 150)
        
        self.botaoRetornarTelaInicio.show()
        self.caixaRemover.show()
        self.botaoConfirmaRemocao.show()
        self.botaoEditar.show()
        self.textoCaixaRemover.show()

    def retornaTelaInicial(self):
        self.botaoImprimir.show()
        self.armazenaDados.show()
        self.cabeNome.show()
        self.cabeIdade.show()
        self.cabeEmail.show()
        self.caixaNome.show()
        self.caixaIdade.show()
        self.caixaEmail.show()
        self.botaoTelaRemover.show()
        self.botaoEditar.hide()

        self.caixaImpressao.move(300, 125)

        self.botaoRetornarTelaInicio.hide()
        self.botaoConfirmaRemocao.hide()
        self.caixaRemover.hide()
        self.textoCaixaRemover.hide()

    def excluiPessoa(self):
        aux = self.caixaRemover.text()
        auxIndex = None
        for i in range(len(gerenciaPessoa.pessoas)):
            print(i)
            auxP = gerenciaPessoa.pessoas[i]
            if auxP.nome == aux:
                auxIndex = i
        
        if(auxIndex != None):
            gerenciaPessoa.pessoas.remove(gerenciaPessoa.pessoas[auxIndex])
        self.caixaRemover.clear()
        self.imprimeDados()


    def editarPessoa(self):
        aux = self.caixaRemover.text()
        for i in range(len(gerenciaPessoa.pessoas)):
            auxP = gerenciaPessoa.pessoas[i]
            if auxP.nome == aux:
                self.caixaNome.show()
                self.caixaEmail.show()
                self.caixaIdade.show()

                self.caixaNome.setText(auxP.nome)
                self.caixaEmail.setText(auxP.email)
                self.caixaIdade.setText(auxP.idade)
                
                self.botaoSalvaEdit.show()
                self.caixaRemover.hide()
                self.caixaImpressao.hide()
                self.botaoTelaRemover.hide()
                self.botaoConfirmaRemocao.hide()
                self.botaoEditar.hide()
                self.textoCaixaRemover.hide()

    def salvaEdit(self):
        aux = self.caixaRemover.text()
        for i in range(len(gerenciaPessoa.pessoas)):
            auxP = gerenciaPessoa.pessoas[i]
            if auxP.nome == aux:
                p1 = Pessoa()
                p1.nome = self.caixaNome.text()
                p1.email = self.caixaEmail.text()
                p1.idade = self.caixaIdade.text()
                #gerenciaPessoa.pessoas[i].nome = self.caixaNome.text()
                #gerenciaPessoa.pessoas[i].email = self.caixaEmail.text()
                #gerenciaPessoa.pessoas[i].idade = self.caixaIdade.text()

                gerenciaPessoa.pessoas.append(p1)

                gerenciaPessoa.pessoas.remove(gerenciaPessoa.pessoas[i])
                print(gerenciaPessoa.pessoas[i].nome)
                self.caixaNome.clear()
                self.caixaEmail.clear()
                self.caixaIdade.clear()
                self.caixaRemover.clear()

                self.retornaTelaInicial()

                self.botaoSalvaEdit.hide()

gerenciaPessoa = Gerenciapessoa()

class Janela(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.show()
        self.resize(1000, 600)
        layout = QVBoxLayout()
        layout.addWidget(Widget())
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

janela = Janela()

app.exec()
