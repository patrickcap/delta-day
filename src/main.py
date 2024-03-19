from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit

class TextEntryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()

        # Create text box
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Enter your text here")

        # Add text box to layout
        layout.addWidget(self.text_box)

        # Set layout to window
        self.setLayout(layout)

        # Set window title
        self.setWindowTitle("Text Entry")

        # Center window
        self.center_window()

        # Show the window
        self.show()

    def center_window(self):
        # Get screen size
        screen_geometry = QApplication.desktop().screenGeometry()

        # Get window size
        window_geometry = self.geometry()

        # Calculate center position
        center_x = (screen_geometry.width() - window_geometry.width()) // 2
        center_y = (screen_geometry.height() - window_geometry.height()) // 2

        # Move window to center
        self.move(center_x, center_y)

if __name__ == "__main__":
    # Create application instance
    app = QApplication([])

    # Create window instance
    window = TextEntryWindow()

    # Run the application loop
    sys.exit(app.exec_())
