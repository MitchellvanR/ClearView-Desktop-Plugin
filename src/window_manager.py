from PyQt5.QtCore import QTimer
from list.list_window import ListWindow

class WindowManager:
    def __init__(self, app):
        self.app = app
        self.windows = {}
        self.initialise_window_classes()

    def initialise_window_classes(self):
        self.windows['list'] = ListWindow(self.app)

    def toggle_window(self, window_key):
        if window_key in self.windows.keys():
            self._toggle_window(self.windows[window_key])
        else:
            print("Window not implemented")

    def _toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
