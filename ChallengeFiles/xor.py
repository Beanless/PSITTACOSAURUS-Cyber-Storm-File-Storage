import sys
import binascii

# pur name of key file here
KEY_NAME = "k3y"
# Welp. Leave it as 1. Anything else is wrong.
BUFFER_SIZE = 1

# set True for clean output, false runs normal print statement (bytearray)
CLEAN_OUTPUT = True
try:
    # read as binary
    with open(f'{KEY_NAME}', 'rb') as file:
        lines = bytearray(file.read())

    # sys.stdin.buffer.read() takes the input from stdin directly as binary.
    # this is done so as to not corrupt the binary going through the usual stdin channel.
    binary_data = bytearray(sys.stdin.buffer.read())

    xor = bytearray(len(binary_data))
    size = len(xor) // BUFFER_SIZE
    output = bytearray(size)

    x = 0
    if (len(binary_data) == len(lines)):
        for i in range(0, len(binary_data), BUFFER_SIZE):
            if (i + BUFFER_SIZE > len(binary_data)):
                break
            output[x] = lines[i] ^ binary_data[i]
            x += 1

        if CLEAN_OUTPUT:
            sys.stdout.buffer.write(output)
        else:
            print(output)


except FileNotFoundError:
    print(f"File \"{KEY_NAME}\" not found")
except Exception as e:
    print(f"An error occurred: {str(e)}") 
print()
