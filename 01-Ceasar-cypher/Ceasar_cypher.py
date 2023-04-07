message = input('Enter message to encrypt: ')
key = int(input('Enter key (number of positions to shift): '))

# ASCII Lower case and Upper case starting and ending decimal numbers
UpperStart = 65
UpperEnd = 90
LowerStart = 97
LowerEnd = 122

encrypted_message = ""

for char in message:
    if char.isupper():
        newChar = (ord(char) - UpperStart + key) % 26 + UpperStart
        encrypted_message += chr(newChar)
    elif char.islower():
        newChar = (ord(char) - LowerStart + key) % 26 + LowerStart
        encrypted_message += chr(newChar)
    else: # If character is not a letter, it is not shifted
        encrypted_message += char

print(f"Encrypted message: {encrypted_message}")
