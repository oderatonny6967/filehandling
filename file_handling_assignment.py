def create_file():
  """Creates a new text file named 'my_file.txt' and writes content to it."""
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line of text.\n")
      file.write("Here's a line with both a string and a number: 42\n")
      file.write("The last line before appending more.\n")
  except PermissionError:
    print("Error: You don't have permission to create the file.")
  except Exception as e:  # Catch any other unexpected exceptions
    print("Error:", e)

def read_file():
  """Reads the contents of 'my_file.txt' and displays them on the console."""
  try:
    with open("my_file.txt", "r") as file:
      content = file.read()
      print(content)
  except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
  except Exception as e:  # Catch any other unexpected exceptions
    print("Error:", e)

def append_to_file():
  """Opens 'my_file.txt' in append mode and writes additional content."""
  try:
    with open("my_file.txt", "a") as file:
      file.write("\nHere are some lines appended to the existing content:\n")
      file.write("Line 1 after appending.\n")
      file.write("Line 2 after appending.\n")
      file.write("Line 3 after appending.\n")
  except PermissionError:
    print("Error: You don't have permission to write to the file.")
  except Exception as e:  # Catch any other unexpected exceptions
    print("Error:", e)

# Create the file
create_file()

# Read the file after creation
read_file()

# Append more content
append_to_file()

# Read the file again to see the appended content
read_file()