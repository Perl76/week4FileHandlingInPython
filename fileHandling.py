def read_and_modify_file():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()

        # Define the output filename
        new_filename = f"modified_{filename}"

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Run the function
read_and_modify_file()
