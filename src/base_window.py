from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QGraphicsDropShadowEffect, QPushButton, QHBoxLayout,
    QApplication
)


class BaseWindow(QMainWindow):
    def __init__(self, app=None):
        super().__init__()
        self.app = app

        # Make window transparent with no frame and always on top
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.configure_window_flags()
        self.setup_window_geometry()

        # Outer vertical layout with margin
        self.outer_layout = QVBoxLayout()
        self.outer_layout.setContentsMargins(20, 20, 20, 20)

        # Main panel container with semi-transparent black bg and rounded corners
        self.panel_container = QWidget()
        self.panel_container.setObjectName("PanelContainer")
        self.panel_container.setStyleSheet("""
            QWidget#PanelContainer {
                background-color: rgba(40, 40, 40, 200);
                border-radius: 20px;
            }
        """)

        # Add drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 160))
        self.panel_container.setGraphicsEffect(shadow)

        # Layout inside the panel container
        self.panel_layout = QVBoxLayout()
        self.panel_layout.setContentsMargins(20, 20, 20, 20)

        # Add logo widget
        self.panel_layout.addWidget(self.setup_ui_logo())

        # Add the general buttons row (settings and exit)
        self.panel_layout.addLayout(self.setup_header_buttons())

        self.panel_container.setLayout(self.panel_layout)
        self.outer_layout.addWidget(self.panel_container)

        # Wrap everything in a central widget
        wrapper = QWidget()
        wrapper.setLayout(self.outer_layout)
        self.setCentralWidget(wrapper)

    def configure_window_flags(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

    def setup_window_geometry(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = int(screen_width * 0.25)
        window_height = screen_height
        x_position = screen_geometry.right() - window_width
        y_position = screen_geometry.top()

        self.setGeometry(x_position, y_position, window_width, window_height)
        self.setFixedSize(window_width, window_height)

    def setup_ui_logo(self) -> QLabel:
        logo_label = QLabel()
        pixmap = QPixmap("assets/logo.png")
        scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignHCenter)
        logo_label.setMaximumHeight(300)
        return logo_label

    def setup_header_buttons(self) -> QHBoxLayout:
        header_layout = QHBoxLayout()
        self.settings_button = QPushButton("⚙")
        self.exit_button = QPushButton("Exit")
        # Exit closes app if app provided, else closes window
        self.exit_button.clicked.connect(self.app.quit if self.app else self.close)

        header_layout.addWidget(self.settings_button)
        header_layout.addWidget(self.exit_button)
        return header_layout

    def paintEvent(self, event):
        # Transparent background paint (helps with translucent window)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.transparent)
        painter.drawRect(self.rect())
