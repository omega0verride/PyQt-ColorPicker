PyQt Color Picker - Instrukcja
Wprowadzenie

Jest to rozszerzona wersja narzędzia do wybierania kolorów (Color Picker) dla PyQt6, która umożliwia użytkownikom wybór kolorów i ich wykorzystanie w różnych formatach, takich jak RGB i HEX. W tej wersji dodano kilka ulepszeń, w tym możliwość wyboru koloru i jego zastosowania za pomocą dedykowanego przycisku Take Code.
Licencja

Licencja BSD
Instalacja

    Wymagania:
        Python 3.x
        Biblioteka PyQt6 (można zainstalować przez pip install PyQt6)

    Instalacja:
        Sklonuj repozytorium lub pobierz pliki.
        Upewnij się, że wszystkie niezbędne zależności są zainstalowane.

    Katalogi:
        Color Picker oczekuje, że wszystkie potrzebne pliki będą znajdować się w tym samym katalogu, co skrypt pyqtpicker.py. Obejmuje to również plik stylów colorPickerStylesheet.css.

Użytkowanie
Integracja Color Pickera w projekcie

Poniżej znajduje się pełny przykład pokazujący, jak zintegrować Color Picker w projekcie PyQt. Przykład zawiera przycisk do otwierania Color Pickera oraz przycisk Take Code do zastosowania wybranego koloru.
Pełny przykład:

python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from pyqtpicker import ColorPicker

class ThemeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Konfiguracja głównego okna
        self.setWindowTitle("Theme Editor")
        self.setGeometry(100, 100, 400, 200)

        # Tworzenie układu
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Przycisk do otwierania Color Pickera
        self.choose_color_button = QPushButton("Choose Color", self)
        self.choose_color_button.clicked.connect(self.open_color_picker)
        self.layout.addWidget(self.choose_color_button)

        # Przycisk do przejęcia wybranego koloru
        self.take_color_button = QPushButton("Take Color Code", self)
        self.take_color_button.clicked.connect(lambda: self.take_color_code("Primary Color"))
        self.layout.addWidget(self.take_color_button)

        # Miejsce na Color Picker
        self.active_color_picker = None
        self.settings_widgets = {
            "Primary Color": self.choose_color_button
        }
        self.theme = {}

    def open_color_picker(self, setting=None):
        try:
            script_directory = os.path.dirname(os.path.realpath(__file__))

            # Inicjalizacja Color Pickera
            self.active_color_picker = ColorPicker(width=250, startupcolor=[0, 255, 255])

            # Zastosowanie stylu
            stylesheet_path = os.path.join(script_directory, 'colorPickerStylesheet.css')
            self.active_color_picker.setStyleSheet(open(stylesheet_path).read())

            # Wyświetlenie Color Pickera
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

Wyjaśnienie:

    Przycisk do otwierania Color Pickera:
        Przycisk Choose Color otwiera Color Picker po kliknięciu.

    Przycisk do przejęcia wybranego koloru:
        Przycisk Take Color Code przejmuje wybrany kolor i aktualizuje odpowiednie ustawienie.

    Integracja:
        Color Picker jest zintegrowany z projektem PyQt i wywoływany za pomocą metody open_color_picker. Wybrany kod koloru jest stosowany za pomocą metody take_color_code.

    Styl:
        Styl jest ładowany z pliku colorPickerStylesheet.css, który musi znajdować się w tym samym katalogu co skrypt pyqtpicker.py.

Uwagi

    Zdarzenie textChanged dla QLabel zostało usunięte, ponieważ QLabel nie obsługuje tego sygnału. Zamiast tego kod koloru jest stosowany za pomocą przycisku Take Code.
    Wszystkie ścieżki są rozwiązywane względem katalogu, w którym znajduje się pyqtpicker.py, co eliminuje konieczność używania globalnego katalogu roboczego.
