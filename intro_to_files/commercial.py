def main():
  # Set up menu
  print("This program allows you to add times for new videos as well as\n", 
       "calculate the total amount of time for all videos combined.")
  while True:
    print("Select the number of the option you want.\n",
         "1. Add new video\n",
         "2. Calculate total time")
    choice = input()
    if choice == "1":
      add_video()
    elif choice == "2":
      calculate_time()
    elif choice == "3":
      break
    else:
      print("That is not a valid option")



def add_video():
  '''
  Void function that gets the length of a video in seconds from a user and
  writes it to an outfile.
  '''
  pass



def calculate_time():
  '''
  Void function that displays the length of every video in seconds stored 
  in an infile as well as displays the total amount of time for all 
  videos combined.
  '''
  pass