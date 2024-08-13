from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider
from PyQt6.QtGui import QPixmap, QFont, QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QPoint
import colorsys
import math
import os
import sys

class defaultColors(QWidget):
    def __init__(self, colorpickerWidget, parent=None):
        super(defaultColors, self).__init__(parent)
        self.layout = QHBoxLayout(self)

        self.colors = {
            "Red": (0, "rgb(255,0,0)"),
            "Green": (120, "rgb(0,255,0)"),
            "Blue": (240, "rgb(0,0,255)"),
            "Yellow": (60, "rgb(255,255,0)"),
            "Aqua": (180, "rgb(0,255,255)"),
            "Magenta": (300, "rgb(255,0,255)"),
            "Orange": (30, "rgb(255,165,0)"),
            "Purple": (270, "rgb(128,0,128)"),
        }

        for name, (hue, color) in self.colors.items():
            button = QPushButton()
            button.setToolTip(name)
            button.setStyleSheet(f"QPushButton{{background-color: {color}; }}")
            button.clicked.connect(lambda _, h=hue: colorpickerWidget.setColor(h))
            self.layout.addWidget(button)

class colorpicker_sliders(QWidget):
    def __init__(self, slidersWidgetWidth, spaceBetweenColorpickerAndSliders, spaceBetweenSliders, parent=None):
        super(colorpicker_sliders, self).__init__(parent)

        self.width = slidersWidgetWidth
        self.setFixedWidth(self.width)

        self.spaceBetweenColorpickerAndSliders = spaceBetweenColorpickerAndSliders
        self.spaceBetweenSliders = spaceBetweenSliders

        self.brightnessSlider = QSlider(Qt.Orientation.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(255)
        self.brightnessSlider.setTickInterval(1)
        self.brightnessSlider.setSingleStep(1)
        self.brightnessSlider.setToolTip("Brightness")

        self.brightness_icon = QPushButton()
        self.brightness_icon.setObjectName("brightness_icon")
        self.brightness_icon.setToolTip("Brightness")

        self.saturationSlider = QSlider(Qt.Orientation.Horizontal)
        self.saturationSlider.setObjectName("saturationSlider")
        self.saturationSlider.setMinimum(0)
        self.saturationSlider.setMaximum(255)
        self.saturationSlider.setTickInterval(1)
        self.saturationSlider.setSingleStep(1)
        self.saturationSlider.setToolTip("Saturation")

        self.saturation_icon = QPushButton()
        self.saturation_icon.setToolTip("Saturation")
        self.saturation_icon.setObjectName("saturation_icon")

        # ------Layout------
        self.layout = QVBoxLayout(self)
        self.layout.addSpacing(self.spaceBetweenColorpickerAndSliders)

        self.brightnessSliderLayout = QHBoxLayout()
        self.brightnessSliderLayout.addWidget(self.brightnessSlider)
        self.brightnessSliderLayout.addWidget(self.brightness_icon)
        self.layout.addLayout(self.brightnessSliderLayout)

        self.layout.addSpacing(self.spaceBetweenSliders)

        self.saturationSliderLayout = QHBoxLayout()
        self.saturationSliderLayout.addWidget(self.saturationSlider)
        self.saturationSliderLayout.addWidget(self.saturation_icon)
        self.layout.addLayout(self.saturationSliderLayout)

        self.layout.addStretch()

class colorpickerWheel(QWidget):
    def __init__(self, colorpickerSize, startupcolor, mouseDot_size, mouseDotDistance_changer, centralColorWidget_size,
                 centralColorWidget_radius, centerColorWidget_isCircle, change_alpha_channel, sliders, parent=None):
        super(colorpickerWheel, self).__init__(parent)

        self.width = colorpickerSize
        self.height = colorpickerSize
        self.centerx = self.width / 2
        self.centery = self.height / 2
        self.mouseDot_size = mouseDot_size
        self.mouseDotDistance_changer = mouseDotDistance_changer
        self.centerColorwidth = int(centralColorWidget_size * 1.5)
        self.centerColorheight = int(centralColorWidget_size * 1.5)
        self.centerColorWidget_is_Circle = centerColorWidget_isCircle
        self.change_alpha_channel = change_alpha_channel

        self.sliders = sliders
        script_directory = os.path.dirname(os.path.realpath(__file__))  # <-- Hinzugefügt: Verzeichnis des Skripts

        self.colorPickerHueWheelImage_File = 'colorpicker_wheel.png'
        self.colorPickerHueWheelImage = QPixmap(
            os.path.join(script_directory, self.colorPickerHueWheelImage_File))  # <-- Geändert: Verzeichnis verwenden
        self.colorPickerHueWheelImage = self.colorPickerHueWheelImage.scaled(self.width, self.height,
                                                                             Qt.AspectRatioMode.KeepAspectRatio,
                                                                             Qt.TransformationMode.SmoothTransformation)
        self.colorPickerHueWheelImageWdiget = QLabel(self)
        self.colorPickerHueWheelImageWdiget.setPixmap(self.colorPickerHueWheelImage)
        self.colorPickerHueWheelImageWdiget.setFixedSize(self.width, self.height)


        # Create the central color display
        self.centerColorDisplay = QLabel(self.colorPickerHueWheelImageWdiget)
        self.centerColorDisplay.setFixedSize(self.centerColorwidth, self.centerColorheight)
        self.centerColorDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.centerColorDisplay.setStyleSheet(f"background-color: black; border-radius: {self.centerColorwidth // 2}px;")
        self.centerColorDisplay.move(int(self.width / 2 - self.centerColorwidth / 2),
                                     int(self.height / 2 - self.centerColorheight / 2))

        # Create the mouse dot (should be initialized before setStartupColor is called)
        self.mouseDot = QLabel(self)
        self.mouseDot.setFixedSize(self.mouseDot_size, self.mouseDot_size)
        self.mouseDotRadius = str(int(self.mouseDot.width() / 2))
        self.mouseDot.setStyleSheet(
            f"QLabel{{background-color: rgba(0,0,0,0); border-radius: {self.mouseDotRadius}px}}")
        self.mouseDot.setObjectName("mouseDot")

        # Create a QLabel for the color code below the sliders
        self.colorCodeLabel = QLabel(self)
        self.colorCodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.colorCodeLabel.setStyleSheet("color: white; background-color: black; padding: 5px;")
        font = QFont()
        font.setPointSize(10)
        self.colorCodeLabel.setFont(font)
        self.colorCodeLabel.setFixedWidth(self.width)

        # ------Layout------
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.colorPickerHueWheelImageWdiget)
        self.layout.addWidget(self.sliders)
        self.layout.addWidget(self.colorCodeLabel)  # Den Farbcode unter die Slider setzen

        # sliders change events
        self.sliders.brightnessSlider.valueChanged.connect(lambda: self.setValue(self.sliders.brightnessSlider.value()))
        self.sliders.saturationSlider.valueChanged.connect(
            lambda: self.setSaturation(self.sliders.saturationSlider.value()))

        self.setStartupColor(startupcolor)

    def setColor(self, color):
        self.HSV_color[0] = round(color / 360 * 255)
        self.HSV_color[1] = 255
        self.HSV_color[2] = 255
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base = [round(self.HSV_color[0] / 255 * 360), round(self.HSV_color[1] / 255 * 100),
                                         round(self.HSV_color[2] / 255 * 100)]
        self.changeMouseDotColor(self.HSV_color[0])
        self.change_sliderColor(self.HSV_color)
        self.setMouseDotPositionFromHue(self.HSV_color[0])
        self.sliders.brightnessSlider.setValue(self.HSV_color[1])
        self.sliders.saturationSlider.setValue(self.HSV_color[2])
        self.updateCenterColorDisplay()
        self.updateColorCode()
        self.update()

    def updateCenterColorDisplay(self):
        self.centerColorDisplay.setStyleSheet(f"background-color: rgb({self.rgb_color[0]}, {self.rgb_color[1]}, {self.rgb_color[2]}); border-radius: {self.centerColorwidth // 2}px;")
        self.centerColorDisplay.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    def hsv2rgb(self, h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

    def setStartupColor(self, startupcolor):
        self.startupColor = [0, 0, 0]  # Declaration
        self.startupColor[0] = round(startupcolor[0] / 360 * 255)
        self.startupColor[1] = startupcolor[1]
        self.startupColor[2] = startupcolor[2]
        self.HSV_color = self.startupColor
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base = [round(self.HSV_color[0] / 255 * 360), round(self.HSV_color[1] / 255 * 100),
                                         round(self.HSV_color[2] / 255 * 100)]  # (H(0-255), S(0-255), V(0-255))
        self.setMouseDotPositionFromHue(self.HSV_color[0])
        self.changeMouseDotColor(self.HSV_color[0])
        self.change_sliderColor(self.HSV_color)
        # Sliders set startup value
        self.sliders.brightnessSlider.setValue(self.startupColor[1])
        self.sliders.saturationSlider.setValue(self.startupColor[2])
        self.updateCenterColorDisplay()  # Sicherstellen, dass die zentrale Farbe korrekt gesetzt wird
        self.updateColorCode()
        self.update()

    def setValue(self, val):
        self.HSV_color[2] = val
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base[2] = round(self.HSV_color[2] / 255 * 100)
        self.updateCenterColorDisplay()
        self.updateColorCode()
        self.update()

    def setSaturation(self, sat):
        self.HSV_color[1] = sat
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base[1] = round(self.HSV_color[1] / 255 * 100)
        self.updateCenterColorDisplay()
        self.updateColorCode()
        self.update()

    def mousePressEvent(self, event):
        y = event.position().y() - self.height / 2
        x = event.position().x() - self.width / 2
        self.updateColorFromPosition(x, y)

    def mouseMoveEvent(self, event):
        y = event.position().y() - self.height / 2
        x = event.position().x() - self.width / 2
        self.updateColorFromPosition(x, y)

    def updateColorFromPosition(self, x, y):
        angle = self.calculateAngle(x, y)
        self.hue = angle / 360 * 255
        if self.hue == 255:
            self.hue = 0
        self.HSV_color[0] = round(self.hue)
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base = [round(self.HSV_color[0] / 255 * 360), round(self.HSV_color[1] / 255 * 100),
                                         round(self.HSV_color[2] / 255 * 100)]
        self.changeMouseDotColor(self.HSV_color[0])
        self.change_sliderColor(self.HSV_color)
        self.movePointer(x, y)
        self.updateCenterColorDisplay()
        self.updateColorCode()
        self.update()

    def calculateAngle(self, x, y):
        if y == 0 and x < 0:
            return 270
        elif y == 0 and x > 0:
            return 90
        elif y == x == 0:
            return 0
        else:
            tangente = x / y
            current_angle = math.degrees(math.atan(tangente))
            if x >= 0 >= y:
                return -round(current_angle)
            if x >= 0 <= y:
                return 180 - round(current_angle)
            if x <= 0 <= y:
                return 180 - round(current_angle)
            if x <= 0 >= y:
                return 360 - round(current_angle)

    def changeMouseDotColor(self, hue):
        self.mouseDot.setStyleSheet(f"QLabel{{background-color: hsv({hue / 255 * 360}, 255, 255); border-radius:{self.mouseDotRadius}px;}}")

    def change_sliderColor(self, color):
        self.sliders.setStyleSheet(
            f"QSlider#brightnessSlider::groove:horizontal{{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, x3:2, y3:0, stop:0 hsv({color[0] / 255 * 360}, 100, 100),  stop:1 hsv({color[0] / 255 * 360},255,255));}}"
            f"QSlider#saturationSlider::groove:horizontal{{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, x3:2, y3:0, stop:0 hsv({color[0] / 255 * 360}, 0, 200), stop:1 hsv({color[0] / 255 * 360},255,255));}}")

    def movePointer(self, x, y):
        radius = self.height / 2 - self.mouseDot.height() / 2 + self.mouseDotDistance_changer
        angle = self.calculateAngle(x, y)
        angle_in_radians = math.radians(angle)
        change_in_y = math.cos(angle_in_radians) * radius
        change_in_x = math.sin(angle_in_radians) * radius

        self.mouseDot.move(int(self.centerx + change_in_x - self.mouseDot.width() / 2),
                           int(self.centery - change_in_y - self.mouseDot.height() / 2))

    def setMouseDotPositionFromHue(self, hue):
        radius = self.height / 2 - self.mouseDot.height() / 2 + self.mouseDotDistance_changer
        angle = hue * 360 / 255
        angle_in_radians = math.radians(angle)
        change_in_y = math.cos(angle_in_radians) * radius
        change_in_x = math.sin(angle_in_radians) * radius
        self.mouseDot.move(int(self.centerx + change_in_x - self.mouseDot.width() / 2),
                           int(self.centery - change_in_y - self.mouseDot.height() / 2))
                       
    def updateColorCode(self):
        hex_color = '#%02x%02x%02x' % self.rgb_color
        self.colorCodeLabel.setText(hex_color.upper())
        self.update()  # This will trigger a repaint

    def currentColorChanged(self):
        try:
            self.class_that_called.onCurrentColorChanged(
                [self.HSV_color, self.rgb_color, self.hsv_color_array_360_base])
        except Exception as e:
            print("To get the color on the main class of colorpicker create this function on it: \n"
                  "def onCurrentColorChanged(color):\n"
                  "    # this function is called every time the color changes\n"
                  "    ColorPicker.hsv_color_array = color[0]  # (H(0-255), S(0-255), V(0-255))\n"
                  "    ColorPicker.rgb_color_array = color[1]  # (R(0-255), G(0-255), B(0-255))\n"
                  "    ColorPicker.hsv_color_array_base_360 = color[2]  # (H(0-360), S(0-100), V(0-100))\n"
                  "    # print(ColorPicker.hsv_color_array)\n"
                  "This lets you use the values from the class that the colorpicker was CALLED!\n", e)
        self.updateColorCode()
        self.update()

class ColorPicker(QWidget):
    def __init__(self, width, startupcolor, parent=None):
        super(ColorPicker, self).__init__(parent)
        self.width = width
        self.startup_color = startupcolor  # HSV (0-360, 0-255, 0-255)

        script_directory = os.path.dirname(os.path.realpath(__file__))
        self.styleSheet_File = 'colorPickerStylesheet.css'
        self.setStyleSheet(open(os.path.join(script_directory, self.styleSheet_File)).read())

        ColorPicker.hsv_color_array = 0
        ColorPicker.rgb_color_array = 0
        ColorPicker.hsv_color_array_base_360 = 0
        ColorPicker.hex_color = 0

        self.sliders = colorpicker_sliders(slidersWidgetWidth=self.width, spaceBetweenColorpickerAndSliders=0,
                                           spaceBetweenSliders=0)

        self.colorpickerWidget = colorpickerWheel(colorpickerSize=self.width, startupcolor=self.startup_color,
                                                  mouseDot_size=30, mouseDotDistance_changer=2,
                                                  centralColorWidget_size=120, centralColorWidget_radius=60,
                                                  centerColorWidget_isCircle=True, change_alpha_channel=False,
                                                  sliders=self.sliders)

        self.colorpickerWidget.setFixedSize(self.colorpickerWidget.width, self.colorpickerWidget.height)
        self.defaultColors = defaultColors(self.colorpickerWidget)
        self.defaultColors.setFixedWidth(self.colorpickerWidget.width)
        self.colorCodeLabel = self.colorpickerWidget.colorCodeLabel

        # ------Layout------
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.colorpickerWidget)
        self.layout.addWidget(self.sliders)
        self.layout.addWidget(self.colorCodeLabel)  # Farbcode unter die Schieberegler setzen
        self.layout.addWidget(self.defaultColors)
        self.layout.addStretch(1)
        # /-/-/-Layout-\-\-\

        self.show()

    def onCurrentColorChanged(self, color):
        # this function is called every time the color changes
        ColorPicker.hsv_color_array = color[0]  # (H(0-255), S(0-255), V(0-255))
        ColorPicker.rgb_color_array = color[1]  # (R(0-255), G(0-255), B(0-255))
        ColorPicker.hsv_color_array_base_360 = color[2]  # (H(0-360), S(0-100), V(0-100))
        ColorPicker.hex_color = '%02x%02x%02x' % ColorPicker.rgb_color_array
        # print("HSV color", ColorPicker.hsv_color_array)
        # print(ColorPicker.hsv_color_array_base_360)
        # print("RGB color", ColorPicker.rgb_color_array)
        # print("HEX Color", ColorPicker.hex_color)

def run():
    app = QApplication(sys.argv)
    Colorpicker = ColorPicker(width=250, startupcolor=[0, 255, 255])  # HSV (0-360, 0-255, 0-255)
    sys.exit(app.exec())
        #2024 V040 ITCRW 

if __name__ == "__main__":
    run()
