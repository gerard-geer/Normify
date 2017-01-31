# Normify
---------
Converts any number of images to normal maps, with options!
-----------------------------------------------------------
I made this to automate converting outputted bump-maps to normal maps.

## Usage
--------
`normify.py filename [...more filenames] [-p pixel conversion method] [-o outfile] [-w]`

Where:
* `filename [...more filenames]` are the image files you want to convert. They don't have to appear before the parameters/options.
* `-p` Specifies a method to project pixel values from 3D (R,G,B) to 1D. Available options are (default is luminance):
  * `l | lum | luminance`: ITU BT.601 luminance.
  * `gs | avg | gray | grey | grayscale | greyscale`: Channel average. (R+G+B/3)
  * `m | mag | magnitude`: Channel magnitude √(R<sup>2</sup>+G<sup>2</sup>+B<sup>2</sup>)
  * `s | sum | total`: Sum of the color channels. (R+G+B)
  * `r | red | x`: Use only the red channel.
  * `g | green | y`: Use only the green channel.
  * `b | blue | z`: Use only the blue channel.
* `-o` Specifies output files. Multiple output files is not yet supported.
* '-w' When no output file is supported, this tells the program to overwrite the input file. The default behavior is to append "_n" to the filename.

## Dependencies
---------------
*Pillow* _The Python Image Library_: Install using `pip install pillow` Don't forget to run that with administrative privleges.
