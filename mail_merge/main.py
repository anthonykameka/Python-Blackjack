
#for each name in invited_names.txt
#Replaces the [name] placeholder with the actual name.
#Saves the letters in the folder "ReadyToSend".


#Open the starting letter file and read its contents

with open("./Input/Letters/starting_letter.txt") as file:
    starting_text = file.read()

#Open invited names list
with open("./Input/Names/invited_names.txt") as file:
    invited_names = file.readlines()

 # strip name of new line character and replace it in text
for name in invited_names:
    stripped_name = name.strip()

    new_text = starting_text.replace("[name]", stripped_name)
    print(new_text)

