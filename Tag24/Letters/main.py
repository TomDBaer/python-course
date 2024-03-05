#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def write_letter(name, content):
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as f:
        f.write(content)


with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = [line.rstrip() for line in file]

# loop all names
for name in names:
    new_letter = letter.replace("[name]", name)
    write_letter(name=name, content=new_letter)



