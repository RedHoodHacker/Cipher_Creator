#!/usr/bin/python3

print("ROT-13 Cipher")




def rot_13():
    strings = input("What is the string you want to cipher from caesar: ")

    result = ""
    for x in strings:
        x = ord(x)
        x += 13 
        if x > 65 and x < 90:
            x = x + 13
            result += chr(x)
        elif x > 32:
            x = x - 26 
            result += chr(x)
        elif x > 97 and x < 122:
            x = x + 13
            result += chr(x)
        elif x  > 97:
            x = x - 26
            result += chr(x)
        else:
            result += chr(x)
    print(strings)
    print(result)


rot_13()




