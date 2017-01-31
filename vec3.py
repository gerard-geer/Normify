"""
File: vec3.py
Author: Gerard Geer
Purpose: Implements the minimum necessary functionality to compute surface
	     normals from two orthagonal surface tangents.
"""

import math
"""
This class represents a 3D vector. It implements the minimum amount of
functionality required to do normal creation. (Normalization and cross
product.)
"""
class vec3(object):
	__self__ = ('x','y','z')
		
	def __init__(self):
		self.x = 0;
		self.y = 0;
		self.z = 0;
	
	def __init__(self, v):
		self.x = v;
		self.y = v;
		self.z = v;
	
	def __init__(self, x, y, z):
		self.x = x;
		self.y = y;
		self.z = z;
		
	def normalize(self):
		length = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		self.x /= length;
		self.y /= length;
		self.z /= length;
		return self
	
def cross(u, v):
	"""
	Computes the cross product of two vec3s, and returns the result as
	a new vector.
	
	Parameters:
		u(vec3): The first of the two vectors to cross.
		v(vec3): The second of the two vectors to cross.
		
	Returns:
		The cross product of u and v.
	"""
	return vec3( u.y*v.z - u.z*v.y,	\
				 u.z*v.x - u.x*v.z, \
				 u.x*v.y - u.y*v.x);