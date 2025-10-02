import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QPushButton, QLabel)
from PyQt6.QtCore import Qt
from ventana import SecondWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        # Configuración de la ventana principal
        self.setWindowTitle('VERSION 1.2')
        self.setGeometry(300, 300, 400, 300)

        # Widget central y layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Título
        title = QLabel('VENTANA PRINCIPAL')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        layout.addWidget(title)

        # Botón para abrir segunda ventana
        self.btn_open = QPushButton('Abrir Ventana 2')
        self.btn_open.setStyleSheet("""
                    QPushButton {
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        padding: 10px;
                        font-size: 14px;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                """)
        self.btn_open.clicked.connect(self.open_second_window)
        layout.addWidget(self.btn_open)

        # Botón para cerrar aplicación
        self.btn_close = QPushButton('Cerrar Aplicación')
        self.btn_close.setStyleSheet("""
                    QPushButton {
                        background-color: #f44336;
                        color: white;
                        border: none;
                        padding: 10px;
                        font-size: 14px;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #da190b;
                    }
                """)
        self.btn_close.clicked.connect(self.close_application)
        layout.addWidget(self.btn_close)

        # Espaciador
        layout.addStretch()

    def open_second_window(self):
        """Abre la segunda ventana"""
        self.second_window = SecondWindow()
        self.second_window.show()

    def close_application(self):
        """Cierra la aplicación"""
        self.close()


def main():
    app = QApplication(sys.argv)

    # Estilo general de la aplicación
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f0f0f0;
        }
    """)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

