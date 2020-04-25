from PyQt4 import QtGui, QtCore
import colorsys
import inspect
import math
import os
import sys


class defaultColors(QtGui.QWidget):
    def __init__(self, colorpickerWidget, parent=None):
        super(defaultColors, self).__init__(parent)
        self.layout = QtGui.QVBoxLayout(self)
        row0 = QtGui.QHBoxLayout()
        row1 = QtGui.QHBoxLayout()

        self.layout.addLayout(row0)
        self.layout.addSpacing(5)
        self.layout.addLayout(row1)

        row0_number_of_colors = 6
        row1_number_of_colors = 5
        self.spaceBetweenButtons = 10

        self.buttonsWidht = colorpickerWidget.width / row0_number_of_colors - self.spaceBetweenButtons
        self.spaceForSeconfRow = self.buttonsWidht / 2
        self.buttonsWidht = str(self.buttonsWidht)
        self.buttonsHeight = str(self.buttonsWidht)
        self.buttonsRadius = str(5)
        self.buttonsHoverColor = str("#1dafaf")

        self.setStyleSheet(
            "QPushButton:hover{border: 2px solid %s;} QPushButton{border: 0px solid black; max-width: %s; max-height: %s; min-width: %s; min-height: %s; border-radius: %s;}" % (
                self.buttonsHoverColor, self.buttonsWidht, self.buttonsHeight, self.buttonsWidht, self.buttonsHeight,
                self.buttonsRadius))

        red = QtGui.QPushButton()
        red.setToolTip("Red")
        red.setStyleSheet("QPushButton{background-color: rgb(255,0,0); }")
        red.clicked.connect(lambda: colorpickerWidget.setColor(0))  # HSV

        green = QtGui.QPushButton()
        green.setToolTip("Green")
        green.setStyleSheet("QPushButton{background-color: rgb(0,255,0); }")
        green.clicked.connect(lambda: colorpickerWidget.setColor(120))  # HSV

        blue = QtGui.QPushButton()
        blue.setToolTip("Blue")
        blue.setStyleSheet("QPushButton{background-color: rgb(0,0,255); }")
        blue.clicked.connect(lambda: colorpickerWidget.setColor(240))  # HSV

        aqua = QtGui.QPushButton()
        aqua.setToolTip("Aqua")
        aqua.setStyleSheet("QPushButton{background-color: rgb(0,255,255); }")
        aqua.clicked.connect(lambda: colorpickerWidget.setColor(180))  # HSV

        tomato = QtGui.QPushButton()
        tomato.setToolTip("Tomato")
        tomato.setStyleSheet("QPushButton{background-color: rgb(255, 99, 71); }")
        tomato.clicked.connect(lambda: colorpickerWidget.setColor(9))  # HSV

        yellow = QtGui.QPushButton()
        yellow.setToolTip("Yellow")
        yellow.setStyleSheet("QPushButton{background-color: rgb(255, 255, 0); }")
        yellow.clicked.connect(lambda: colorpickerWidget.setColor(60))  # HSV

        blueviolet = QtGui.QPushButton()
        blueviolet.setToolTip("BlueViolet")
        blueviolet.setStyleSheet("QPushButton{background-color: rgb(138, 43, 226); }")
        blueviolet.clicked.connect(lambda: colorpickerWidget.setColor(271))  # HSV

        violet = QtGui.QPushButton()
        violet.setToolTip("Violet")
        violet.setStyleSheet("QPushButton{background-color: rgb(255, 0, 255); }")
        violet.clicked.connect(lambda: colorpickerWidget.setColor(300))  # HSV

        orange = QtGui.QPushButton()
        orange.setToolTip("Orange")
        orange.setStyleSheet("QPushButton{background-color: rgb(255, 165, 0); }")
        orange.clicked.connect(lambda: colorpickerWidget.setColor(39))  # HSV

        orangered = QtGui.QPushButton()
        orangered.setToolTip("OrangeRed")
        orangered.setStyleSheet("QPushButton{background-color: rgb(255, 68, 0); }")
        orangered.clicked.connect(lambda: colorpickerWidget.setColor(16))  # HSV

        lightgreen = QtGui.QPushButton()
        lightgreen.setToolTip("Lightgreen")
        lightgreen.setStyleSheet("QPushButton{background-color: rgb(0, 255, 157); }")
        lightgreen.clicked.connect(lambda: colorpickerWidget.setColor(157))  # HSV

        row0.addWidget(red)
        row0.addWidget(green)
        row0.addWidget(blue)
        row0.addWidget(yellow)
        row0.addWidget(aqua)
        row0.addWidget(violet)

        # space_for_secondRow = QtGui.QWidget()
        row1.addSpacing(self.spaceForSeconfRow)
        row1.addWidget(orange)
        row1.addWidget(lightgreen)
        row1.addWidget(blueviolet)
        row1.addWidget(tomato)
        row1.addWidget(orangered)
        row1.addSpacing(self.spaceForSeconfRow)


class colorpicker_sliders(QtGui.QWidget):
    def __init__(self, slidersWidgetWidth, spaceBetweenColorpickerAndSliders, spaceBetweenSliders, parent=None):
        super(colorpicker_sliders, self).__init__(parent)

        self.width = slidersWidgetWidth
        self.setFixedWidth(self.width)

        self.spaceBetweenColorpickerAndSliders = spaceBetweenColorpickerAndSliders
        self.spaceBetweenSliders = spaceBetweenSliders

        self.brightnessSlider = QtGui.QSlider(1)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(255)
        self.brightnessSlider.setTickInterval(1)
        self.brightnessSlider.setSingleStep(1)
        self.brightnessSlider.setToolTip("Brightness")

        self.brightness_icon = QtGui.QPushButton()
        self.brightness_icon.setObjectName("brightness_icon")
        self.brightness_icon.setToolTip("Brightness")

        self.saturationSlider = QtGui.QSlider(1)
        self.saturationSlider.setObjectName("saturationSlider")
        self.saturationSlider.setMinimum(0)
        self.saturationSlider.setMaximum(255)
        self.saturationSlider.setTickInterval(1)
        self.saturationSlider.setSingleStep(1)
        self.saturationSlider.setToolTip("Saturation")

        self.saturation_icon = QtGui.QPushButton()
        self.saturation_icon.setToolTip("Saturation")
        self.saturation_icon.setObjectName("saturation_icon")

        # ------Layout------
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addSpacing(self.spaceBetweenColorpickerAndSliders)

        self.brightnessSliderLayout = QtGui.QHBoxLayout()
        self.brightnessSliderLayout.addWidget(self.brightnessSlider)
        self.brightnessSliderLayout.addWidget(self.brightness_icon)
        self.layout.addLayout(self.brightnessSliderLayout)

        self.layout.addSpacing(self.spaceBetweenSliders)

        self.saturationSliderLayout = QtGui.QHBoxLayout()
        self.saturationSliderLayout.addWidget(self.saturationSlider)
        self.saturationSliderLayout.addWidget(self.saturation_icon)
        self.layout.addLayout(self.saturationSliderLayout)

        self.layout.addStretch()
        # /-/-/-Layout-\-\-\


class colorpickerWheel(QtGui.QWidget):
    def __init__(self, colorpickerSize, startupcolor, mouseDot_size, mouseDotDistance_changer, centralColorWidget_size,
                 centralColorWidget_radius, centerColorWidget_isCircle, sliders, parent=None):
        super(colorpickerWheel, self).__init__(parent)

        self.width = colorpickerSize
        self.height = colorpickerSize
        self.centerx = self.width / 2
        self.centery = self.height / 2
        self.mouseDot_size = mouseDot_size
        self.mouseDotDistance_changer = mouseDotDistance_changer
        self.centerColorwidth = centralColorWidget_size
        self.centerColorheight = centralColorWidget_size
        self.centerColorWidget_is_Circle = centerColorWidget_isCircle

        self.sliders = sliders

        stack = inspect.stack()
        self.class_that_called = stack[1][0].f_locals["self"].__class__
        self.class_that_called_name = stack[1][0].f_locals["self"].__class__.__name__
        # gets the class from which the colorpicker was called to call the function onCurrentColorChanged

        self.colorPickerHueWheelImage = QtGui.QPixmap(r'%s\colorpicker_wheel.png' % working_directory)
        self.colorPickerHueWheelImage = self.colorPickerHueWheelImage.scaled(self.width, self.height,
                                                                             QtCore.Qt.KeepAspectRatio,
                                                                             QtCore.Qt.SmoothTransformation)
        self.colorPickerHueWheelImageWdiget = QtGui.QLabel()
        self.colorPickerHueWheelImageWdiget.setPixmap(self.colorPickerHueWheelImage)
        self.colorPickerHueWheelImageWdiget.setFixedSize(self.width, self.height)

        self.centerColorWidget = QtGui.QLabel(parent=self.colorPickerHueWheelImageWdiget)
        self.centerColorWidget.setFixedSize(self.centerColorwidth, self.centerColorheight)
        self.centerColorWidget.move(int(self.width / 2 - self.centerColorWidget.width() / 2),
                                    int(self.height / 2 - self.centerColorWidget.height() / 2))
        if self.centerColorWidget_is_Circle:
            self.centerColorWidgetRadius = int(self.centerColorWidget.width() / 2)
        else:
            self.centerColorWidgetRadius = centralColorWidget_radius
        self.centerColorWidget.setStyleSheet(
            "QLabel{background-color: #ff0000; border-radius: %s; border}" % str(self.centerColorWidgetRadius))

        self.mouseDot = QtGui.QLabel(parent=self.colorPickerHueWheelImageWdiget)
        self.mouseDot.setFixedSize(self.mouseDot_size, self.mouseDot_size)
        self.mouseDotRadius = str(int(self.mouseDot.width() / 2))
        self.mouseDot.setStyleSheet(
            "QLabel{background-color: rgba(0,0,0,0); border-radius: %s}" % self.mouseDotRadius)
        self.mouseDot.setObjectName("mouseDot")

        # ------Layout------
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.colorPickerHueWheelImageWdiget)
        # /-/-/-Layout-\-\-\

        # sliders change events
        self.sliders.brightnessSlider.valueChanged.connect(lambda: self.setValue(self.sliders.brightnessSlider.value()))
        self.sliders.saturationSlider.valueChanged.connect(
            lambda: self.setSaturation(self.sliders.saturationSlider.value()))

        self.setStartupColor(startupcolor)

    def hsv2rgb(self, h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

    def setStartupColor(self, startupcolor):
        self.startupColor = [0, 0, 0]  # declaration
        self.startupColor[0] = round(startupcolor[0] / 360 * 255)
        self.startupColor[1] = startupcolor[1]
        self.startupColor[2] = startupcolor[2]
        self.HSV_color = self.startupColor
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base = [round(self.HSV_color[0] / 255 * 360), round(self.HSV_color[1] / 255 * 100),
                                         round(self.HSV_color[2] / 255 * 100)]  # (H(0-255), S(0-255), V(0-255))
        self.setMouseDotPositionFromHue(self.HSV_color[0])
        self.change_centerColor(self.rgb_color, self.HSV_color[2])
        self.changeMouseDotColor(self.HSV_color[0])
        self.change_sliderColor(self.HSV_color)
        # sliders set startup value
        self.sliders.brightnessSlider.setValue(self.startupColor[1])
        self.sliders.saturationSlider.setValue(self.startupColor[2])
        self.currentColorChanged()

    def setValue(self, val):
        self.HSV_color[2] = val
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base[2] = round(self.HSV_color[2] / 255 * 100)
        self.change_centerColorHueValue(self.rgb_color, self.HSV_color[2])
        self.currentColorChanged()

    def setSaturation(self, sat):
        self.HSV_color[1] = sat
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base[1] = round(self.HSV_color[1] / 255 * 100)
        self.change_centerColorHueSaturation(self.rgb_color, self.HSV_color[2])
        self.currentColorChanged()

    def mousePressEvent(self, QMouseEvent):
        y = QMouseEvent.y() - self.height / 2
        x = QMouseEvent.x() - self.width / 2
        if y == 0:
            tangente = 0
        else:
            tangente = x / y
        current_angle = math.degrees(math.atan(tangente))
        # print(x, y, round(tangente), current_angle)
        if x >= 0 >= y:
            angle = -round(current_angle)
        if x >= 0 <= y:
            angle = 180 - round(current_angle)
        if x <= 0 <= y:
            angle = 180 - round(current_angle)
        if x <= 0 >= y:
            angle = 360 - round(current_angle)
        # print(angle)
        self.hue = angle / 360 * 255
        if self.hue == 255:
            self.hue = 0
        # print(self.hue)
        self.HSV_color[0] = round(self.hue)
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base = [round(self.HSV_color[0] / 255 * 360), round(self.HSV_color[1] / 255 * 100),
                                         round(self.HSV_color[2] / 255 * 100)]  # (H(0-255), S(0-255), V(0-255))
        rgb_color_for_central_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255,
                                                   self.HSV_color[2] / 255)

        self.change_centerColor(rgb_color_for_central_color, self.HSV_color[2])
        self.changeMouseDotColor(self.HSV_color[0])
        self.change_sliderColor(self.HSV_color)
        self.movePointer(x, y)
        self.currentColorChanged()

    def mouseMoveEvent(self, QMouseEvent):
        y = QMouseEvent.y() - self.height / 2
        x = QMouseEvent.x() - self.width / 2
        if y == 0 and x < 0:
            angle = 270
        elif y == 0 and x > 0:
            angle = 90
        else:
            tangente = x / y
            current_angle = math.degrees(math.atan(tangente))
            if x >= 0 >= y:
                angle = -round(current_angle)
            if x >= 0 <= y:
                angle = 180 - round(current_angle)
            if x <= 0 <= y:
                angle = 180 - round(current_angle)
            if x <= 0 >= y:
                angle = 360 - round(current_angle)

        self.hue = angle / 360 * 255
        if self.hue == 255:
            self.hue = 0
        # print(self.hue)
        self.HSV_color[0] = round(self.hue)
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base = [round(self.HSV_color[0] / 255 * 360), round(self.HSV_color[1] / 255 * 100),
                                         round(self.HSV_color[2] / 255 * 100)]  # (H(0-255), S(0-255), V(0-255))
        rgb_color_for_central_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255,
                                                   self.HSV_color[2] / 255)

        self.change_centerColor(rgb_color_for_central_color, self.HSV_color[2])
        self.changeMouseDotColor(self.HSV_color[0])
        self.change_sliderColor(self.HSV_color)
        self.movePointer(x, y)
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.currentColorChanged()

    def change_centerColor(self, color, value):
        rgba_color = (str(color)).replace(")", ", ") + str(value) + ")"
        self.centerColorWidget.setStyleSheet(
            "QLabel{background-color: rgba%s; border-radius:%s;}" % (rgba_color, str(self.centerColorWidgetRadius)))

    def change_centerColorHueValue(self, color, value):
        rgba_color = (str(color)).replace(")", ", ") + str(value) + ")"
        self.centerColorWidget.setStyleSheet(
            "QLabel{background-color: rgba%s; border-radius:%s;}" % (rgba_color, str(self.centerColorWidgetRadius)))

    def change_centerColorHueSaturation(self, color, value):
        rgba_color = (str(color)).replace(")", ", ") + str(value) + ")"
        self.centerColorWidget.setStyleSheet(
            "QLabel{background-color: rgba%s; border-radius:%s;}" % (rgba_color, str(self.centerColorWidgetRadius)))

    def changeMouseDotColor(self, hue):
        self.mouseDot.setStyleSheet("QLabel{background-color: hsv(%s, 255, 255); border-radius:%s;}" % (
            str(hue / 255 * 360), self.mouseDotRadius))

    def change_sliderColor(self, color):
        self.sliders.setStyleSheet(
            "QSlider#brightnessSlider::groove:horizontal{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, x3:2, y3:0, stop:0 hsv(%s, 100, 100),  stop:1 hsv(%s,255,255));}"
            "QSlider#saturationSlider::groove:horizontal{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, x3:2, y3:0, stop:0 hsv(%s, 0, 200), stop:1 hsv(%s,255,255));}" % (
                str(color[0] / 255 * 360), str(color[0] / 255 * 360), str(color[0] / 255 * 360),
                str(color[0] / 255 * 360)))

    def movePointer(self, x, y):
        radius = self.height / 2 - self.mouseDot.height() / 2 + self.mouseDotDistance_changer
        if y == 0 and x < 0:
            angle = 270
            angle_in_radians = math.radians(angle)
            change_in_y = math.cos(angle_in_radians) * radius
            change_in_x = math.sin(angle_in_radians) * radius
        elif y == 0 and x > 0:
            angle = 90
            angle_in_radians = math.radians(angle)
            change_in_y = math.cos(angle_in_radians) * radius
            change_in_x = math.sin(angle_in_radians) * radius
        else:
            tangente = x / y
            current_angle = math.degrees(math.atan(tangente))
            if x >= 0 >= y:
                angle = -round(current_angle)
                angle_in_radians = math.radians(angle)
                change_in_y = math.cos(angle_in_radians) * radius
                change_in_x = math.sin(angle_in_radians) * radius
            if x >= 0 and y >= 0:
                angle = 180 - round(current_angle)
                angle_in_radians = math.radians(angle)
                change_in_y = math.cos(angle_in_radians) * radius
                change_in_x = math.sin(angle_in_radians) * radius
            if x <= 0 and y >= 0:
                angle = 180 - round(current_angle)
                angle_in_radians = math.radians(angle)
                change_in_y = math.cos(angle_in_radians) * radius
                change_in_x = math.sin(angle_in_radians) * radius
            if x <= 0 and y <= 0:
                angle = 360 - round(current_angle)
                angle_in_radians = math.radians(angle)
                change_in_y = math.cos(angle_in_radians) * radius
                change_in_x = math.sin(angle_in_radians) * radius

        self.mouseDot.move(self.centerx + change_in_x - self.mouseDot.width() / 2,
                           self.centery - change_in_y - self.mouseDot.height() / 2)

    def setColor(self, color):
        self.HSV_color[0] = round(color / 360 * 255)
        self.HSV_color[1] = 255
        self.HSV_color[2] = 255
        self.rgb_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255, self.HSV_color[2] / 255)
        self.hsv_color_array_360_base = [round(self.HSV_color[0] / 255 * 360), round(self.HSV_color[1] / 255 * 100),
                                         round(self.HSV_color[2] / 255 * 100)]  # (H(0-255), S(0-255), V(0-255))
        rgb_color_for_central_color = self.hsv2rgb(self.HSV_color[0] / 255, self.HSV_color[1] / 255,
                                                   self.HSV_color[2] / 255)
        self.change_centerColor(rgb_color_for_central_color, self.HSV_color[2])
        self.changeMouseDotColor(self.HSV_color[0])
        self.change_sliderColor(self.HSV_color)
        self.setMouseDotPositionFromHue(self.HSV_color[0])
        self.sliders.brightnessSlider.setValue(self.HSV_color[1])
        self.sliders.saturationSlider.setValue(self.HSV_color[2])
        self.currentColorChanged()

    def setMouseDotPositionFromHue(self, hue):
        radius = self.height / 2 - self.mouseDot.height() / 2 + self.mouseDotDistance_changer
        angle = hue * 360 / 255
        angle_in_radians = math.radians(angle)
        change_in_y = math.cos(angle_in_radians) * radius
        change_in_x = math.sin(angle_in_radians) * radius
        self.mouseDot.move(self.centerx + change_in_x - self.mouseDot.width() / 2,
                           self.centery - change_in_y - self.mouseDot.height() / 2)

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


class ColorPicker(QtGui.QWidget):
    def __init__(self, width, startupcolor, parent=None):
        super(ColorPicker, self).__init__(parent)
        self.width = width
        self.startup_color = startupcolor  # HSV (0-360, 0-255, 0-255)
        self.setStyleSheet(open(r'%s\colorPickerStylesheet.css' % working_directory).read())

        ColorPicker.hsv_color_array = 0
        ColorPicker.rgb_color_array = 0
        ColorPicker.hsv_color_array_base_360 = 0

        # self.sliders = colorpicker_sliders(slidersWidgetWidth (recommended same as colorpicker width "self.width"), spaceBetweenColorpickerAndSliders, spaceBetweenSliders)
        self.sliders = colorpicker_sliders(slidersWidgetWidth=self.width, spaceBetweenColorpickerAndSliders=0,
                                           spaceBetweenSliders=0)

        # colorpicker_test_class(int colorpickerSize, startup_color[h(0-360), s(0-255), v(0-255)], int mouseDot_size, int mouseDotDistance_changer, int centralColorWidget_size, int centralColor_radius, bool centerColorWidget_isCircle if True makes the centralcolorWidegt a circle else uses the radius, self.sliders //default do not remove)
        self.colorpickerWidget = colorpickerWheel(colorpickerSize=self.width, startupcolor=self.startup_color,
                                                  mouseDot_size=30, mouseDotDistance_changer=2,
                                                  centralColorWidget_size=55, centralColorWidget_radius=20,
                                                  centerColorWidget_isCircle=True, sliders=self.sliders)

        self.colorpickerWidget.setFixedSize(self.colorpickerWidget.width, self.colorpickerWidget.height)  # do not forget to set a fixed size same as the size when initialising the class/otherwise set layouts with stretches.

        self.defaultColors = defaultColors(self.colorpickerWidget)
        self.defaultColors.setFixedWidth(self.colorpickerWidget.width)  # do not forget to set a fixed size same as the size when initialising the class/otherwise set layouts with stretches.

        # ------Layout------
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.colorpickerWidget)
        self.layout.addWidget(self.sliders)
        self.layout.addWidget(self.defaultColors)
        self.layout.addStretch(1)
        # /-/-/-Layout-\-\-\

        self.show()

    def onCurrentColorChanged(color):
        # this function is called every time the color changes
        ColorPicker.hsv_color_array = color[0]  # (H(0-255), S(0-255), V(0-255))
        ColorPicker.rgb_color_array = color[1]  # (R(0-255), G(0-255), B(0-255))
        ColorPicker.hsv_color_array_base_360 = color[2]  # (H(0-360), S(0-100), V(0-100))
        # print("HSV color", ColorPicker.hsv_color_array)
        # print(ColorPicker.hsv_color_array_360_base)
        # print("RGB color", ColorPicker.rgb_color_array)


def run():
    app = QtGui.QApplication(sys.argv)
    global working_directory
    working_directory = os.path.dirname(os.path.realpath(__file__)) #directory where files are placed in this case same as the executable directory
    Colorpicker = ColorPicker(width=250, startupcolor=[0, 255, 255])  # HSV (0-360, 0-255, 0-255)
    # check the ColorPicker to change more values

    # You can get the updated values outside the class using an other event like this
    # print(ColorPicker.hsv_color_array)

    sys.exit(app.exec_())

run()
