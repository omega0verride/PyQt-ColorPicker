PyQt Color Picker - Instructions
Introduction

Il s'agit d'une version améliorée d'un sélecteur de couleurs (Color Picker) pour PyQt6, permettant aux utilisateurs de sélectionner des couleurs et de les utiliser dans différents formats tels que RGB et HEX. Cette version inclut des améliorations, telles que la possibilité de sélectionner une couleur et de l'appliquer à l'aide d'un bouton dédié Take Code.
Licence

Licence BSD
Installation

    Prérequis :
        Python 3.x
        Bibliothèque PyQt6 (installable via pip install PyQt6)

    Installation :
        Clonez le dépôt ou téléchargez les fichiers.
        Assurez-vous que toutes les dépendances nécessaires sont installées.

    Répertoires :
        Le Color Picker attend que tous les fichiers nécessaires soient dans le même répertoire que le script pyqtpicker.py. Cela inclut également le fichier de style colorPickerStylesheet.css.

Utilisation
Intégration du Color Picker dans un projet

Voici un exemple complet montrant comment intégrer le Color Picker dans votre projet PyQt. Cet exemple inclut un bouton pour ouvrir le Color Picker et un bouton Take Code pour appliquer la couleur sélectionnée.
Exemple complet :

python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from pyqtpicker import ColorPicker

class ThemeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.setWindowTitle("Theme Editor")
        self.setGeometry(100, 100, 400, 200)

        # Création du layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Bouton pour ouvrir le Color Picker
        self.choose_color_button = QPushButton("Choose Color", self)
        self.choose_color_button.clicked.connect(self.open_color_picker)
        self.layout.addWidget(self.choose_color_button)

        # Bouton pour appliquer la couleur sélectionnée
        self.take_color_button = QPushButton("Take Color Code", self)
        self.take_color_button.clicked.connect(lambda: self.take_color_code("Primary Color"))
        self.layout.addWidget(self.take_color_button)

        # Placeholder pour le Color Picker
        self.active_color_picker = None
        self.settings_widgets = {
            "Primary Color": self.choose_color_button
        }
        self.theme = {}

    def open_color_picker(self, setting=None):
        try:
            script_directory = os.path.dirname(os.path.realpath(__file__))

            # Initialisation du Color Picker
            self.active_color_picker = ColorPicker(width=250, startupcolor=[0, 255, 255])

            # Application de la feuille de style
            stylesheet_path = os.path.join(script_directory, 'colorPickerStylesheet.css')
            self.active_color_picker.setStyleSheet(open(stylesheet_path).read())

            # Affichage du Color Picker
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

Explication :

    Bouton pour ouvrir le Color Picker :
        Le bouton Choose Color ouvre le Color Picker lorsqu'il est cliqué.

    Bouton pour appliquer la couleur sélectionnée :
        Le bouton Take Color Code applique la couleur sélectionnée et met à jour le paramètre correspondant.

    Intégration :
        Le Color Picker est intégré dans le projet PyQt et est appelé via la méthode open_color_picker. Le code de la couleur sélectionnée est appliqué via la méthode take_color_code.

    Feuille de style :
        La feuille de style est chargée à partir du fichier colorPickerStylesheet.css, qui doit se trouver dans le même répertoire que le script pyqtpicker.py.

Remarques

    L'événement textChanged pour QLabel a été supprimé car QLabel ne prend pas en charge ce signal. À la place, le code de la couleur est appliqué via le bouton Take Code.
    Tous les chemins sont résolus par rapport au répertoire où se trouve pyqtpicker.py, ce qui rend inutile l'utilisation d'un répertoire de travail global.

Cet exemple fournit une implémentation complète qui inclut à la fois l'ouverture du Color Picker et l'application de la couleur sélectionnée.

