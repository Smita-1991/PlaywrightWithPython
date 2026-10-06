# Read the whole file

with open ("PythonBasics/example.txt", "w") as file:
    file.write("Hello world\nhow are you doing?\n")


with open("PythonBasics/example.txt", "a") as file:
    file.writelines("This is a new content\n")

with open("PythonBasics/example.txt", "r") as file:
    for line in file:
        print(line.strip())

def count_line_char(filepath):
    with open(filepath) as file:
        lines=file.readlines()
        line_count=len(lines)
        wordcount= sum(len(line.split())for line in lines)
        char_count=sum(len(line) for line in lines)
    return line_count, wordcount, char_count

count_line_char("PythonBasics/example.txt")
line_count, word_count, char_count = count_line_char("PythonBasics/example.txt")
print(f"line: {line_count}, word: {word_count}, char: {char_count}")

with open("PythonBasics/example.txt", "w+") as file:
    # Move the curser to the beginning of the file
    file.seek(0)
    file.write("Good Morning\n India")

with open("PythonBasics/example.txt", "r") as file:
    content=file.read()
    print(content)