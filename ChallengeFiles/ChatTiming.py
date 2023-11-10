'''
Team Members: Jeremy Wood, Nicholas Gilley, Chance Jackson, James McMahan, Nick Nash, Victoria Grillo
Date: 10/2/2023
Assignment: Chat (Timing) Covert Channel
'''

import socket
from time import time

# Keep true while testing, set false when ready to turn in
DEBUG = False

# socket details
IP = "10.4.4.100"
PORT = 12345

def main():

    print("Receiving Message...")

    # create the socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    soc.connect((IP, PORT))

    # the overt and covert message
    message = ""
    c_message = ""

    # receive data until EOF
    data = soc.recv(4096).decode()

    while (data.rstrip("\n") != "EOF"):
        message += data
        # start the "timer", get more data, and end the "timer"
        t0 = time()
        data = soc.recv(4096).decode()
        t1 = time()
        # calculate the time delta (and output if debugging)
        # delta is just time taken to recieve the next character in message
        delta = round(t1 - t0, 3)

        # print each character and the delay it was ent with
        if (DEBUG):
            print(data, " ", delta)

        # # # NOTE: 1 is delay of .1 and 0 is delay of .025 # # #
        # decodes the delays into covert binary
        if delta > .15:
            c_message += '1'
        else:
            c_message += '0'

    # close the connection to the server
    soc.close()

    # # # message recieved # # #
    print(message)
    
    # handles covert message
    bit8decode(c_message)

    return

# decodes the binary covert message into normal text and prints it.
def bit8decode(bin_string):
    print("Covert message: ")
    out = ""
    while len(bin_string) > 7:
        # stops when recieving EOF, so check the next 3 characters for EOF and cut off message if yes
        end = ""
        #end += chr(int(bin_string[0:8], 2))
        #end += chr(int(bin_string[8:16], 2))
        #end += chr(int(bin_string[16:24], 2))
        if end == "EOF":
            break
        out += chr(int(bin_string[0:8], 2))
        bin_string = bin_string[8:]

    print(out)
    

##### MAIN #####
if __name__ =="__main__":
    main()