alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
def encrypt(words,shift):
    shift %= 26
    result = ""
    for i in words:
        if i in alphabet:
            result += alphabet[((alphabet.index(i)+shift)%26)]
        else:
            result += i
    print("Here's the encoded result: "+result)
def decrypt(words,shift):
    shift %= 26
    result = ""
    for i in words:
        if i in alphabet:
            result += alphabet[(26+(alphabet.index(i)-shift))%26]
        else:
            result += i
    print("Here's the decoded result: "+result)
run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text,shift)
    else:
        print("Wrong input")
    cont=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if cont == 'no':
        run = False

