
# File Handling and Exception Handling Assignment

def file_read_write():
    """
    Reads from 'input.txt' and writes a modified version to 'output.txt'.
    Modification: Convert text to uppercase.
    """
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File has been read, modified, and written to output.txt")

    except FileNotFoundError:
        print("❌ Error: 'input.txt' was not found.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def error_handling_lab():
    """
    Asks the user for a filename and handles errors if it doesn’t exist or can’t be read.
    """
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r") as file:
            print("\n📖 File Content:")
            print(file.read())
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# --- Main Program ---
if __name__ == "__main__":
    print("Running File Read & Write Challenge 🖋️")
    file_read_write()

    print("\nRunning Error Handling Lab 🧪")
    error_handling_lab()
