try:
  x = 10
  y = 0
  z = x / y
except IOError:
  print("This code caused an IOError.")
except ValueError:
  print("This code caused a ValueError.")
except:
  print("Error")
else:
  print(z)
