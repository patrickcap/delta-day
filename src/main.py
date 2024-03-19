from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.text_array = []  # Initialize an empty array to store text
        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()

        # Create text box
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Enter your text here")

        # Create enter button
        self.enter_button = QPushButton("Enter")
        self.enter_button.clicked.connect(self.handle_enter_click)  # Connect button click to a function

        # Add text box and button to layout
        layout.addWidget(self.text_box)
        layout.addWidget(self.enter_button)

        # Set layout to window
        self.setLayout(layout)

        # Set window title
        self.setWindowTitle("Delta Day")

        # Center window (same as before)
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

    def handle_enter_click(self):
        # Get text from the box
        text = self.text_box.text()

        # Check if text is empty
        if text:
            # Add text to the array
            self.text_array.append(text)

            # Clear the text box
            self.text_box.clear()

            # (Optional) Display a message or perform other actions based on the stored text

if __name__ == "__main__":
    # Create application instance
    app = QApplication([])

    # Create window instance
    window = Window()

    # Run the application loop
    sys.exit(app.exec_())
