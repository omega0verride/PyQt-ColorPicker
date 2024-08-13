# pyqtpicker
PyQt Color Picker - Instructions
Introduction

This is an enhanced version of a Color Picker for PyQt6, allowing users to select colors and use them in various formats such as RGB and HEX. This version includes improvements, such as the ability to select a color and apply it using a dedicated Take Code button.
License

BSD License
Installation

    Requirements:
        Python 3.x
        PyQt6 Library (Installable via pip install PyQt6)

    Installation:
        Clone the repository or download the files.
        Ensure all necessary dependencies are installed.

    Directories:
        The Color Picker expects all required files to be in the same directory as the pyqtpicker.py script. This includes the stylesheet file colorPickerStylesheet.css.

Usage
Integrating the Color Picker into a Project

Below is a complete example showing how to integrate the Color Picker into your PyQt project. The example includes a button to open the Color Picker and a Take Code button to apply the selected color.
Full Example:
------------------------------------------------------------------------------------------------------
python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from pyqtpicker import ColorPicker

class ThemeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup main window
        self.setWindowTitle("Theme Editor")
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Button to open the Color Picker
        self.choose_color_button = QPushButton("Choose Color", self)
        self.choose_color_button.clicked.connect(self.open_color_picker)
        self.layout.addWidget(self.choose_color_button)

        # Button to take the selected color
        self.take_color_button = QPushButton("Take Color Code", self)
        self.take_color_button.clicked.connect(lambda: self.take_color_code("Primary Color"))
        self.layout.addWidget(self.take_color_button)

        # Placeholder for the Color Picker
        self.active_color_picker = None
        self.settings_widgets = {
            "Primary Color": self.choose_color_button
        }
        self.theme = {}

    def open_color_picker(self, setting=None):
        try:
            script_directory = os.path.dirname(os.path.realpath(__file__))

            # Initialize the Color Picker
            self.active_color_picker = ColorPicker(width=250, startupcolor=[0, 255, 255])

            # Apply the stylesheet
            stylesheet_path = os.path.join(script_directory, 'colorPickerStylesheet.css')
            self.active_color_picker.setStyleSheet(open(stylesheet_path).read())

            # Show the Color Picker
            self.active_color_picker.show()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open color picker: {str(e)}")
	    
     	    # TAKE THE COLOR CODE
    def take_color_code(self, setting):
        if self.active_color_picker and hasattr(self.active_color_picker.colorpickerWidget, 'colorCodeLabel'):
            hex_color = self.active_color_picker.colorpickerWidget.colorCodeLabel.text()
            self.settings_widgets[setting].setStyleSheet(f"background-color: {hex_color}; border: 1px solid black;")
            self.theme[setting] = hex_color
        else:
            QMessageBox.warning(self, "Error", "Color picker not open or no color selected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThemeEditor()
    window.show()
    sys.exit(app.exec())
-----------------------------------------------------------------------------------------------
Explanation:

    Button to Open the Color Picker:
        The Choose Color button opens the Color Picker when clicked.

    Button to Take the Selected Color:
        The Take Color Code button applies the selected color and updates the corresponding setting.

    Integration:
        The Color Picker is integrated into the PyQt project and is called via the open_color_picker method. The selected color code is applied using the take_color_code method.

    Stylesheet:
        The stylesheet is loaded from the colorPickerStylesheet.css file, which must be in the same directory as the pyqtpicker.py script.

Notes

    The textChanged event for QLabel was removed because QLabel does not support this signal. Instead, the color code is applied via the Take Code button.
    All paths are resolved relative to the directory where pyqtpicker.py is located, making the use of a global working directory unnecessary.

