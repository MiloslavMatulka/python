"""
This program asks for the original file name and the new file,
opens the original file and writes its contents into the new file.
You can specify a path as input, for example h:/file.txt

"""

while True:
    original_file = input("Insert the original file name to copy: ")
    try:
        with open(original_file, mode='r', encoding="utf-8-sig") as open_file:
            contents = open_file.read()
    except FileNotFoundError:
        print("File not found.")
        break
        
    new_file = input("Insert the new name of the file: ")
    with open(new_file, mode='w', encoding="utf-8-sig") as write_file:
        write_file.write(contents)
    break
