from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.configure_window_flags()
        self.setup_window_geometry()
        self.initialize_ui()

    def configure_window_flags(self):
        """Set window to stay on top, remove window frame and to not appear on the toolbar."""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

    def setup_window_geometry(self):
        """Position the window on the right edge of the screen and set size."""
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = int(screen_width * 0.25)
        window_height = screen_height
        x_position = screen_geometry.right() - window_width
        y_position = screen_geometry.top()

        self.setGeometry(x_position, y_position, window_width, window_height)
        self.setFixedSize(window_width, window_height)

    def initialize_ui(self):
        """Set up the main UI layout."""
        layout = QVBoxLayout()

        # Temporary
        # ------------------------------------------
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.app.quit)
        # ------------------------------------------

        layout.addWidget(QLineEdit())
        layout.addWidget(exit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

