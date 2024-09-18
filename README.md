Código PySide6 (Qt):
Este código crea una aplicación de calculadora utilizando PySide6 y Qt. Incluye:

Clase LineEditPersonalizado: Una subclase de QLineEdit que solo permite la entrada de caracteres específicos (números y operadores matemáticos).
Clase Calculadora: Define una ventana principal (QMainWindow) con una interfaz gráfica de calculadora, incluyendo botones para números, operadores, y funcionalidad básica de cálculo.
Interfaz:
Utiliza un diseño en cuadrícula (QGridLayout) para los botones y un diseño vertical (QVBoxLayout) para la disposición general.
Carga una fuente personalizada para los botones.
Implementa funciones para manejar la entrada de botones, limpiar la entrada y calcular resultados.


Código Tkinter:
Este código crea una calculadora utilizando Tkinter. Incluye:

Clase Calculadora: Define una ventana principal (Tk) con una interfaz de calculadora, utilizando botones para números y operadores.
Interfaz:
Utiliza un diseño de cuadrícula para los botones y una entrada (Entry) para mostrar las operaciones y resultados.
Implementa funciones para manejar la entrada de botones, validar la entrada y calcular resultados utilizando eval().
Incluye manejo de errores para la división por cero y expresiones inválidas, mostrando mensajes de error cuando sea necesario.
Ambos códigos crean una calculadora con una interfaz gráfica, pero utilizan diferentes bibliotecas para hacerlo: PySide6 con Qt y Tkinter con el módulo estándar de Python.
