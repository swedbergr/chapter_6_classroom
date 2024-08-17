# Get functions from modules
import circle
import rectangle

# Constants for menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CIRCLE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
  '''
  Main function for execution of geometry formulas through menu.
  '''
  choice = 0
  while choice != QUIT_CHOICE:
    # Display menu
    display_menu()

    # Get user's choice
    choice = int(validate_num(input(), 5))

    if choice == AREA_CIRCLE_CHOICE:
      # Get radius
      radius = float(validate_num(input("Enter the radius: ")))
      print(circle.area(radius))

    elif choice == CIRCUMFERENCE_CIRCLE_CHOICE:
      # Get radius
      radius = float(validate_num(input("Enter the radius: ")))
      print(circle.circumference(radius))

    elif choice == AREA_RECTANGLE_CHOICE:
      # Get width and length
      width = float(validate_num(input("Enter the width: ")))
      length = float(validate_num(input("Enter the width: ")))
      print(rectangle.area(width, length))

    elif choice == PERIMETER_RECTANGLE_CHOICE:
      # Get width and length
      width = float(validate_num(input("Enter the width: ")))
      length = float(validate_num(input("Enter the width: ")))
      print(rectangle.perimeter(width, length))

    else:
      print("Exiting the program.")


def display_menu():
  '''
  Function displays the main menu 
  '''
  print("MENU")
  print("1. Area of a circle")
  print("2. Circumference of a circle")
  print("3. Area of a rectangle")
  print("4. Perimeter of a rectangle")
  print("5. Quit")
  print("Please select the number of what you would like to do.")


def validate_num(message, min=-1*2**31, max=2**31):
    '''
    Function determines if string is able to be cast to int or float.
    It also checks if it fits within a range.
    param message: string for the input function prompt
    param min: default of lowest possible int or minimum value posibility
    param max: default of highest possible int or maximum value posibility
    return: data that can be cast to int or float
    '''
    # Loop for bad input
    while True:
      # Get user input
      user_input = input(message)
      improved_input = user_input.replace(",", "").replace(" ", "")

      # Check to make sure no bad characters
      if len(improved_input) == 1:
        if not improved_input.isdigit():
          print("Please only input a number.")
          continue
      elif improved_input[0] == ".":
        if not improved_input[1:].replace(",", "").isdigit():
          print("Please only input a number.")
          continue
      elif not improved_input[1:].replace(".", "", 1).replace(",", "").isdigit() or \
        not (improved_input[0] == "-" or improved_input[0].isdigit()):
        print("Please only input a number.")
        continue

      # Check input with range
      if float(improved_input) < min or float(improved_input) > max:
        print("That number is not in the range.")
        print(f"Please select a number between {min} and {max}.")
        continue

      # Return
      return float(improved_input)


# Execute main if executing this module
if __name__ == "__main__":
  main()