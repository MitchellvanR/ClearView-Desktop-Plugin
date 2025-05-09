from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import (
    QApplication, 
    QHBoxLayout, 
    QLabel,
    QLineEdit, 
    QMainWindow, 
    QPushButton,
    QScrollArea,
    QVBoxLayout, 
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.configure_window_flags()
        self.setup_window_geometry()
        self.initialize_ui()

    def configure_window_flags(self) -> None:
        """Set window to stay on top, remove window frame and to not appear on the toolbar."""
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

    def setup_window_geometry(self) -> None:
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

    def initialize_ui(self) -> None:
        """Set up the main UI layout."""
        layout = QVBoxLayout()

        layout.addWidget(self.setup_ui_logo())
        layout.addLayout(self.setup_header_ui())
        layout.addWidget(self.setup_list_ui())
        layout.addLayout(self.setup_input_ui())

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def paintEvent(self, event) -> None:
        """Override paintEvent to apply the semi-transparent background."""
        painter = QPainter(self)
        painter.setPen(Qt.transparent)

        transparent_black = QColor(253, 241, 218, 50)

        painter.setBrush(transparent_black)
        painter.drawRect(self.rect())

    def setup_ui_logo(self) -> QLabel:
        logo_label = QLabel()

        pixmap = QPixmap("assets/logo.png")
        scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignHCenter)
        
        logo_label.setMaximumHeight(300)
        
        return logo_label

    def setup_header_ui(self) -> QHBoxLayout:
        """Set up the header UI layout"""
        header_layout = QHBoxLayout()

        clear_button = QPushButton("Clear")
        help_button = QPushButton("?")
        settings_button = QPushButton("⚙")
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.app.quit)

        header_layout.addWidget(clear_button)
        header_layout.addWidget(help_button)
        header_layout.addWidget(settings_button)
        header_layout.addWidget(exit_button)

        return header_layout
    
    def setup_list_ui(self) -> QScrollArea:
        """Set up the list UI layout"""
        self.list_container = QVBoxLayout()

        list_widget = QWidget()
        list_widget.setLayout(self.list_container)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setWidget(list_widget)
        scroll_area.setFixedHeight(300)

        return scroll_area

    def setup_input_ui(self) -> QHBoxLayout:
        input_layout = QHBoxLayout()

        self.list_input = QLineEdit()
        self.list_input.setPlaceholderText("Add a new item...")
        self.list_input.returnPressed.connect(self.handle_add_todo)

        submit_button = QPushButton("Add")
        submit_button.clicked.connect(self.handle_add_todo)

        input_layout.addWidget(self.list_input)
        input_layout.addWidget(submit_button)

        return input_layout

    def handle_add_todo(self) -> None:
        pass

