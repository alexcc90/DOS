import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAMA FEATURES1")
        self.setGeometry(100, 100, 300, 200)  # x, y, ancho, alto
        self.setStyleSheet("background-color:rgb(166,128,126);")
        self.inicializar_ui()

    def inicializar_ui(self):
        # Crear botón
        boton = QPushButton("¡FEATURES1!", self)
        boton.setGeometry(100, 60, 100, 100)  # x, y, ancho, alto

        # Hacer botón redondo usando estilos CSS
        boton.setStyleSheet("""
            QPushButton {
                border-radius: 50px;  /* la mitad del ancho/alto para hacerlo redondo */
                background-color: #e61263;
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #8ee612;
            }
        """)

        # Conectar acción al botón
        boton.clicked.connect(self.boton_presionado)

    def boton_presionado(self):
        print("¡Botón redondo presionado!")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
