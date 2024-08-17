def main():
  # Determine what the user wants to do
  menu = "y"
  while menu == "y":
    print("You can write, read, or append to a file. Which wich would you like to do?")
    menu_choice = input()
    if menu_choice == "read":
      read_file()
    elif menu_choice == "write":
      write_file()
    elif menu_choice == "append":
      append_file()
    else:
      print("That is not an option.")

    # Determine if the user wants to exit the program
    menu = input("Would you like to continue running the program? Type y for yes.\n")

def write_file():
  '''
  Void function gets values from user and writes them to a file.
  '''
  # Get input from user to add to file
  done = "n"
  data = ""
  while done != "y":
    data = data + input("What would you like to add to the file?\n")
    data = data + "\n"
    done = input("Are you done adding to the file? Type y for yes.\n")

  # Open, write to file, and close
  file = open("main_file.txt", "w")
  file.write(data)
  file.close()

def read_file():
  '''
  Void function reads data from a file and displays it.
  '''
  # Open, print, and close file
  file = open("main_file.txt", "r")
  data = file.read()
  file.close()

  # Display file data
  print(data)

def append_file():
  '''
  Void function that gets user input to append to file.
  '''
  # Open file
  file = open("main_file.txt", "a")
  
  # Get input from user to append to the file
  done = "n"
  while done != "y":
    data = input("What would you like to add to the file?\n")
    file.write(data)
    done = input("Are you done adding to the file? Type y for yes.\n")

  # Close the file
  file.close()
  
if __name__ == "__main__":
  main()