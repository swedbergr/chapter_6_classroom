# Import library
import os


def main():
  print("This program allows a user to manage student records.")
  print("Each record consists of a student's first name, last name, and grade.")
  while True:
    print("What would you like to do?")
    print("Type the number for one of the following:\n",
         "1. Add records\n",
         "2. Display records\n",
         "3. Search for a specific record\n",
         "4. Modify records\n",
         "5. Delete records\n",
         "6. Exit")
    choice = input()
    if choice == "1":
      add_record()
    elif choice == "2":
      display_record()
    elif choice == "3":
      search_record()
    elif choice == "4":
      modify_record()
    elif choice == "5":
      delete_record()
    elif choice == "6":
      break
    else:
      print("That is not a valid option. Please try again.")



def add_record():
  '''
  Void function gets records from user and appends them to a file.
  '''
  # Create sentinel for loop
  more = "y"
  # Open a file
  with open("students.txt", "a") as outfile:
    # Loop for every user input
    while more == "y" or more == "Y":
      # Get fields from user
      first = input("First name: ")
      last = input("Last name: ")
      grade = input("Grade: ")

      # Write record to file
      outfile.write(first + "\n" + last + "\n" + grade + "\n")

      # Update the sentinel
      more = input("Would you like to add another record? (y or n) ")




def display_record():
  '''
  Void function displays all the records in a file.
  '''
  # Open file to read
  with open("students.txt", "r") as infile:
    # Read first line for priming read
    data = infile.readline()
    counter = 1
    # Iterate for every record
    while data != "":
      first = data.rstrip("\n")
      last = infile.readline().rstrip("\n")
      grade = infile.readline().rstrip("\n")
      # Display 
      print(f"Student number {counter} {first} {last} in grade {grade}")

      # Update counter
      counter += 1

      # Read next line to check for end of file
      data = infile.readline()




def search_record():
  '''
  Void function searches for a specific record in the file.
  '''
  # Prompt user for search
  search = input("What would you like to search for? ")

  # Open file
  with open("students.txt", "r") as infile:
    # Create flag
    found = False
    # Get data in first line for priming read
    data = infile.readline()
    # Itereate through every record until finding searched item
    while not found and data != "":
      # Assign first field from record
      first = data.rstrip("\n")
      # Get and assign second field from record
      last = infile.readline().rstrip("\n")
      # Get and assign last field from record
      grade = infile.readline().rstrip("\n")

      # Check whole record for search data
      if search == first or search == last or search == grade:
        print("A record was found!")
        print(f"First name: {first}")
        print(f"Last name: {last}")
        print(f"Grade: {grade}")
        # Check if the user wants to continue the search
        more = input("Would you like to continue the search for more records? (y or n)")
        if not (more == "y") and not (more == "Y"):
          found = True
          break

      # Get next line
      data = infile.readline()

    if not found:
      print(f"{search} was not found.")





def modify_record():
  '''
  Void function modifies a specific record in the file.
  '''
  # Prompt user for search
  search = input("What would you like to modify? ")

  # Open file
  with open("students.txt", "r") as infile, \
  open("temp.txt", "a") as outfile:
    # Create flag
    found = False
    # Get data in first line for priming read
    data = infile.readline()
    # Itereate through every record until finding searched item
    while data != "":
      # Assign first field from record
      first = data.rstrip("\n")
      # Get and assign second field from record
      last = infile.readline().rstrip("\n")
      # Get and assign last field from record
      grade = infile.readline().rstrip("\n")

      # Check whole record for search data
      if search == first or search == last or search == grade:
        print("A record was found!")
        print(f"First name: {first}")
        print(f"Last name: {last}")
        print(f"Grade: {grade}")
        # Check if the user wants to continue the search
        more = input("Is this the record you want to modify? (y or n)")
        if more == "y" or more == "Y":
          # Get a replacement field
          replace = input(f"What would you like to replace {search} with?")
          if first == search:
            first = replace
          elif last == search:
            last = replace
          else:
            grade = replace

          # Update the flag
          found = True

      # Write to outfile
      outfile.write(first + "\n" + last + "\n" + grade + "\n")

      # Get next line
      data = infile.readline()

    if found:
      print(f"{search} was modified successfully!")
    else:
      print(f"{search} was not found.")
    
  # Remove old file
  os.remove("students.txt")
  # Rename new file
  os.rename("temp.txt", "students.txt")




def delete_record():
  '''
  Void function deletes a specific record in the file.
  '''
  # Prompt user for search
  search = input("Enter a field from the record that you like to delete? ")

  # Open file
  with open("students.txt", "r") as infile, \
  open("temp.txt", "a") as outfile:
    # Create flag
    found = False
    skip = False
    # Get data in first line for priming read
    data = infile.readline()
    # Itereate through every record until finding searched item
    while data != "":
      # Assign first field from record
      first = data.rstrip("\n")
      # Get and assign second field from record
      last = infile.readline().rstrip("\n")
      # Get and assign last field from record
      grade = infile.readline().rstrip("\n")

      # Check whole record for search data
      if search == first or search == last or search == grade:
        print("A record was found!")
        print(f"First name: {first}")
        print(f"Last name: {last}")
        print(f"Grade: {grade}")
        # Check if the user wants to continue the search
        more = input("Is this the record you want to delete? (y or n)")
        if more == "y" or more == "Y":
          # Update the flag
          found = True
          skip = True

      if not found or not skip:
        # Write to outfile
        outfile.write(first + "\n" + last + "\n" + grade + "\n")
      skip = False

      # Get next line
      data = infile.readline()

    if found:
      print(f"{search} was deleted successfully!")
    else:
      print(f"{search} was not found.")

  # Remove old file
  os.remove("students.txt")
  # Rename new file
  os.rename("temp.txt", "students.txt")




if __name__ == "__main__":
  main()