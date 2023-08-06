# to get a-z alphabet.
import string
alphabet = string.ascii_lowercase

def encryption(plaintext, shift):
    cipher_text = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.index(char)
            #we need to be within the 26 letter.
            new_position = (position+shift)%26
            cipher_text += alphabet[new_position]
        else:
            # number or space will be print as it is
           cipher_text += char
    print("the text after encryption is :", cipher_text)
    
    
def decryption(cipher_text, shift):
    plaintext = ""
    for char in cipher_text :
        if char in alphabet:
            position = alphabet.index(char)
            #we need to be within the 26 letter.
            new_position = (position-shift)%26
            plaintext += alphabet[new_position]
        else:
             # number or space will be print as it is
            plaintext += char
    print("the text after decryption is :", plaintext)

 # if u want to end on 'no'   
end = False
while not end:
    mode = input("type 'encrypt' for encryption, type 'decrypt' for decryption : ")
    plaintext = input("please enter a sentence : ")
    shift = int(input("please enter the number of place to shift : "))
    if mode == "encrypt" :
        encryption(plaintext, shift)
    elif mode == "decrypt":
        decryption(plaintext, shift)
    play_again = input("type 'yes' to continue, type 'no' to exit : ")
    if play_again == 'no':
        end = True
        print("Have a nice day...")
    
