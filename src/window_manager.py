from list.list_window import ListWindow
from base_window import BaseWindow  # for NotepadWindow and CalculatorWindow stubs
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QGuiApplication

class WindowManager:
    MAX_WINDOWS = 3
    WINDOW_WIDTH_RATIO = 0.25  # 25% screen width

    def __init__(self, app):
        self.app = app
        self.windows = {}
        self.visible_windows = []  # list of currently visible windows, order matters
        self._initialise_window_classes()

    def _initialise_window_classes(self) -> None:
        self.windows['list'] = ListWindow(self.app)
        self.windows['notepad'] = BaseWindow(self.app)
        self.windows['calculator'] = BaseWindow(self.app)

    def toggle_window_visibility(self, window_key: str) -> None:
        if window_key not in self.windows:
            print("Window not implemented")
            return

        window = self.windows[window_key]

        if window.isVisible():
            self._hide_window(window)
        else:
            self._show_window(window)

        self._reposition_windows()

    def _show_window(self, window: QMainWindow) -> None:
        if window in self.visible_windows:
            # Already visible, no need to add again
            return

        # If max windows reached, hide oldest (first) window
        if len(self.visible_windows) >= self.MAX_WINDOWS:
            oldest = self.visible_windows.pop(0)
            oldest.hide()

        # Show and add window to the right-most position
        window.show()
        self.visible_windows.append(window)

    def _hide_window(self, window: QMainWindow) -> None:
        if window in self.visible_windows:
            window.hide()
            self.visible_windows.remove(window)

    def _reposition_windows(self) -> None:
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = int(screen_width * self.WINDOW_WIDTH_RATIO)
        window_height = screen_height
        margin_right = screen_geometry.right() - (screen_width - window_width)  # basically zero but keep for clarity
        margin_between = margin_right  # keep same margin as right margin for spacing between windows

        for idx, window in enumerate(reversed(self.visible_windows)):
            x_pos = screen_geometry.right() - window_width - margin_between * idx
            y_pos = screen_geometry.top()
            window.setGeometry(x_pos, y_pos, window_width, window_height)
            window.setFixedSize(window_width, window_height)

        # Show settings and exit buttons only on the right-most window
        if not self.visible_windows:
            return

        right_most_window = self.visible_windows[-1]
        for window in self.visible_windows:
            if hasattr(window, 'settings_button') and hasattr(window, 'exit_button'):
                if window == right_most_window:
                    window.settings_button.show()
                    window.exit_button.show()
                else:
                    window.settings_button.hide()
                    window.exit_button.hide()
