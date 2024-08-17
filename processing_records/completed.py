# Import libraries
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
  # Set sentinel
  more = "y"
  #Open file
  with open("students.txt", "a") as outfile:
    # Get whole record data for a student from the user
    while more == "y" or more == "Y":
      print("Enter the student's information.")
      first = input("First name: ")
      last = input("Last name: ")
      grade = input("Grade: ")
      # Add record to file
      outfile.write(first + "\n" + last + "\n" + grade + "\n")

      # Update sentinel
      more = input("Do you want to add another student? Type y for yes.")




def display_record():
  '''
  Void function displays all the records in a file.
  '''
  # Open file
  with open("students.txt", "r") as infile:
    # Get first line in priming read
    data = infile.readline()
    # Read each line if file
    while data != "":
      # User first field in record
      first = data.rstrip("\n")
      # Get and use second field in record
      last = infile.readline().rstrip("\n")
      # Get and use the third field in record
      grade = infile.readline().rstrip("\n")
      # Display record
      print(f"First name: {first}")
      print(f"Last name: {last}")
      print(f"Grade: {grade}")

      # Chech next line for more data
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
  # Get what user wants to be searched
  search = input("What would you like to search and replace? ")

  # Open file and create a temp file to copy records
  with open("students.txt", "r") as infile, \
  open("temp.txt", "a") as outfile:
    # Create flag
    found = False
    # Get data in first line for priming read
    data = infile.readline()
    # Itereate through every record intil finding searched item
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
        found = input(f"Is this the record in which you want to replace {search}? (y or n)")
        if found == "y" or found == "Y":
          # Update flag
          found = True
          # Get replacement
          replace = input(f"What would you like to replace {search} with? ")
          # Change field in record
          if search == first:
            first = replace
          elif search == last:
            last = replace
          else:
            grade = replace

      # Write whole record to temp file
      outfile.write(first + "\n" + last + "\n" + grade + "\n")

      # Get next line
      data = infile.readline()

  # Update user on success
  if found:
    print("The record has been updated.")
  else:
    print(f"{search} was never found.")

  # Delete old students.txt
  os.remove("students.txt")
  # Rename temp file to replace students.txt
  os.rename("temp.txt", "students.txt")




def delete_record():
  '''
  Void function deletes a specific record in the file.
  '''
  # Get what user wants to be searched
  search = input("What would you like to search and delete? ")

  # Open file and create a temp file to copy records
  with open("students.txt", "r") as infile, \
  open("temp.txt", "a") as outfile:
    # Create flags
    found = False
    write = True
    # Get data in first line for priming read
    data = infile.readline()
    # Itereate through every record intil finding searched item
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
        confirm = input(f"Is this the record in which you want to delete? (y or n)")
        if confirm == "y" or confirm == "Y":
          # Update flags
          found = True
          write = False

      if not found and write:
        # Write whole record to temp file
        outfile.write(first + "\n" + last + "\n" + grade + "\n")

      # Get next line and switch flag back
      data = infile.readline()
      write = True

  # Update user on success
  if found:
    print("The record has been deleted.")
  else:
    print(f"{search} was never found.")

  # Delete old students.txt
  os.remove("students.txt")
  # Rename temp file to replace students.txt
  os.rename("temp.txt", "students.txt")




if __name__ == "__main__":
  main()