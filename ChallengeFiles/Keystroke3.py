from pynput.keyboard import Controller
from termios import tcflush, TCIFLUSH
from sys import stdin
from time import sleep
from random import uniform

# wait 5 seconds before typing
sleep(5)

# requires the password and the timings of each character.
password = "This is an incorrect password.Thhiiss iiss aann iinnccoorrrreecctt ppaasssswwoorrdd."
timings = "0.26, 0.51, 0.52, 0.28, 0.33, 0.34, 0.65, 0.95, 0.97, 0.58, 0.12, 0.42, 0.67, 0.41, 0.48, 0.49, 0.43, 0.38, 0.35, 0.17, 0.89, 0.20, 0.13, 0.27, 0.78, 0.18, 0.67, 0.66, 0.94, 0.64, 0.87, 0.43, 0.87, 0.65, 0.96, 0.85, 0.65, 0.15, 0.78, 0.78, 0.72, 0.78, 0.86, 0.72, 0.70, 0.26, 0.56, 0.35, 0.28, 0.26, 0.76, 0.41, 0.55, 0.33, 0.69, 0.54, 0.75, 0.75, 0.56"

# clean up the inputs
password = password.split(",")
password = password[:(len(password) // 2 + 1)]
timings = timings.split(",")
timings = [ float(a) for a in timings ]

# generate list of timings for sleep functions
keypress = timings[:len(timings) // 2 + 1]
keyinterval = timings[len(timings) // 2 + 1:]

# prepare to type the output
keyboard = Controller()
string = password
for x in range(0,len(string[0])):
    keyboard.press(string[0][x])
    sleep(keypress[x])
    keyboard.release(string[0][x])
    # last interval doesnt exist, so skip it when it gives an error.
    try:
        sleep(keyinterval[x])
    except:
        break

tcflush(stdin, TCIFLUSH)