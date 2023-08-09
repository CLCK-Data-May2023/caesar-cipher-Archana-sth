# to get a-z alphabet
import string 
alphabet= string.ascii_lowercase
shift = 5
plain_sentences=input("please enter a sentences : ")


new_message = ""
for char in plain_sentences:
    if char in alphabet:
        position=alphabet.index(char)
        # we need to be within 26 letters.
        new_position = (position+shift)%26
        new_message += alphabet[new_position]
    else:
        # number or space will be print as it is.
        new_message += char
print("the encrypted sentence is: ", new_message)
