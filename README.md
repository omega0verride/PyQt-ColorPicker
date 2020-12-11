# PyQt-ColorPicker
Circular ColorPicker for PyQt Python.

This is a new design PyQt ColorPicker for python.

![](/demo/colorpicker_run.PNG)

The color circle is actually an image and the hue values are generated from finding the tangent of the distance of the mouse coordinates + center coordinates only within the colorpickerWheel class.


Make sure that all the files are  in the same directory with the executable/script or change the "working_directory" variable.

Call the ColorPicker class like this (change the variables)
	
	Colorpicker = ColorPicker(width=250, startupcolor=[0, 255, 255])  # HSV (0-360, 0-255, 0-255)
	
The colorcycle calls the function "onCurrentColorChanged" in "ColorPicker" class when the color changes. There it returns 3 arrays
        
	hsv_color_array = color[0]  # (H(0-255), S(0-255), V(0-255))
	hsv_color_array_base_360 = color[2]  # (H(0-360), S(0-100), V(0-100))
	rgb_color_array = color[1]  # (R(0-255), G(0-255), B(0-255))
	
If you need to use HSV with other values like (H(0-1), S(0-1), V(0-1)) use a conversion like
	
	hsv_color_array_base_1 = [hsv_color_array[0]/255, hsv_color_array[1]/255, hsv_color_array[2]/255]
	
If you change the width the mouseDot might seem a bit off, this can be fixed on the colorpickerWheel class initiation

  Values that can be changed:
  	
	self.sliders = colorpicker_sliders(slidersWidgetWidth=self.width, spaceBetweenColorpickerAndSliders=0,
                                           spaceBetweenSliders=0)
	
	####
	#"colorpicker_sliders" class must be initiated before "colorpickerWheel" class because it is passed to "colorpickerWheel"
	####
	
	self.colorpickerWidget = colorpickerWheel(colorpickerSize=self.width, startupcolor=self.startup_color,
                                                  mouseDot_size=30, mouseDotDistance_changer=2,
                                                  centralColorWidget_size=55, centralColorWidget_radius=20,
                                                  centerColorWidget_isCircle=True, sliders=self.sliders)
	
	colorpickerSize=self.width	   by default is inherited when you initialize the ColorPicker class
	startupcolor=self.startup_color    by default is inherited when you initialize the ColorPicker class
	mouseDot_size=30		   changes the size of the mouse circle that moves around the circle
	mouseDotDistance_changer=2	   changes the distance of mouseFot from the center
	centralColorWidget_size=55	   changes the size of the color widget inside the circle
	centralColorWidget_radius=20	   changes the border-radius of the color widget inside the circle
	centerColorWidget_isCircle=True    if True sets the central color widget as a circle and ignores the value of centralColorWidget_radius
	change_alpha_channel=True          if True changes the central color widget alpha channel (opacity) based on the value of brightness slider
	sliders=self.sliders		   is default, do not remove unless you remove all functoions associated with sliders
	
You can get the updated values outside the class like this
	
	print(ColorPicker.hsv_color_array)
		
Notice - If you use this as a widget set oboject names for QPushButtons and QSliders of parent because it affects the child widget.

