from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider


class ColorPickerSliders(QWidget):
    def __init__(self, width, parent=None):
        super(ColorPickerSliders, self).__init__(parent)
        self.width = width
        self.setFixedWidth(self.width)

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

        self.brightnessSliderLayout = QHBoxLayout()
        self.brightnessSliderLayout.addWidget(self.brightnessSlider)
        self.brightnessSliderLayout.addWidget(self.brightness_icon)
        self.layout.addLayout(self.brightnessSliderLayout)

        self.saturationSliderLayout = QHBoxLayout()
        self.saturationSliderLayout.addWidget(self.saturationSlider)
        self.saturationSliderLayout.addWidget(self.saturation_icon)
        self.layout.addLayout(self.saturationSliderLayout)

        self.layout.addStretch()
        # /-/-/-Layout-\-\-
