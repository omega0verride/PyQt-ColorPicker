from typing import Callable

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton


class DefaultColorsWidget(QWidget):
    def __init__(self, width: int, action: Callable[[str, int, int], None], parent=None):
        super(DefaultColorsWidget, self).__init__(parent)
        self.action = action

        self.items_per_row = 6
        self.space_between_buttons = 10
        self.buttons_radius = 5
        self.buttons_hover_color = "#1dafaf"
        self.buttons_width = width / self.items_per_row - self.space_between_buttons
        self.setFixedWidth(width + self.space_between_buttons * 2)

        self.layout = QVBoxLayout(self)
        self.row0 = QHBoxLayout()
        self.row1 = QHBoxLayout()

        self.layout.addLayout(self.row0)
        self.layout.addSpacing(5)
        self.layout.addLayout(self.row1)

        self.setStyleSheet(
            f"QPushButton:hover{{border: 2px solid {self.buttons_hover_color};}} "
            f"QPushButton{{border: 0px solid black; max-width: {self.buttons_width}px; max-height: {self.buttons_width}px; "
            f"min-width: {self.buttons_width}px; min-height: {self.buttons_width}px; border-radius: {self.buttons_radius}px;}}"
        )

        colors = [
            ("Red", "#FF0000", 255, 255),
            ("Green", "#00FF00", 255, 255),
            ("Blue", "#0000FF", 255, 255),
            ("Yellow", "#FFFF00", 255, 255),
            ("Aqua", "#00FFFF", 255, 255),
            ("Violet", "#FF00FF", 255, 255),
            ("Orange", "#FFA500", 255, 255),
            ("LightGreen", "#00FF9D", 255, 255),
            ("BlueViolet", "#8A2BE2", 255, 255),
            ("Tomato", "#FF6347", 255, 255),
            ("OrangeRed", "#FF4400", 255, 255),
        ]

        # First row buttons
        for color_name, hex_value, saturation, brightness in colors[:6]:
            self.add_button(self.row0, color_name, hex_value, saturation, brightness)

        # Second row buttons
        self.row1.addSpacing(int(self.buttons_width / 2))  # extra space since this row has 1 less item
        for color_name, hex_value, saturation, brightness in colors[6:]:
            self.add_button(self.row1, color_name, hex_value, saturation, brightness)
        self.row1.addSpacing(int(self.buttons_width / 2))  # extra space since this row has 1 less item

    def add_button(self, layout: QHBoxLayout, color_name: str, hex_value: str, saturation: int, brightness: int):
        button = QPushButton()
        button.setToolTip(color_name)
        button.setStyleSheet(f"QPushButton{{background-color: {hex_value};}}")
        button.clicked.connect(lambda: self.action(hex_value, saturation, brightness))
        layout.addWidget(button)
