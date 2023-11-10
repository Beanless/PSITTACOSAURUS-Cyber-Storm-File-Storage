'''
Team Members: Jeremy Wood, Nicholas Gilley, Chance Jackson, James McMahan, Nick Nash, Victoria Grillo
Date: 9/27/2023
Assignment: FTP (Storage) Covert Channel
'''

##For 7 bits, ignore files that have either of the first 3 bits

from ftplib import FTP

# set to 7 or 10, whichever bit type you want tested.
METHOD = 7

# FTP server details
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = f"/{METHOD}"
USE_PASSIVE = True # set to False if the connection times out

# main code here
def main():

    # connect and login to the FTP server
    ftp = FTP()
    ftp.connect(IP, PORT)
    ftp.login(USER, PASSWORD)
    ftp.set_pasv(USE_PASSIVE)

    # navigate to the specified directory and list files
    ftp.cwd(FOLDER)
    files = []
    ftp.dir(files.append)

    # exit the FTP server
    ftp.quit()

    if METHOD == 7:
        bit7(files)
        print(bit7)
    elif METHOD == 10:
        bit10(files)
        print(bit10)

# # # # # # #
### NOTE: the reason we commented out the print statements is the pdf says only output the decoded text ###
# # # # # # #

def bit7(files):

    #print("Now let us work with the 7-right bits")
    #print("-------------------------------------")
    # display the folder contents (For 7-right bits)
    text7 = ""
    final7 = ""
    for f in files:
        #print(f[3:10])
        if (f[0:3] == "---"):
            #print("Above is valid")
            f7 = ""
            for i in f[3:10]:
                if (i == "-"):
                    f7 += "0"
                else:
                    f7 += "1"
            text7 = chr(int(f7, 2))
            #f7 += ","
            #print(f7)
            #print(text7)
            final7 += text7

    #print()

    #print("##################")
    #print(f"Final encoded message is:\n{final7}")
    #print("##################")

    print(final7)
    ####end####

def bit10(files):

    #print("Now let us work with all 10 bits")
    #print("--------------------------------")
    # display the folder contents (For all 10 bits)
    text10 = ""
    final10 = ""
    for f in files:
        #print(f[:10])
        f10 = ""
        for i in f[:10]:
            if (i == "-"):
                f10 += "0"
            else:
                f10 += "1"
        text10 = chr(int(f10, 2))
        #f10 += ","
        #print(f10)
        #print(text10)
        final10 += text10

    #print()  

    #print("###################")
    #print(f"Final encoded message is:\n{final10}")
    #print("###################")

    print(final10)
    ####end####


##### MAIN #####
if __name__ == "__main__":
    main()
