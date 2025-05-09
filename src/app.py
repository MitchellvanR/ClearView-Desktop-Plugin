import sys
import keyboard
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from list_ui import MainWindow


class MyApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.window = MainWindow(self)
        self.listen_for_shortcuts()

    def listen_for_shortcuts(self):
        """Listen for global hotkeys in a non-blocking way."""
        keyboard.add_hotkey('alt+l', self.toggle_window)

    def toggle_window(self):
        """Schedule the window toggle in the main thread."""
        QTimer.singleShot(0, self._toggle_window)

    def _toggle_window(self):
        """Toggle the window's visibility."""
        if self.window.isVisible():
            self.window.hide()
        else:
            self.window.show()

app = MyApp(sys.argv)

sys.exit(app.exec())

