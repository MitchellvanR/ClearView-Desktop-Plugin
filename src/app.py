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
        self._setup_global_hotkeys()

    def _handle_hotkey(self, window_type: str) -> None:
        """Fires an event to the main thread to toggle to the correct window according to the hotkey used."""
        QTimer.singleShot(0, partial(self.toggle_window_status, window_type))

    def _setup_global_hotkeys(self) -> None:
        """Starts a thread that listens for hotkeys."""
        def hotkey_thread():
            keyboard.add_hotkey('alt+l', partial(self.handle_hotkey, 'list'))
            keyboard.add_hotkey('alt+n', partial(self.handle_hotkey, 'notepad'))
            keyboard.add_hotkey('alt+c', partial(self.handle_hotkey, 'calculator'))
            keyboard.wait()

        threading.Thread(target=hotkey_thread, daemon=True).start()

    def _toggle_window_status(self, window_type: str) -> None:
        """Starts the process of toggling the activated or deactivated window status."""
        self.manager.toggle_window_visibility(window_type)


if __name__ == "__main__":
    app = MyApp(sys.argv)
    sys.exit(app.exec())

