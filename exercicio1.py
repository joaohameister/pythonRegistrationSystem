from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QLabel,
)

app = QApplication([])


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setContentsMargins(30, 30, 30, 30)

        self.valor = 0

        self.caixaValor = QLabel(self)
        self.caixaValor.move(50, 50)

        self.caixaValor.setScaledContents(True)

        self.caixaValor.setText(str(self.valor))

        self.aumentaNumero = QPushButton("Aumenta valor", self)
        self.aumentaNumero.move(50, 100)

        self.aumentaNumero.clicked.connect(self.incrementaValor)

    def incrementaValor(self):
        self.valor += 1
        self.caixaValor.setText(str(self.valor))
        self.caixaValor.adjustSize()


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
