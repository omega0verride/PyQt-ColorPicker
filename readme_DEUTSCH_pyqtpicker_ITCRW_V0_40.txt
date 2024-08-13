PyQt Color Picker - Anleitung
Einführung

Dies ist eine erweiterte Version eines Farbwählers (Color Picker) für PyQt6, der es Benutzern ermöglicht, Farben auszuwählen und diese in verschiedenen Formaten wie RGB und HEX zu verwenden. In dieser Version wurden einige Verbesserungen hinzugefügt, einschließlich der Möglichkeit, eine Farbe auszuwählen und diese über einen speziellen Take Code-Button zu übernehmen.
Lizenz

BSD-Lizenz
Installation

    Voraussetzungen:
        Python 3.x
        PyQt6 Bibliothek (Installierbar über pip install PyQt6)

    Installation:
        Klone das Repository oder lade die Dateien herunter.
        Stelle sicher, dass die notwendigen Abhängigkeiten installiert sind.

    Verzeichnisse:
        Der Color Picker erwartet, dass alle benötigten Dateien im selben Verzeichnis liegen, in dem sich das Skript pyqtpicker.py befindet. Dies schließt auch die Stylesheet-Datei colorPickerStylesheet.css ein.

Nutzung
Integration des Color Pickers in ein Projekt

Hier ist ein vollständiges Codebeispiel, das zeigt, wie du den Color Picker in dein PyQt-Projekt integrieren kannst. Das Beispiel enthält einen Button zum Öffnen des Color Pickers und einen Take Code-Button zum Übernehmen der ausgewählten Farbe.
Vollständiges Codebeispiel:

python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from pyqtpicker import ColorPicker

class ThemeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Hauptfenster einrichten
        self.setWindowTitle("Theme Editor")
        self.setGeometry(100, 100, 400, 200)

        # Layout erstellen
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Button zum Öffnen des Color Pickers
        self.choose_color_button = QPushButton("Choose Color", self)
        self.choose_color_button.clicked.connect(self.open_color_picker)
        self.layout.addWidget(self.choose_color_button)

        # Button zum Übernehmen der Farbe
        self.take_color_button = QPushButton("Take Color Code", self)
        self.take_color_button.clicked.connect(lambda: self.take_color_code("Primary Color"))
        self.layout.addWidget(self.take_color_button)

        # Platzhalter für den Color Picker
        self.active_color_picker = None
        self.settings_widgets = {
            "Primary Color": self.choose_color_button
        }
        self.theme = {}

    def open_color_picker(self, setting=None):
        try:
            script_directory = os.path.dirname(os.path.realpath(__file__))

            # ColorPicker initialisieren
            self.active_color_picker = ColorPicker(width=250, startupcolor=[0, 255, 255])

            # Stylesheet anwenden
            stylesheet_path = os.path.join(script_directory, 'colorPickerStylesheet.css')
            self.active_color_picker.setStyleSheet(open(stylesheet_path).read())

            # ColorPicker anzeigen
            self.active_color_picker.show()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open color picker: {str(e)}")

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

Erklärung:

    Button zum Öffnen des Color Pickers:
        Der Button Choose Color öffnet den Color Picker, wenn er gedrückt wird.

    Button zum Übernehmen der Farbe:
        Der Button Take Color Code übernimmt die ausgewählte Farbe und wendet sie auf das entsprechende Setting an.

    Integration:
        Der Color Picker wird in das PyQt-Projekt integriert, indem er über die Methode open_color_picker aufgerufen wird. Der ausgewählte Farbcode wird durch take_color_code übernommen.

    Stylesheet:
        Das Stylesheet wird aus der Datei colorPickerStylesheet.css geladen, die sich im gleichen Verzeichnis wie das Skript pyqtpicker.py befinden muss.

Hinweise

    Der textChanged-Event für QLabel wurde entfernt, da QLabel dieses Signal nicht unterstützt. Stattdessen wird der Farbcode über den Take Code-Button übernommen.
    Alle Pfade werden relativ zu dem Verzeichnis aufgelöst, in dem sich pyqtpicker.py befindet. Dies macht die Verwendung eines globalen Arbeitsverzeichnisses überflüssig.
    
    

