
# to get a-z alphabet.
import string
alphabet = string.ascii_lowercase
# to get a-z alphabet
import string 
alphabet= string.ascii_lowercase


def encripted_sentences(plain_sentences, shift):
    cipher_sentences = ""
    for char in plain_sentences:
        if char in alphabet:
            position=alphabet.index(char)
            # we need to be within 26 letters.
            new_position = (position+shift)%26
            cipher_sentences += alphabet[new_position]
        else:
            # number or space will be print as it is.
            cipher_sentences += char
    print("the encrypted sentences is :", cipher_sentences)


plain_sentences=input("please enter a sentences : ")
shift=int(input("please enter the number of place to shift : "))
encripted_sentences(plain_sentences, shift)

