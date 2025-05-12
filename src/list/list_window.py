from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (
    QApplication, 
    QHBoxLayout, 
    QLabel,
    QLineEdit, 
    QMainWindow, 
    QPushButton,
    QScrollArea,
    QVBoxLayout, 
    QWidget,
    QGraphicsDropShadowEffect
)

class ListWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.configure_window_flags()
        self.setup_window_geometry()
        self.initialize_ui()

    def configure_window_flags(self) -> None:
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

    def setup_window_geometry(self) -> None:
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
        # Outer layout with transparent background
        outer_layout = QVBoxLayout()
        outer_layout.setContentsMargins(20, 20, 20, 20)

        # Inner container with semi-transparent background and shadow
        self.panel_container = QWidget()
        self.panel_container.setObjectName("PanelContainer")
        self.panel_container.setStyleSheet("""
            QWidget#PanelContainer {
                background-color: rgba(40, 40, 40, 200);
                border-radius: 20px;
            }
        """)

        # Drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 160))
        self.panel_container.setGraphicsEffect(shadow)

        # Main layout inside the styled container
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(self.setup_ui_logo())
        layout.addLayout(self.setup_header_ui())
        layout.addWidget(self.setup_list_ui())
        layout.addLayout(self.setup_input_ui())

        self.panel_container.setLayout(layout)
        outer_layout.addWidget(self.panel_container)

        wrapper = QWidget()
        wrapper.setLayout(outer_layout)
        self.setCentralWidget(wrapper)

    def paintEvent(self, event) -> None:
        # Transparent background
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.transparent)
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
