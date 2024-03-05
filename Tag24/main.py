# open and close a file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# open and write
with open("my_file.txt", mode="w") as file:
    file.write("Look at my nudes")

# open and add write to file
with open("my_file.txt", mode="a") as file:
    file.write("\nEven more nudes")


