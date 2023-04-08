message = input('Enter encrypted message: ')

#message = 'Ht P, kljyfwalk?' # =  "Am I, decrypted?" key = 7

# ASCII Lower case and Upper case starting and ending decimal numbers
UpperStart = 65
UpperEnd = 90
LowerStart = 97
LowerEnd = 122


# Variables
decryptation = '' # Empty string to store decrypted message
char = ''         # Empty string to store each character in message
attempt = 1       # Counter for number of attempts

#------------------------------------------------------------ Code logic description -----------------------------------------------------------------------------------

# Function to shift characters.  It takes the ASCII end of the alphabet as a parameter, and then shifts the character by the key. 
# The parameter is used to determine if the character needs to wrap around the alphabet. If the character is not a letter, it is not shifted.
# The new character is then added to the decryptation string.
# The function is called twice, once for upper case and once for lower case.



def shifter(asciiEnd):
    global decryptation
    newChar = ord(char) + key
    if newChar > asciiEnd:
            newChar = newChar - 26 # Wrap around alphabet
    decryptation += chr(newChar)


for key in range(0, 26): # 26 possible keys to try
    for char in message[0: len(message): 1]:
        if char.isupper():
            shifter(UpperEnd)
        elif char.islower():
            shifter(LowerEnd)
        elif ord(char) not in range(UpperStart, UpperEnd) and ord(char) not in range(LowerStart, LowerEnd):    # If character is not a letter, it is not shifted
            decryptation += char 
            newChar = 0
    print(f"Attempt {attempt}: " + decryptation)
    attempt+=1
    decryptation = '' # Resetting decryptation string empty for next attempt
    
    
    
#     ("HELLO", "IFMMP", 1),
#     ("world!", "DUYSH!", 7),
#     ("Ab-C", "Za-B", 25),
#     ("This is a secret message :)", "Qefp fp x pbzobq jbppxdb :)", 23),
#     ("python", "ueynsl", 5),
#     ("Caesar Cipher", "Swkwm Uebotl", 20),
#     ("The quick brown fox jumps over the lazy dog.", "Fov agcuc nbyzr rkd vylfe clyex tcs.", 12),
#     ("Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "Ebyvt Zcnwf zj jvumpi wlssj ksan jcrkibw zexwylw lesvih.", 17),
#     ("1234abcd", "4567defg", 3),
#     ("", "", 13)
    
