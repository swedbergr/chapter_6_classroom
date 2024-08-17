# Import math module
import math

def area(width, length):
  ''' 
  This function takes a length and a width of a rectangle and 
  returns the area.
  param width: int or float for the width of the rectangle
  param length: int or  float for the length of the rectangle
  return: float for the area
  '''
  return width * length

def perimeter(width, length):
  '''
  This function takes a length and a width of a rectanlge and 
  returns the area.
  param width: int or float for the width of the rectangle
  param length: int or float for the length of the rectangle
  return: float for the perimeter
  '''
  return 2 * (width + length)