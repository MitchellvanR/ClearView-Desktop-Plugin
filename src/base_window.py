from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QGraphicsDropShadowEffect
)

class BaseWindow(QMainWindow):
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
        screen_geometry = self.app.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = int(screen_width * 0.25)
        window_height = screen_height
        x_position = screen_geometry.right() - window_width
        y_position = screen_geometry.top()

        self.setGeometry(x_position, y_position, window_width, window_height)
        self.setFixedSize(window_width, window_height)

    def initialize_ui(self) -> None:
        # Outer layout with transparent background and margins
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

        # Layout inside panel container
        panel_layout = QVBoxLayout()
        panel_layout.setContentsMargins(20, 20, 20, 20)

        # Header widget
        self.header_widget = QWidget()
        self.header_widget.setFixedHeight(100)
        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(10, 10, 10, 10)
        self.header_widget.setLayout(self.header_layout)

        # Logo label
        self.logo_label = QLabel()
        pixmap = QPixmap("assets/logo.png")
        scaled_pixmap = pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.header_layout.addWidget(self.logo_label)

        self.header_layout.addStretch()

        # Settings and Exit buttons
        self.settings_button = QPushButton("⚙")
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.app.quit)

        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(10)
        buttons_widget.setLayout(buttons_layout)
        buttons_layout.addWidget(self.settings_button)
        buttons_layout.addWidget(self.exit_button)

        self.header_layout.addWidget(buttons_widget)

        # Separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: gray;")

        # Content widget for child classes
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 10, 0, 0)
        self.content_widget.setLayout(self.content_layout)

        # Assemble the panel layout
        panel_layout.addWidget(self.header_widget)
        panel_layout.addWidget(separator)
        panel_layout.addWidget(self.content_widget)

        self.panel_container.setLayout(panel_layout)
        outer_layout.addWidget(self.panel_container)

        wrapper = QWidget()
        wrapper.setLayout(outer_layout)
        self.setCentralWidget(wrapper)

    def paintEvent(self, event) -> None:
        # Transparent background painting
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.transparent)
        painter.drawRect(self.rect())
