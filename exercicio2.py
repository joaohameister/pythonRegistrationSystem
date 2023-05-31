from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QLineEdit,
)

app = QApplication([])


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setContentsMargins(30, 30, 30, 30)

        self.inputNome = QLineEdit(self)
        self.inputNome.move(50, 50)

        imprimeNome = QPushButton("Imprimir saudação", self)
        imprimeNome.move(50, 100)

        self.caixaTexto = QLabel(self)
        self.caixaTexto.move(50, 150)

        imprimeNome.clicked.connect(self.imprimeSaudacao)

    def imprimeSaudacao(self):
        self.caixaTexto.setText("Olá " + self.inputNome.text())
        self.caixaTexto.adjustSize()
        self.inputNome.clear()


class Janela(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.show()
        self.resize(300, 300)
        layout = QVBoxLayout()
        layout.addWidget(Widget())
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


janela = Janela()

app.exec()
