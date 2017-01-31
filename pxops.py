"""
File: pxops.py
Author: Gerard Geer
Purpose: Defines several operations to get a single value from the three color
		 channels of a pixel.
"""
				 
def luminance(p):
	"""
	Computes the luminance of the given pixel according to ITU BT.601.
	
	Parameters:
		p (pixel): The pixel to operate on.
	
	Returns:
		The luminance of the pixel.
	"""
	return 0.299*p[0] + 0.587*p[1] + 0.114*p[2]
	
def grayscale(p):
	"""
	Computes the grayscale (channel average) value of the given pixel.
	
	Parameters:
		p (pixel): The pixel to operate on.
	
	Returns:
		The grayscale value of the pixel.
	"""
	return p[0] + p[1] + p[2] / 3.0
	
def sum(p):
	"""
	Computes the sum of the color channels. Allows for a bit greater
	accuracy.
	
	Parameters:
		p (pixel): The pixel to operate on.
	
	Returns:
		The channel sum of the pixel.
	"""
	return p[0] + p[1] + p[2]
	
def red(p):
	"""
	Returns the red value of the given pixel.
	
	Parameters:
		p (pixel): The pixel to operate on.
	
	Returns:
		The red channel value of the pixel.
	"""
	
def green(p):
	"""
	Returns the green value of the given pixel.
	
	Parameters:
		p (pixel): The pixel to operate on.
	
	Returns:
		The green channel value of the given pixel.
	"""
	
def blue(p):
	"""
	Returns the blue value of the given pixel.
	
	Parameters:
		p (pixel): The pixel to operate on.
	
	Returns:
		The blue channel value of the given pixel.
	"""
	return p[0]
	
def getOp(o):
	"""
	Given an option, returns the correct pixel operation.
	
	Parameters:
		o (Str): The value of the operation option.
		
	Returns:
		The function corresponding to the option.
	"""
	if o == "l" or o == "lum" or o == "luminance": return luminance
	elif o == "gs" or o == "gray" or o == "grayscale": return grayscale
	elif o == "avg" or o == "grey" or o == "greyscale": return grayscale
	elif o == "s" or o == "sum" or o == "total": return sum
	elif o == "r" or o == "red" or o == "x": return red
	elif o == "g" or o == "green" or o == "y": return green
	elif o == "b" or o == "blue" or o == "z": return blue
	else: return luminance
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	