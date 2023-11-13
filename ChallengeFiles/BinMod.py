import sys


def main():

    binary = ""
    # geets first line
    for line in sys.stdin:
        binary = line
        break
    
    output = ""
    tracker = 0
    while len(binary) > 7:

        # do 7 bit
        if (tracker % 2) == 0:
            temp = int(binary[0:7], 2)
            output += chr(temp)
            binary = binary[7:]
            pass
        # do 8 bit
        else:
            temp = int(binary[0:8], 2)
            output += temp.to_bytes((temp.bit_length() + 7) // 8, "big").decode("utf-7")
            binary = binary[8:]
            pass
        tracker += 1
    print(output)

    pass


if __name__ == "__main__":
    main()