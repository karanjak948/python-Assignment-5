# file_handling_assignment.py

def create_file():
    """Create a new text file and write initial content."""
    try:
        with open('my_file.txt', 'w') as file:
            file.write("This is the first file class in PlP.\n")
            file.write("Its fun to code with PlP: 42\n")
            file.write("This is the 5th week on python class\n")
        print("File created and initial content written.")
    except PermissionError:
        print("Permission denied: Cannot write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    """Read the contents of the file and display them."""
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile contents:\n", content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    """Append additional lines of text to the file."""
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line of text.\n")
            file.write("Adding another line with numbers: 123\n")
            file.write("Final line with more text: Goodbye!\n")
        print("Additional lines appended to the file.")
    except PermissionError:
        print("Permission denied: Cannot write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == '__main__':
    main()
