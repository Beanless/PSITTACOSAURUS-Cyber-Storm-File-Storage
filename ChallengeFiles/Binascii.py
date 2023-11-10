'''
Team Members: Jeremy Wood, Nicholas Gilley, Chance Jackson, James McMahan, Nick Nash, Victoria Grillo
'''

##### infection.txt response #####
# The code shown activates an infinite loop and (this is my assumption) calls itself over and over.
# This is a fork bomb meant to slow down the host computer. When we ran it, it the CPU usage of the VM
# went up by a large margin. As of right now, we are not sure how to stop it... There's probably a 
# single command that would stop it, knowing Linux.

# system command import. allows use of stdin, stdout, etc...
import sys

# main function
def main():
    
    ### NOTE: this try except is here for when the user themselves types in binary in the command line ###
    try:
        # until there is no more input from stdin
        for line in sys.stdin:
            
            # if the characters in the input are divisible by 7, then it is a utf-7 decoding 
            if ((len(line) - 1) % 7) == 0:
                dec7(line)
            # if the characters in the input are divisible by 7, then it is a utf-8 decoding 
            if ((len(line) - 1) % 8) == 0:
                dec8(line)
    except:
        print("Some error occured.")
        return

# utf-8 decoder
def dec8(line):
    tokens = []
    
    # turns the input into 8-bit (8 character) tokens
    while(True):
        if len(line) < 8:
            break
        tokens.append(line[0:8])
        line = line[8:]
    
    answer8 = ""
    # for every token
    for bits in tokens:
        
        # if token is this string, it is a backspace, so remove last added character from output
        if bits == '00001000':
            answer8 = answer8[0:len(answer8)]
        
        # turn the token into an integer for the decoder
        nums = int(bits, 2)
        
        # default uses utf-8 decoding
        #
        # found this function here:
        # https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
        # modified to fit this program.
        answer8 += nums.to_bytes((nums.bit_length() + 7) // 8, "big").decode()
    # print decoded text
    print(answer8)

# utf-7 decoder
def dec7(line):
    tokens = []
    
    # turns the input into 7-bit (7 character) tokens
    while(True):
        if len(line) < 7:
            break
        tokens.append(line[0:7])
        line = line[7:]
    
    answer = ""
    # for every token
    for bits in tokens:
        
        # if token is this string, it is a backspace, so remove last added character from output
        if bits == '0001000':
            answer = answer[0:len(answer)]
        
        # turn the token into an integer for the decoder
        nums = int(bits, 2)
        
        # decode using utf-7 as base
        #
        # found this function here:
        # https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
        # modified to fit this program.
        answer += nums.to_bytes((nums.bit_length() + 7) // 8, "big").decode("utf-7")
    # print decoded text
    print(answer)


##### MAIN #####
# if this file is the one being run, run this file
if __name__ == "__main__":
    main()
