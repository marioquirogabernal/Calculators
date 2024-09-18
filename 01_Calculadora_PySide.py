import sys

from PySide6.QtGui import QFontDatabase, QFont, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QWidget

class LineEditPersonalizado(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        # Definir las teclas permitidas
        allowed_keys = '0123456789*/+-.'
        if event.text() in allowed_keys:
            super().keyPressEvent(event)
        else:
            event.ignore()  # Ignorar otras teclas
class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(300,280)
        # Inicializamos variable a utilizar
        self.resultado = None
        # Creamos componentes
        # Linea de texto
        self.entrada = LineEditPersonalizado()
        # Configuramos la linea de texto
        self.entrada.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.entrada.setFixedHeight(50) # Establecemos Altura
        # Botones Numeros
        self.cero = QPushButton('0')
        self.uno = QPushButton('1')
        self.dos = QPushButton('2')
        self.tres = QPushButton('3')
        self.cuatro = QPushButton('4')
        self.cinco = QPushButton('5')
        self.seis = QPushButton('6')
        self.siete = QPushButton('7')
        self.ocho = QPushButton('8')
        self.nueve = QPushButton('9')
        # Botones Extra
        self.punto = QPushButton('.')
        self.c = QPushButton('C')
        self.igual = QPushButton('=')
        # Botones Operacion
        self.division = QPushButton('/')
        self.multiplicacion = QPushButton('x')
        self.resta = QPushButton('-')
        self.suma = QPushButton('+')
        # Creamos layout grid
        self.layout_grid = QGridLayout()
        self.layout_grid.addWidget(self.siete, 0, 0)
        self.layout_grid.addWidget(self.ocho, 0, 1)
        self.layout_grid.addWidget(self.nueve,0, 2)
        self.layout_grid.addWidget(self.division, 0, 3)
        self.layout_grid.addWidget(self.cuatro, 1, 0)
        self.layout_grid.addWidget(self.cinco, 1, 1)
        self.layout_grid.addWidget(self.seis, 1, 2)
        self.layout_grid.addWidget(self.multiplicacion, 1, 3)
        self.layout_grid.addWidget(self.uno, 2, 0)
        self.layout_grid.addWidget(self.dos, 2, 1)
        self.layout_grid.addWidget(self.tres, 2, 2)
        self.layout_grid.addWidget(self.resta, 2, 3)
        self.layout_grid.addWidget(self.cero, 3, 0)
        self.layout_grid.addWidget(self.punto, 3, 1)
        self.layout_grid.addWidget(self.c, 3, 2)
        self.layout_grid.addWidget(self.suma, 3, 3)
        self.layout_grid.addWidget(self.igual, 3, 4)
        # Cargamos fuente personalizada
        fuente_path = f"D:/Cursos Udemy/fuentes/PressStart2P-Regular.ttf"
        fuente_id = QFontDatabase.addApplicationFont(fuente_path)
        fuente_familia = QFontDatabase.applicationFontFamilies(fuente_id)[0]
        # Crear un objeto QFont y configurar el tamaño y estilo de la fuente
        fuente = QFont(fuente_familia, 13)
        # Aplicar la fuente a cada widget individualmente
        self.entrada.setFont(fuente)
        self.cero.setFont(fuente)
        self.uno.setFont(fuente)
        self.dos.setFont(fuente)
        self.tres.setFont(fuente)
        self.cuatro.setFont(fuente)
        self.cinco.setFont(fuente)
        self.seis.setFont(fuente)
        self.siete.setFont(fuente)
        self.ocho.setFont(fuente)
        self.nueve.setFont(fuente)
        self.punto.setFont(fuente)
        self.c.setFont(fuente)
        self.igual.setFont(fuente)
        self.division.setFont(fuente)
        self.multiplicacion.setFont(fuente)
        self.resta.setFont(fuente)
        self.suma.setFont(fuente)
        # Creamos el layout vertical
        self.layout_vertical = QVBoxLayout()
        # Añadimos componentes al layout vertical
        self.layout_vertical.addWidget(self.entrada)
        self.layout_vertical.addLayout(self.layout_grid)
        # Especificamos espacios entre componentes
        self.layout_vertical.setSpacing(10)
        self.layout_vertical.setContentsMargins(15,10,15,10)
        # Definimos funciones de los botones
        self.cero.clicked.connect(lambda: self._click('0'))
        self.uno.clicked.connect(lambda: self._click('1'))
        self.dos.clicked.connect(lambda: self._click('2'))
        self.tres.clicked.connect(lambda: self._click('3'))
        self.cuatro.clicked.connect(lambda: self._click('4'))
        self.cinco.clicked.connect(lambda: self._click('5'))
        self.seis.clicked.connect(lambda: self._click('6'))
        self.siete.clicked.connect(lambda: self._click('7'))
        self.ocho.clicked.connect(lambda: self._click('8'))
        self.nueve.clicked.connect(lambda: self._click('9'))
        self.punto.clicked.connect(lambda: self._click('.'))
        self.division.clicked.connect(lambda: self._click_op('/'))
        self.multiplicacion.clicked.connect(lambda: self._click_op('*'))
        self.resta.clicked.connect(lambda: self._click_op('-'))
        self.suma.clicked.connect(lambda: self._click_op('+'))
        self.c.clicked.connect(self._click_c)
        self.igual.clicked.connect(self._click_igual)
        # Creamos componente central
        self.componente = QWidget()
        self.componente.setLayout(self.layout_vertical)
        # Publicamos el componente
        self.setCentralWidget(self.componente)

    def _click(self, tecla):
        operacion = self.entrada.text()
        if operacion == "Error!" or str(operacion) == str(self.resultado):
            operacion = ""
        self.entrada.setText(operacion + tecla)
    def _click_op(self, tecla):
        operacion = self.entrada.text()
        if operacion == "Error!":
            operacion = ""
        self.entrada.setText(operacion + tecla)
    def _click_c(self):
        self.entrada.setText("")
    def _click_igual(self):
        try:
            operacion = self.entrada.text()
            self.resultado = eval(operacion)
            self.entrada.setText(str(self.resultado))
        except Exception as e:
            self.entrada.setText("Error!")


app = QApplication()
ventana = Calculadora()
ventana.show()
sys.exit(app.exec())

