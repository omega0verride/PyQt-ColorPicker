import sys

from PyQt6.QtWidgets import QApplication

from QtColorPicker import QtColorPicker

app = QApplication(sys.argv)
QtColorPicker(listener=lambda h, s, v: print(f"color: ({h}, {s}, {v})")).show()
sys.exit(app.exec())
