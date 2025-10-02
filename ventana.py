from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QPushButton, QLabel)
from PyQt6.QtCore import Qt


class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la segunda ventana
        self.setWindowTitle('Ventana Secundaria')
        self.setGeometry(400, 400, 350, 200)

        # Widget central y layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Mensaje de bienvenida
        welcome_label = QLabel('¡Ventana 2!')
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("""
            font-size: 24px; 
            font-weight: bold; 
            color: #2E86AB;
            margin: 30px;
            padding: 20px;
            background-color: #E8F4F8;
            border-radius: 10px;
        """)
        layout.addWidget(welcome_label)

        # Botón para cerrar esta ventana
        self.btn_close = QPushButton('Cerrar Ventana')
        self.btn_close.setStyleSheet("""
            QPushButton {
                background-color: #FF6B6B;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
                margin: 20px;
            }
            QPushButton:hover {
                background-color: #EE5A5A;
            }
        """)
        self.btn_close.clicked.connect(self.close)
        layout.addWidget(self.btn_close)

        # Espaciador
        layout.addStretch()
