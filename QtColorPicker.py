import colorsys
import math
import os
from typing import Callable

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor, QMouseEvent
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from ColorPickerSliders import ColorPickerSliders
from DefaultColorsWidget import DefaultColorsWidget


def calculate_angle(x: float, y: float) -> int:
    if y == 0 and x < 0:
        return 270
    elif y == 0 and x > 0:
        return 90
    elif y == x == 0:
        return 0
    else:
        tan = x / y
        angle = math.degrees(math.atan(tan))
        if x >= 0 >= y:
            return -round(angle)
        elif x >= 0 <= y:
            return 180 - round(angle)
        elif x <= 0 <= y:
            return 180 - round(angle)
        elif x <= 0 >= y:
            return 360 - round(angle)
        return 0


def hex_to_hue(hex_color: str) -> int:
    color = QColor(hex_color)
    r, g, b = color.red(), color.green(), color.blue()
    hue, _, _, _ = QColor(r, g, b).getHsvF()
    hue_degrees = hue * 360
    return int(hue_degrees)


class ColorCircle(QWidget):
    def __init__(self,
                 size: int,
                 listener: Callable[[int], None],
                 pointer_distance_correction: int = 2,
                 parent: QWidget = None):
        super(ColorCircle, self).__init__(parent)

        self.listener = listener
        self.pointer_distance_correction = pointer_distance_correction

        self.center_x = size / 2
        self.center_y = size / 2

        # Load and scale color picker wheel image
        self.wheel_image = QPixmap(os.path.join(os.path.dirname(__file__), 'colorpicker_wheel.png'))
        self.wheel_image = self.wheel_image.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio,
                                                   Qt.TransformationMode.SmoothTransformation)
        self.wheel_image_widget = QLabel()
        self.wheel_image_widget.setPixmap(self.wheel_image)
        self.wheel_image_widget.setFixedSize(size, size)

        # Central color widget
        self.central_color_widget = QLabel(parent=self.wheel_image_widget)
        self.central_color_widget.setFixedSize(55, 55)
        self.central_color_widget.move(int(self.center_x - self.central_color_widget.width() / 2),
                                       int(self.center_y - self.central_color_widget.height() / 2))
        self.central_color_widget_radius = int(self.central_color_widget.width() / 2)

        # Color picker pointer
        self.pointer = QLabel(parent=self.wheel_image_widget)
        self.pointer.setFixedSize(30, 30)
        self.pointer_radius = str(int(self.pointer.width() / 2))
        self.pointer.setObjectName("pointer")

        # Layout configuration
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.wheel_image_widget)

    def mousePressEvent(self, q_mouse_press_event: QMouseEvent):
        self.mouseMoveEvent(q_mouse_press_event)

    def mouseMoveEvent(self, q_mouse_move_event: QMouseEvent):
        mouse_position = q_mouse_move_event.position()
        x = mouse_position.x() - self.center_x
        y = mouse_position.y() - self.center_y
        angle = calculate_angle(x, y)
        self.listener(angle)

    def set_pointer_position_from_hue(self, hue: float):
        """ :param hue: Hue in degrees (0-360). """
        angle_in_radians = math.radians(hue)
        pointer_distance = self.center_x - self.pointer.size().width() / 2 + self.pointer_distance_correction
        change_in_y = math.cos(angle_in_radians) * pointer_distance
        change_in_x = math.sin(angle_in_radians) * pointer_distance
        self.pointer.move(int(self.center_x + change_in_x - self.pointer.width() / 2),
                          int(self.center_y - change_in_y - self.pointer.height() / 2))


class QtColorPicker(QWidget):
    def __init__(self,
                 size: int = 250,
                 startup_color: list[int] = (360, 255, 255),
                 pointer_distance_correction: int = 2,
                 change_central_color_widget_brightness: bool = True,
                 listener: Callable[[int, int, int], None] = None,
                 parent: QWidget = None):
        super(QtColorPicker, self).__init__(parent)

        self.hue = None
        self.saturation = None
        self.brightness = None
        self.listener = listener
        self.pointer_distance_correction = pointer_distance_correction
        self.change_central_color_widget_brightness = change_central_color_widget_brightness

        # Load css
        self.setStyleSheet(open(os.path.join(os.path.dirname(__file__), 'colorPickerStylesheet.css')).read())

        # ColorCircle
        self.colorCircle = ColorCircle(size, self.set_hue)
        # Sliders
        self.sliders = ColorPickerSliders(size)
        self.sliders.saturationSlider.valueChanged.connect(
            lambda: self.set_saturation(self.sliders.saturationSlider.value()))
        self.sliders.brightnessSlider.valueChanged.connect(
            lambda: self.set_brightness(self.sliders.brightnessSlider.value()))
        # DefaultColors
        self.defaultColors = DefaultColorsWidget(size, self.set_color_hex)

        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.colorCircle)
        self.layout.addWidget(self.sliders)
        self.layout.addWidget(self.defaultColors)
        self.layout.addStretch(1)

        self.set_color(startup_color[0], startup_color[1], startup_color[2])

    def set_color_hex(self, hex_color: str, saturation: int, brightness: int):
        hue = hex_to_hue(hex_color)
        self.set_color(hue, saturation, brightness)

    def set_hue(self, value):
        self.set_color(hue=value, saturation=self.saturation, brightness=self.brightness)

    def set_saturation(self, value):
        self.set_color(hue=self.hue, saturation=value, brightness=self.brightness)

    def set_brightness(self, value):
        self.set_color(hue=self.hue, saturation=self.saturation, brightness=value)

    def set_color(self, hue: int, saturation: int, brightness: int):
        if hue == 360:
            hue = 0
        self.hue = hue
        self.brightness = brightness
        self.saturation = saturation
        self.set_css(hue, saturation, brightness)
        self.colorCircle.set_pointer_position_from_hue(hue)
        self.sliders.brightnessSlider.setValue(brightness)
        self.sliders.saturationSlider.setValue(saturation)
        if self.listener is not None:
            self.listener(self.hue, self.saturation, self.brightness)

    def set_css(self, hue: int, saturation: int, brightness: int):
        if not self.change_central_color_widget_brightness:
            brightness = 255
        self.colorCircle.central_color_widget.setStyleSheet(
            f"QLabel{{background-color: hsv({hue}, {saturation}, {brightness}); border-radius:{self.colorCircle.central_color_widget_radius};}}")

        self.colorCircle.pointer.setStyleSheet(
            f"QLabel{{background-color: hsv({hue}, 255, 255); border-radius:{self.colorCircle.pointer_radius};}}")

        self.sliders.setStyleSheet(
            f"QSlider#brightnessSlider::groove:horizontal{{background-color: qlineargradient(spread:pad, x1:0, y1:0, "
            f"x2:1, y2:0, stop:0 hsv({hue}, 100, 100), stop:1 hsv({hue}, 255, 255));}}"
            f"QSlider#saturationSlider::groove:horizontal{{background-color: qlineargradient(spread:pad, x1:0, y1:0, "
            f"x2:1, y2:0, stop:0 hsv({hue}, 0, 200), stop:1 hsv({hue}, 255, 255));}}")

    def get_hsv(self):
        return [self.hue, self.saturation, self.brightness]

    def get_hue(self):
        return self.hue

    def get_saturation(self):
        return self.saturation

    def get_brightness(self):
        return self.brightness

    def get_rgb(self):
        r, g, b = colorsys.hsv_to_rgb(self.get_hue() / 360.0, self.get_saturation() / 255.0,
                                      self.get_brightness() / 255.0)
        # Scale the values to 0-255
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        return r, g, b

    def get_default_colors_widget(self):
        return self.defaultColors

    def get_sliders(self):
        return self.sliders

    def get_pointer(self):
        return self.colorCircle.pointer

    def get_wheel_image_widget(self):
        return self.colorCircle.wheel_image_widget

    def get_central_color_widget(self):
        return self.colorCircle.central_color_widget
