from list.list_window import ListWindow
from PyQt5.QtWidgets import QMainWindow

class WindowManager:
    def __init__(self, app):
        self.app = app
        self.windows = {}
        self._initialise_window_classes()

    def toggle_window_visibility(self, window_key: str) -> None:
        """Toggles the visibility of a window type based on a key."""
        if window_key in self.windows.keys():
            self._toggle_window_visibility(self.windows[window_key])
        else:
            print("Window not implemented")

    def _initialise_window_classes(self) -> None:
        """Creates the classes for the windows supported by the overlay."""
        self.windows['list'] = ListWindow(self.app)

    def _toggle_window_visibility(self, window: QMainWindow) -> None:
        """Toggles visibility of the passed window."""
        if window.isVisible():
            window.hide()
        else:
            window.show()

