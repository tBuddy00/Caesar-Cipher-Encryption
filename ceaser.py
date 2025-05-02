message = "Hello World!"
shift = 7

FIRST_CHAR_CODE = ord("A") #A starts at 65
LAST_CHAR_CODE = ord("Z") # Z Ends with 90 
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1 #The difference (90 - 65) is 26 (All alphabetical letters)

def caesar_shift(message, shift):
    #result placeholder
    result = ''

    #iterate through every message, upper case is easier to handle with
    for i in message.upper():
        #convert to ASCII Code
        #check for alphabet letters
        if(i.isalpha()):
            conv_letter = ord(i) #convert letter into ASCII Code number
            new_letter_code = conv_letter + shift #Using ASCII Number + Shift = New Letter
            
            #+++ Alphabetical Limitation - Between A to Z (26 numbers between)+++
            #to encrypt a message 
                #e. g. 93 -> 90 --> to much
                # solution: 93 - 26 = 67 (makes letter 'C')
            if(new_letter_code > LAST_CHAR_CODE):

                new_letter_code -= CHAR_RANGE

            #to decrypt a message
            if(new_letter_code < FIRST_CHAR_CODE):
                new_letter_code += CHAR_RANGE
            
            new_letter = chr(new_letter_code) #deconvert from ASCII code number to alphabet letter
            result += new_letter 

           # print(f"\nOriginal: {i}\nASCII Code: {conv_letter}\nShifted Code: {new_letter_code}\nNew letter: {new_letter}\n")
        else:
            result = result + i #if char is not alphabetical, add to result
    return result

user_message = input("\nMessage to encrypt: ")
user_shiftKey = int(input("Shift: "))
cypher_text = caesar_shift(user_message, user_shiftKey)

print(f"\n+++ Cypher text: {cypher_text} +++\n")
