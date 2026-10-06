import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

os.makedirs("new_directory", exist_ok=True)

file_path="new_directory/new_file.txt"
file_descriptor=os.open(file_path, os.O_WRONLY | os.O_CREAT)
os.write(file_descriptor, b"This file was created with the os package.\n")
os.close(file_descriptor)