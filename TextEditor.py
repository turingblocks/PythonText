def main():
    lines = []
    filename = ""

    while True:
        print("\n1. Create a new file")
        print("2. Edit an existing file")
        print("3. Add line to file")
        print("4. Edit a line in file")
        print("5. Save the file")
        print("6. Exit")

        option = input("\nPlease choose an option: ")

        if option == '1':
            filename = input("\nEnter new file name: ")
            lines = []
        elif option == '2':
            filename = input("\nEnter existing file name: ")
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                print("\nFile not found. Please try again.")
        elif option == '3':
            line = input("\nEnter line to add: ")
            lines.append(line + '\n')
        elif option == '4':
            for i, line in enumerate(lines, 1):
                print(f"{i}: {line.strip()}")
            line_number = int(input("\nEnter line number to edit: ")) - 1
            if 0 <= line_number < len(lines):
                new_line = input("\nEnter new line: ")
                lines[line_number] = new_line + '\n'
            else:
                print("\nInvalid line number.")
        elif option == '5':
            if filename:
                with open(filename, 'w') as file:
                    file.writelines(lines)
                print("\nFile saved.")
            else:
                print("\nNo file to save. Please create a new file or edit an existing one.")
        elif option == '6':
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
