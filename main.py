import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAMA MODI 1")

        self.setGeometry(100, 100, 400, 400)  # x, y, ancho, alto
        self.setStyleSheet("background-color:rgb(166,128,126);")
        self.inicializar_ui()

    def inicializar_ui(self):
        # Crear botón
        boton = QPushButton("¡DEVELOP!", self)
        boton1 = QPushButton("¡DEVELOP!", self)

        boton.setGeometry(10, 30, 100, 100)  # x, y, ancho, alto
        boton1.setGeometry(150, 30, 100, 100)

        # Hacer botón redondo usando estilos CSS
        boton.setStyleSheet("""
            QPushButton {
                border-radius: 20px;  /* la mitad del ancho/alto para hacerlo redondo */
                background-color: #e61263;
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #8ee612;
            }
        """)

        boton1.setStyleSheet("""
                    QPushButton {
                        border-radius: 40px;  /* la mitad del ancho/alto para hacerlo redondo */
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
