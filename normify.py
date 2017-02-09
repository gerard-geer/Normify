"""
File: normify.py
Author: Gerard Geer
Purpose:
	This program converts any number of images into normal maps.
	
	Usage: filename [...additional filenames] [-p pixelop=lum] [-w] [-o outfile]
	Parameters:
	  -p = operation used to get a 1-d value per pixel.
	  -o = output filename. Will always be saved as .PNG, mind you.
	Options:
	  -w = If no output filename is specified, this flag symbolizes to overwrite
	       rather than append '_n' to the original filename.
	
"""
import sys
from os import path
from PIL import Image
from vec3 import *
from pxops import *
from argvops import *

def getPx(px, u, v, size):
	"""
	Gets a pixel from the 1D pixel list, with wrapping.
	
	Parameters:
		px([]): The 1D list containing all the pixels.
		u: The x coordinate to sample.
		v: The y coordinate to sample.
		size((int)): A tuple containing the width and height of the
		image.
		
	Returns:
		The pixel.
	"""
	return px[ size[1]*( v % size[0]) + (u % size[1]) ]
	
def getPartialDerivatives(px, u, v, op, size):
	"""
	Returns the partial derivatives of the image at the given pixel
	coordinate.

	Parameters:
		px ([]): A 1D list of pixel values from the original image.
		uv (integer tuple): A tuple containing two zero-indexed 
			values for sampling.
		op (value function): The operation to be used to get a value
			from a pixel.
		size((int)): A tuple containing the width and height of the
		image.
			
	Returns:
		a tuple of two vec3s, each containing the partial derivative
		along its
		axis.
	"""
	dy = ( op(getPx(px,u,v,size))*.01 - op(getPx(px,u,v-1,size))*.01 )
	dx = ( op(getPx(px,u,v,size))*.01 - op(getPx(px,u-1,v,size))*.01 )
	
	return ( vec3(1.0, dx, 0), vec3(0, dy, 1.0) )
	
def calcNormal(dx, dy):
	"""
	Returns a surface normal given two partial derivates.
	
	Parameters:
		dx(vec3): Partial directional derivative in the x-axis.
		dy(vec3): Partial directional derivative in the y-axis.
		
	Returns:
		The surface normal at the given point.
	"""
	return cross(dy,dx).normalize()
	
def convert(px, op, size):
	"""
	Converts each pixel in the image to a surface normal in tehe form
	of a vec3 instance.
	
	Parameters:
		px([]): A 1D list of the pixel data from the image.
		op(function(pixel)): The operation to use to get a value for
		each pixel.
		size((int)): A tuple containing the width and height of the
		image.
	Returns:
		A new 2D array of vec3s.
	"""
	# Create the new image, putting vec3 instances in each pixel.
	normalMap = Image.new("RGB", size)
	npx = normalMap.load()
	for u in range(size[0]):
		printProgressBar("Progress: ",30,u/size[0])
		for v in range(size[1]):
			d = getPartialDerivatives(px, u, v, op, size)
			n = calcNormal(d[0],d[1])
			n.x = (n.x+1.0)*127.5
			n.y = (n.y+1.0)*127.5
			n.z = (n.z+1.0)*127.5
			npx[u,v] = (int(n.x),int(n.z),int(n.y))
			
	return normalMap

def convertImage(argv, filename):
	"""
	Converts and saves an image given the command line arguments and
	a filename.
	
	Parameters:
	argv([str]): The command line args.
	filename(str): The filename of the current image.
	
	Returns:
		None.
	
	Postconditions:
		A new file is saved.
	"""
	# Get the specified pixel op.
	op = getOp(checkParam('-p', argv))
	
	# Get the output filename.
	outfile = checkParam('-o', argv)
	if outfile ==  None:
		if checkOption('-w',sys.argv):
			outfile = path.splitext(filename)[0]+".png"
		else:
			outfile = path.splitext(filename)[0]+"_n.png"
	
	# Before we do anything, let's print out some info.
	print("\n\nImage:    "+filename)
	print("Method:   "+op.__name__) # That's dirty.
	print("Outfile:  "+outfile)
	# Get the filename and open the file.
	img = None
	try:
		img = Image.open(filename)
		px  = list(img.getdata())
	except:
		print("Error: could not open image: "+sys.argv[1])
		sys.exit(1)
	
	# Actually do the conversion.
	normalMap = convert(px, op, img.size)
	
	# Save the normal map.
	normalMap.save(outfile, "PNG")
	
def main():
	"""
	The main function of normify.
	
	Parameters:
		None.
	
	Returns:
		0 if successful, error otherwise.
	"""
	# If a filename wasn't specified, we print usage and exit.
	if len(sys.argv) < 2:
		print("Normify: Converts any number of images into normal maps.")
		print("Usage: filename [...additional filenames] [-p pixelop=lum] [-w] [-o outfile]")
		print("Parameters:")
		print("  -p = operation used to get a 1-d value per pixel.")
		print("  -o = output filename. Will always be saved as .PNG, mind you.")
		print("Options:")
		print("  -w = If no output filename is specified, this flag symbolizes to overwrite")
		print("       rather than append '_n' to the original filename.")
		sys.exit(0)
	
	# Get all the filenames out of the command line args.
	filenames = getFilenames(sys.argv)
	
	# Print some info.
	print("Converting "+str(len(filenames))+" image"+"s"*int(len(filenames)>1.0)+"...", end='')
	
	# Go through and convert all the images.
	for filename in filenames:
		convertImage(sys.argv, filename)
	
if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
