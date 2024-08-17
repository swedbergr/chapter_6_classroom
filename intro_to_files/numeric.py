def main():
  # Set up menu
  while True:
    print("This program allows you to record transations and display a current balance.")
    print("Enter the number of the option you would like to do:")
    print("1. Add transations\n2. Display balance\n3. Create ints\n4. Quit")
    user_choice = input()
    if user_choice == "1":
      transaction = float(validate_num("Please enter the amount: "))
      # Send transaction to be added to file
      write_value(transaction)
    elif user_choice == "2":
      # Get balance from file
      balance = get_balance()
      print(f"The balance is ${balance:.2f}.")
    elif user_choice == "3":
      convert()
    elif user_choice == "4":
      break
    else:
      print("That is not a valid option. Please try again.")



def get_balance():
  '''
  Function reads a file and adds every amount in the file
  return: float for the sum of all the values in a file
  '''
  # Set accumulator
  balance = 0
  
  # Open file
  with open("num_file.txt", "r") as file:
    # Read every line in file individually and add to accumulator
    for value in file:
      balance += float(value)

  # Return balance
  return balance
  


def write_value(value):
  '''
  Void function takes an int or float and writes it to a file.
  param value: int or float of value to be writen in file
  '''
  # Open, append, and close file
  with open("num_file.txt", "a") as file:
    file.write(str(value) + "\n")


def convert():
  '''
  Void function opens a file, converts all strings to 
  floats, then to ints, then back to strings for a new
  file.
  '''
  # Set up files to read and write
  with open("num_file.txt", "r") as infile, \
  open("int_file.txt", "a") as outfile:
    for value in infile:
      temp = float(value)
      outfile.write(str(int(temp)) + "\n")


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
    improved_input = user_input.replace(",", "").replace(" ", "").replace("$", "", 1)

    # Check to make sure no bad characters
    if len(improved_input) == 1:
      if not improved_input.isdigit():
        print("Please only input a number.")
        continue
    elif improved_input[0] == ".":
      if not improved_input[1:].isdigit():
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

if __name__ == "__main__":
  main()