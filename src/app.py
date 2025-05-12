import sys
import threading
import keyboard
from functools import partial
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from window_manager import WindowManager

class MyApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.manager = WindowManager(self)
        self.setup_global_hotkeys()

    def setup_global_hotkeys(self):
        """Listen for global hotkeys in a separate thread."""
        def hotkey_thread():
            keyboard.add_hotkey('alt+l', partial(self.handle_hotkey, 'list'))
            keyboard.add_hotkey('alt+n', partial(self.handle_hotkey, 'notepad'))
            keyboard.add_hotkey('alt+c', partial(self.handle_hotkey, 'calculator'))
            keyboard.wait()

        threading.Thread(target=hotkey_thread, daemon=True).start()

    def handle_hotkey(self, window_type):
        QTimer.singleShot(0, partial(self.toggle_correct_window, window_type))

    def toggle_correct_window(self, window_type):
        self.manager.toggle_window(window_type)

if __name__ == "__main__":
    app = MyApp(sys.argv)
    sys.exit(app.exec())
