from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QComboBox
)
import datetime
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.text_array = []  # Initialize an empty array to store text
        self.category_options = ["Select Category"]  # List to store defined categories
        self.init_ui()

    def init_ui(self):
        # Create main layout
        layout = QVBoxLayout()

        # Create text box and button layout
        text_box_layout = QHBoxLayout()

        # Create text box
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Enter your text here")
        text_box_layout.addWidget(self.text_box)

        # Create category selection
        self.category_box = QComboBox()
        self.category_box.addItems(self.category_options)  # Add initial options

        # Create new category text box
        self.new_category_box = QLineEdit()
        self.new_category_box.setPlaceholderText("New Category")

        # Create button to add new category
        self.add_category_button = QPushButton("Add")
        self.add_category_button.clicked.connect(self.handle_add_category)

        # Layout for category selection
        category_layout = QHBoxLayout()
        category_layout.addWidget(self.category_box)
        category_layout.addWidget(self.new_category_box)
        category_layout.addWidget(self.add_category_button)

        # Add text box, category selection, and button to layout
        text_box_layout.addLayout(category_layout)

        # Create enter button
        self.enter_button = QPushButton("Enter")
        self.enter_button.clicked.connect(self.handle_enter_click)  # Connect button click to a function
        text_box_layout.addWidget(self.enter_button)

        # Add text box and button layout to main layout
        layout.addLayout(text_box_layout)

        # Create entries display box
        self.entries_box = QTextEdit()
        self.entries_box.setReadOnly(True)  # Make entries box read-only
        layout.addWidget(self.entries_box)

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

    def handle_add_category(self):
        # Get new category text
        new_category = self.new_category_box.text().strip()

        # Check if new category is empty or already exists
        if new_category and new_category not in self.category_options:
            self.category_options.append(new_category)
            self.category_box.addItem(new_category)
            self.new_category_box.clear()  # Clear new category text box

    def handle_enter_click(self):
        # Get text from the box
        text = self.text_box.text()

        # Check if text is empty
        if text:
            # Get selected category
            selected_category = self.category_box.currentText()

            # Add timestamp to the text
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_text = f"{timestamp} - {selected_category}: {text}"

            # Append formatted text to the array
            self.text_array.append(formatted_text)

            # Sort the array by timestamp (descending order)
            self.text_array.sort(reverse=True)

            # Clear text box
            self.text_box.clear()

            # Update entries display box
            self.update_entries_box()


    def update_entries_box(self):
        # Clear current entries
        self.entries_box.clear()

        # Add all entries from the array to the display box
        for entry in self.text_array:
            self.entries_box.append(entry + "\n")  # Add newline character after each entry

if __name__ == "__main__":
    # Create application instance
    app = QApplication([])

    # Create window instance
    window = Window()

    # Run the application loop
    sys.exit(app.exec_())
