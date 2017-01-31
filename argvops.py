"""
File: argvops.py
Author: Gerard Geer
Purpose:
	Defines a quick set of operations to perform on command line arguments.
	Features:
		filenames anywhere in the list except after parameters.
		Allows for both parameters and options.
	
"""
import os

def getFilenames(argv):
	"""
	Takes the argv list, and returns a new list containing just input
	filenames.
	
	Parameters:
		argv ([Str]): List of command line arguments.
		
	Returns:
		A new list of filenames.
	"""
	filenames = []
	filenames = argv[1:]
	
	# Prepend every argument after an option flag ('-') with a hyphen.
	for i in range(len(filenames)-1, -1, -1):
		if filenames[i].startswith('-') and i < len(filenames)-1: 
			filenames[i+1] = '-'+filenames[i+1]
	
	# Return all elements that don't have a hyphen.
	return [x for x in filenames if not x.startswith('-')]
	
def checkParam(parameter, argv):
	"""
	Checks the arg list for a parameter flag, and if it exists
	returns its value.
	
	Parameters:
		parameter(str): The parameter flag to check, with punctuation.
		argv([str]): The arguments list.
	
	Returns:
		The value of the parameter, if it exists.
	"""
	
	# Try to find the argument in the  list.
	for i in range(len(argv)):
	
		# Since we need to check the element *after* the option,
		# we need to make sure that it's not the last element.
		if argv[i] == parameter and i < len(argv) -1:
			# Make sure it's not another parameter.
			if argv[i+1].startswith('-'): return None
			else: return argv[i+1]
			
	# If we didn't find it, we return an easily detectable value.
	return None
	
def checkOption(option, argv):
	"""
	Checks the arglist for the existence of an option flag.
	
	Parameters:
		option(str): The option to check for.
		argv([str]): The arguments list.
		
	Returns:
		Whether or not the argument is in the list.
	"""
	return option in argv
	
def printProgressBar(title, width, percent):
	"""
	A quick and janky commandline progress bar. Updates in-situ, and
	uses sub-block characters for smoothing.
	
	Example:
	"Progress: [████████████████▌           ] 55%"
	"""
	# If we're on windows, the empty chars need to be two spaces.
	space = ""
	if(os.name == 'nt'): space = "  "
	else: space = " "	
	
	# Get the number of full blocks
	blocks = int(width*percent)
	
	# Get the fractional amount of block right at the edge.
	fractblock = width*percent-blocks
	
	# The smallest fractional block is at 0x285f, so we subtract from
	# that our fractional amount, now stretched out over 8 integer
	# values.
	fractchar = chr(0x258f-int(fractblock*8))
	
	# Extra spaces after the progress bar.
	notblocks = int(width-blocks)-1
	
	# Print the bar itself. First we print a carriage return to start
	# over at the beginning of the line, then the title, then the
	# opening bracket, then the full and fractional blocks, then the
	# empty region, then the percent sign. We finish it off with an
	# optional parameter to not append a newline to the output.
	print("\r"+title+"["+"\u2588"*blocks+fractchar+space*notblocks+"] "	\
	          +str(int(percent*101))+"%", end='')
