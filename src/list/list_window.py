from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton,
    QScrollArea, QWidget, QLineEdit
)
from base_window import BaseWindow


class ListWindow(BaseWindow):
    def __init__(self, app):
        self.app = app
        super().__init__(app)  # Set up base UI (background, logo, buttons)

        # Add the two custom header buttons ('Clear', '?')
        self.panel_layout.addLayout(self.setup_local_header_buttons())

        # Add scrollable list and input area
        self.panel_layout.addWidget(self.setup_list_ui())
        self.panel_layout.addLayout(self.setup_input_ui())

    def setup_local_header_buttons(self) -> QHBoxLayout:
        header_layout = QHBoxLayout()
        clear_button = QPushButton("Clear")
        help_button = QPushButton("?")

        header_layout.addWidget(clear_button)
        header_layout.addWidget(help_button)
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

    def handle_add_todo(self):
        # Placeholder for todo logic
        pass
