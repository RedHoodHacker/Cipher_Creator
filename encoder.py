#!/usr/bin/python3 

import math 
import time 


#Encoder that uses:
# Caesar Cipher 1 
# ROT-13        2
# XOR FF        3
# Affine Cipher 4
# Atbash Cipher 5
# Bacon Cipher  6
# Music Notes   7
# ROT-47        8 
# Morse Code    9 
# Enigma Machine 10 


# Pseudo Code 

# Prints WELCOME TO JURASSIC PARK, oh wait no that's not right but hey 
# there are some strange things here! Go ahead and choose one to test it out! 

# shows list of 10 ciphers to choose from

# Choose 1 good sir! 

# checks to see if it's between 1 and 10 if not error 

# Chooses 1 

# alright you chose #blank# wonderful! What is the string you want to encode? 

# enters string, does it have to check for any invalid characters? 

# Encrypts it using the provided function and/or class 

# prints out encoded value 

# here you are my sir! 

# Asks if there's anything else the user wants to encode y/n 

# if not, exit, if yes 

# Goodbye good sir! Hope to encode something again soon! 


menu = """1. Caesar 
          2. ROT-13
          3. XOR FF
          4. Affine
          5. Atbash 
          6. Bacon
          7. Music Notes
          8. ROT-47
          9. Morse Code 
          10. ENIGMA MACHINE!! """


print("""Welcome to Jurassic Park! oh wait that's not right buy hey,
there's are some strange things here! Go ahead and choose one to test it out!""")
time.sleep(5)




def Caesar_cipher(): # can only do ascii no digits, must check for that
    unencoded_val = input("PIZZA PIZZA! What can caesar encode for you?: ")





















while True:
    print(menu)
    choice = int(input("Choose one! [1-10]: "))
    if choice < 10:
        break
    else:
        print("I am sorry that doesn't work, denied!")
        exit()
