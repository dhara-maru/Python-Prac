# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppending additional content to the file.")

# Reading the updated file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
