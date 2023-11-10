'''
Team Members: Jeremy Wood, Nicholas Gilley, Chance Jackson, James McMahan, Nick Nash, Victoria Grillo
'''

import sys

############# NOTES FOR LATER ###################
# string.isupper() returns boolean and checks if string has uppercase letters in it
# string.upper() makes all characters in the string uppercase

# benefit of doing the code like this is we can make any alphabet for encoding/decoding

def main():
    # grabs desired coding instruction (encrypt or decrypt), and the desired key
    coding = sys.argv[1].lower()
    key = sys.argv[2].lower()
    
    # try except is to make the command prompt cleaner when closing the program.
    try:
        # is user wants to encode
        if coding.lower() == "-e":
            # replace() removes the spaces from the key
            encode(key.replace(" ", ""))
        
        # if user wants to decode
        if coding.lower() == "-d":
            # replace() removes the spaces from the key
            decode(key.replace(" ", ""))
    except:
        return

# encoding function
def encode(key):
    # custom alphabet
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # infinitely ask for things to encode, main loop
    while(True):
        # initialize some values
        keypos = 0
        output = ""
        
        # get text from the command line
        text = input()
        
        # continue until all text is encoded.
        while len(text) != 0:
            char1 = key[keypos]
            char2 = text[0]
            
            # if the full key has been used, reuse the key.
            if (len(key) - 1) == keypos:
                keypos = 0
            
            # index throws an error if item not in list, so do try, except
            try:
                # get cypher number of the text's character
                ind2 = alpha.index(char2.lower())
                
                # get cypher num of the key's current character
                ind1 = alpha.index(char1)
                
                # gets the cyher text index
                cyindex = (ind1 + ind2) % 26
                
                # if character is uppercase, keep uppercase in output
                if char2.isupper():
                    temp = alpha[cyindex]
                    output += temp.upper()
                    text = text[1:]
                    keypos += 1
                else:
                    # adds the encrypted character to the output string
                    output += alpha[cyindex]
                    text = text[1:]
                    keypos += 1
                
            # if the current character in text isn't in the alphabet, append to output string
            except:
                output += text[0]
                text = text[1:]
        # prints fully encoded text
        print(output)
    return 

# decoder function
def decode(key):
    # custom alphabet
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # infinitely ask for things to decode
    for text in sys.stdin:
        # initialize some values
        keypos = 0
        output = ""
        # this slices the new line character off the end of the string.
        text = text[:len(text) - 1]
        
        # continue until all text is decoded.
        while len(text) != 0:
            char1 = key[keypos]
            char2 = text[0]
            
            # if the full key has been used, reuse the key.
            if (len(key) - 1) == keypos:
                keypos = 0
            
            # index throws an error if item not in list, so do try, except
            try:
                # get cypher number of the encrypted text's character
                ind2 = alpha.index(char2.lower())
                
                # get cypher number of the key's current character
                ind1 = alpha.index(char1)
                
                # gets the decrypted text index
                cyindex = (26 + (ind2 - ind1)) % 26
                
                # if character is uppercase, keep uppercase in output
                if char2.isupper():
                    temp = alpha[cyindex]
                    output += temp.upper()
                    text = text[1:]
                    keypos += 1
                else:
                    # adds the decrypted character to the output string
                    output += alpha[cyindex]
                    text = text[1:]
                    keypos += 1
                
            # if the current character in text isn't in the alphabet, just append to output string
            except:
                output += text[0]
                text = text[1:]
        # prints fully encoded text
        print(output)
    return

########## MAIN ##########

if __name__ == "__main__":
    main()