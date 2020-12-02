from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
    if direction == "encode":
        encode = True
    else:
        encode = False
    returnT=""
    alphabet_size = (len(alphabet) - 1)
    if shift > alphabet_size:
        shift = shift % alphabet_size
    message = "Your encrypted message is: "
    if not encode:
        shift = -shift
        message = "Your decrypted message is: "
    for c in text:
        if c in alphabet:
            cIndex = alphabet.index(c)
            eIndex = cIndex + shift
            if eIndex > alphabet_size:
                eIndex = eIndex - alphabet_size
            elif eIndex < 0:
                eIndex -= 1                
            returnT += alphabet[eIndex]
        else:
            returnT += c
    print(message+returnT)

while True:
    direction=""
    retry=""
    while not (direction == "encode" or direction == "decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        caesar(text, shift, direction)
    elif direction == "decode":
        caesar(text,shift, direction)
    while not (retry == "y" or retry == "n"):
        retry = input("Would you like to continue? input y for yes, n for no:\n").lower()
    if retry == "n":
        break
print("Goodbye!")

    