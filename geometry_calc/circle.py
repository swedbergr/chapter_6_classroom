# Import math module
import math

def main():
  pass

def area(radius):
  '''
  The area function takes a radius, computes the area, and returns the area
  param radius: float or int value for radius
  return: float value that represents the area of a circle
  '''
  return math.pi * radius ** 2

def circumference(radius):
  '''
  The circumference function takes a radius, computes the circumference, and returns
  the circumference.
  param radius: float or int value for radius
  return: float value that represents the circumference of a circle
  '''
  return math.pi * radius * 2

if __name__ == "__main__":
  main()