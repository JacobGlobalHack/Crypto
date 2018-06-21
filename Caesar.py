import string
def alphabet_position(letter):
    if letter == "a" or letter == "A":
        return 1 
    elif letter == "b" or letter == "B":
        return 2
    elif letter == "c" or letter == "C":
        return 3
    elif letter == "d" or letter == "D":
        return 4
    elif letter == "e" or letter == "E":
        return 5
    elif letter == "f" or letter == "F":
        return 6
    elif letter == "g" or letter == "G":
        return 7
    elif letter == "h" or letter == "H":
        return 8
    elif letter == "i" or letter == "I":
        return 9
    elif letter == "j" or letter == "J":
        return 10
    elif letter == "k" or letter == "K":
        return 11 
    elif letter == "l" or letter == "L":
        return 12
    elif letter == "m" or letter == "M":
        return 13
    elif letter == "n" or letter == "N":
        return 14
    elif letter == "o" or letter == "O":
        return 15
    elif letter == "p" or letter == "P":
        return 16
    elif letter == "q" or letter == "Q":
        return 17
    elif letter == "r" or letter == "R":
        return 18
    elif letter == "s" or letter == "S":
        return 19
    elif letter == "t" or letter == "T":
        return 20
    elif letter == "u" or letter == "U":
        return 21
    elif letter == "v" or letter == "V":
        return 22
    elif letter == "w" or letter == "W":
        return 23
    elif letter == "x" or letter == "X":
        return 24
    elif letter == "y" or letter == "Y":
        return 25
    elif letter == "z" or letter == "Z":
        return 26
def rotate_character (char, rot):
    number = alphabet_position(char) + rot 
    if number < 26:
        if number == 1 and char.isupper():
            return "A"
        elif number == 2 and char.isupper():
            return "B"
        elif number == 3 and char.isupper():
            return "C"
        elif number == 4 and char.isupper():
            return "D"
        elif number == 5 and char.isupper():
            return "E"
        elif number == 6 and char.isupper():
            return "F"
        elif number == 7 and char.isupper():
            return "G"  
        elif number == 8 and char.isupper():
            return "H"
        elif number == 9 and char.isupper():
            return "I"
        elif number == 10 and char.isupper():
            return "J"
        elif number == 11 and char.isupper():
            return "K"
        elif number == 12 and char.isupper():
            return "L"
        elif number == 13 and char.isupper():
            return "M"
        elif number == 14 and char.isupper():
            return "N"
        elif number == 15 and char.isupper():
            return "O"
        elif number == 16 and char.isupper():
            return "P"
        elif number == 17 and char.isupper():
            return "Q"
        elif number == 18 and char.isupper():
            return "R"
        elif number == 19 and char.isupper():
            return "S"
        elif number == 20 and char.isupper():
            return "T"
        elif number == 21 and char.isupper():
            return "U"
        elif number == 22 and char.isupper():
            return "V"
        elif number == 23 and char.isupper():
            return "W"
        elif number == 24 and char.isupper():
            return "X"
        elif number == 25 and char.isupper():
            return "Y"
        elif number == 26 and char.isupper():
            return "Z"
        elif number == 1   and char.islower():
            return "a"
        elif number == 2   and char.islower():
            return "b"
        elif number == 3   and char.islower():
            return "c"
        elif number == 4   and char.islower():
            return "d"
        elif number == 5   and char.islower():
            return "e"
        elif number == 6   and char.islower():
            return "f"
        elif number == 7   and char.islower():
            return "g"
        elif number == 8   and char.islower():
            return "h"
        elif number == 9   and char.islower():
            return "i"
        elif number == 10   and char.islower():
            return "j"
        elif number == 11  and char.islower():
            return "k"
        elif number == 12   and char.islower():
            return "l"
        elif number == 13   and char.islower():
            return "m"
        elif number == 14   and char.islower():
            return "n"
        elif number == 15   and char.islower():
            return "o"
        elif number == 16   and char.islower():
            return "p"
        elif number == 17   and char.islower():
            return "q"
        elif number == 18   and char.islower():
            return "r"
        elif number == 19   and char.islower():
            return "s"
        elif number == 20   and char.islower():
            return "t"
        elif number == 21   and char.islower():
            return "u"
        elif number == 22   and char.islower():
            return "v"
        elif number == 23   and char.islower():
            return "w"
        elif number == 24   and char.islower():
            return "x"
        elif number == 25   and char.islower():
            return "y"
        elif number == 26   and char.islower():
            return "z"
    else:
        number2 = number % 26
        if number2 == 1 and char.isupper():
            return "A"
        elif number2 == 2 and char.isupper():
            return "B"
        elif number2 == 3 and char.isupper():
            return "C"
        elif number2 == 4 and char.isupper():
            return "D"
        elif number2 == 5 and char.isupper():
            return "E"
        elif number2 == 6 and char.isupper():
            return "F"
        elif number2 == 7 and char.isupper():
            return "G"  
        elif number2 == 8 and char.isupper():
            return "H"
        elif number2 == 9 and char.isupper():
            return "I"
        elif number2 == 10 and char.isupper():
            return "J"
        elif number2 == 11 and char.isupper():
            return "K"
        elif number2 == 12 and char.isupper():
            return "L"
        elif number2 == 13 and char.isupper():
            return "M"
        elif number2 == 14 and char.isupper():
            return "N"
        elif number2 == 15 and char.isupper():
            return "O"
        elif number2 == 16 and char.isupper():
            return "P"
        elif number2 == 17 and char.isupper():
            return "Q"
        elif number2 == 18 and char.isupper():
            return "R"
        elif number2 == 19 and char.isupper():
            return "S"
        elif number2 == 20 and char.isupper():
            return "T"
        elif number2 == 21 and char.isupper():
            return "U"
        elif number2 == 22 and char.isupper():
            return "V"
        elif number2 == 23 and char.isupper():
            return "W"
        elif number2 == 24 and char.isupper():
            return "X"
        elif number2 == 25 and char.isupper():
            return "Y"
        elif number2 == 26 and char.isupper():
            return "Z"
        elif number2 == 1   and char.islower():
            return "a"
        elif number2 == 2   and char.islower():
            return "b"
        elif number2 == 3   and char.islower():
            return "c"
        elif number2 == 4   and char.islower():
            return "d"
        elif number2 == 5   and char.islower():
            return "e"
        elif number2 == 6   and char.islower():
            return "f"
        elif number2 == 7   and char.islower():
            return "g"
        elif number2 == 8   and char.islower():
            return "h"
        elif number2 == 9   and char.islower():
            return "i"
        elif number2 == 10   and char.islower():
            return "j"
        elif number2 == 11  and char.islower():
            return "k"
        elif number2 == 12   and char.islower():
            return "l"
        elif number2 == 13   and char.islower():
            return "m"
        elif number2 == 14   and char.islower():
            return "n"
        elif number2 == 15   and char.islower():
            return "o"
        elif number2 == 16   and char.islower():
            return "p"
        elif number2 == 17   and char.islower():
            return "q"
        elif number2 == 18   and char.islower():
            return "r"
        elif number2 == 19   and char.islower():
            return "s"
        elif number2 == 20   and char.islower():
            return "t"
        elif number2 == 21   and char.islower():
            return "u"
        elif number2 == 22   and char.islower():
            return "v"
        elif number2 == 23   and char.islower():
            return "w"
        elif number2 == 24   and char.islower():
            return "x"
        elif number2 == 25   and char.islower():
            return "y"
        elif number2 == 26   and char.islower():
            return "z"
        
        
       
def encrypt(text = raw_input("Type a message:"), key = raw_input("Encryption key:")):
    returnvalue = ''
    keycount = len(key)
    index = 0
    for char in text:
         if char.isalpha():
             rot = key[(index % keycount)]
             rot = alphabet_position(rot)
             encrypt_char = rotate_character(char, rot)
             returnvalue = returnvalue + encrypt_char
             index = index + 1
         else:
            encrypt_char = char
            returnvalue = returnvalue + encrypt_char
    return returnvalue
    
        
    #returnvalue = ''
    #for char in text:
      #  if char.isalpha():
         #   encrypted = rotate_character(char, rot)
          #  returnvalue = returnvalue + encrypted 
        #else:
          #  encrypted = char
          #  returnvalue = returnvalue + encrypted
    
    #return returnvalue    
        
print encrypt()




#print encrypt("Hello, World!", 5)