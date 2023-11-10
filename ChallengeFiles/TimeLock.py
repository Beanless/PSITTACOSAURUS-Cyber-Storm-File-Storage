'''
Team Members: Jeremy Wood, Nicholas Gilley, Chance Jackson, James McMahan, Nick Nash, Victoria Grillo
Date: 10/19/2023
Assignment: TimeLock
'''

#Idea of using datatime library from https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
from datetime import datetime, timezone
import sys
import hashlib
import pytz
import time

DEBUG = True

# main function
def main():
    ### NOTE: this try except is to check the vadlity of user input ###
    try:
        for line in sys.stdin:
            print(line)
            if (len(line) > 19): #To handle echo method [just get the date only]
                line = line[1:20] # Use this for windows
                #line = line[:19] use this for l VM. 
                print(line)
            # if the characters in the input equal to 19, then it is a valid date 
            if (len(line) == 19):
                time_code(line)

    except:
        print("Invalid format! Correct format is YYYY MM DD HH mm SS")
        return

def time_code(line):
    your_secs = 0
    epoch_secs = 0
    code = ""
    element_count = 0

    # Idea from https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
    your_time =(datetime.now().strftime('%Y %m %d %H %M %S')) # Your system time
    print("Your time: {}".format(your_time))
    your_time = (datetime.now(timezone.utc).strftime('%Y %m %d %H %M %S')) # You system time in UTC
    print("Current UTC time: {}".format(your_time))
    current = datetime.strptime(your_time,'%Y %m %d %H %M %S')
    your_secs = current.timestamp() #convert datetime to seconds
    print("UTC time in secs: {}".format(your_secs))
    
    #If Debug is true, you can put a different time as your system time
    print()
    if (DEBUG == True):
        print("Since DEBUG is True, you will work with any time you put below")
        why = datetime(2013, 5, 6, 7, 43, 25)
        print("Your NEW time: {}".format(why))
        tzy = pytz.timezone('US/Central')
        d_tzy = tzy.normalize(tzy.localize(why))
        your_time = d_tzy.astimezone(pytz.utc)
        print("Your NEW UTC time now: {}".format(your_time))

        your_secs = your_time.timestamp()
        print("Your NEW UTC time in secs: {}".format(your_secs))
        print()
        
    # Covert epoch time from str to datatime so it can be convert to UTC time.\
    epochdate = datetime.strptime(line, '%Y %m %d %H %M %S')
    print("Your epoch time: {}".format(epochdate))
    tz = pytz.timezone('US/Central')
    d_tz = tz.normalize(tz.localize(epochdate))
    utc_epochdate = d_tz.astimezone(pytz.utc)
    print("Your epoch time now: {}".format(utc_epochdate))

    epoch_secs = utc_epochdate.timestamp()
    print("Your epoch time in secs: {}".format(epoch_secs))
    print()
    
    # Get the difference
    difference = (your_secs - epoch_secs)
    interval_difference = difference - (difference % 60)
    print("Difference: {}".format(difference))
    print("Difference to the lastest window: {}".format(interval_difference))
    print()
    
    # Hash the interval_difference
    interval_difference = int(interval_difference) # To get rid of the .0 because the hash use that.

    hash_this = str(interval_difference)
    
    hash_result = hashlib.md5(hash_this.encode())
    hash_again = hashlib.md5(str(hash_result.hexdigest()).encode())
    hexdigest_result = hash_again.hexdigest()

    print(hexdigest_result)

    for x in str(hexdigest_result):
        if (x.isalpha() and element_count < 2):
            code += x
            element_count += 1

    element_count = 0
    
    for y in reversed(str(hexdigest_result)):
        if (y.isdigit() and element_count < 2):
            code += y
            element_count += 1

    print("Final code: {}".format(code))
    
    return

##### MAIN #####
# if this file is the one being run, run this file
if __name__ == "__main__":
    main()
    
