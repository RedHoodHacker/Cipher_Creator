#!/usr/bin/python3 

#The first function in my cipher creator script in python, just chunking away at the bits 



# Pseudo Code

# Give me a string to encrypt
# Give me the number of shifts you want me to perform 

#outputs encoded value 

print("Welcome to my caesar cipher encoder!")
strings = str(input("Give me the string you want caesar to cipher: "))
shift = int(input("Give me the number of shifts you want to perform: "))




def caesar(strings, shift):
    result = ""

    for x in strings:
        x = ord(x)
        x += shift
        if x > 126:
            x = x - 95
        elif x < 32:
            x = x + 95 
        else: 
            result += chr(x)
    print(strings)
    print(result)


caesar(strings, shift)