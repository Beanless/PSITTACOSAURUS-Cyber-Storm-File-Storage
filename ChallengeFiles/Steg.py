import sys

SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

def store_byte_method(wrapper_bytes, hidden_bytes, offset, interval):
    i = 0
    while i < len(hidden_bytes):

        if (offset >= len(wrapper_bytes)):
            return

        wrapper_bytes[offset] = hidden_bytes[i]
        offset += interval
        i += 1
    for byte in SENTINEL:
        wrapper_bytes[offset] = byte
        offset += interval

def retrieve_byte_method(wrapper_bytes, offset, interval):
    hidden_bytes = bytearray()
    while offset < len(wrapper_bytes):
        match = True
        b = wrapper_bytes[offset]
        # if b matches first sentinel byte, check if the next 5 bytes are the rest of the sentinel.
        if (b == SENTINEL[0]):
            for x in range(1,6):
                if (offset + x) >= len(wrapper_bytes):
                    return hidden_bytes
                if (wrapper_bytes[offset + x] != SENTINEL[x]):
                    match = False
                    break
            # if all bytes match, stop there. end of file reached.
            if (match):
                return hidden_bytes
            else:
                hidden_bytes.append(b)
        # if b is not a sentinel byte, add to hidden_bytes array
        else:
            hidden_bytes.append(b)
        
        if (len(hidden_bytes) >= 6):
            if (hidden_bytes[len(hidden_bytes) - 6:] == SENTINEL):
                return hidden_bytes

        offset += interval
    return hidden_bytes

def store_bit_method(wrapper_bytes, hidden_bytes, offset, interval):
    for byte in hidden_bytes:
        for j in range(8):

            if (offset >= len(wrapper_bytes)):
                return

            wrapper_bytes[offset] &= 0b11111110
            wrapper_bytes[offset] |= ((byte & 0b10000000) >> 7)
            byte = (byte << 1) & ((2 ** 8) - 1)
            offset += interval
    
    for byte in SENTINEL:
        for j in range(8):
            wrapper_bytes[offset] &= 0b11111110
            wrapper_bytes[offset] |= ((byte & 0b10000000) >> 7)
            byte = (byte << 1) & ((2 ** 8) - 1)
            offset += interval
            

def retrieve_bit_method(wrapper_bytes, offset, interval):
    hidden_bytes = bytearray()
    while offset < len(wrapper_bytes):
        byte = 0
        for j in range(8):
            if (offset >= len(wrapper_bytes)):
                return hidden_bytes
            byte |= (wrapper_bytes[offset] & 0b00000001)
            if (j < 7):
                byte = (byte << 1) & ((2 ** 8) - 1)
                offset += interval

        if (byte == SENTINEL[0]):
            for x in range(1,6):
                if (wrapper_bytes[offset + x] != SENTINEL[x]):
                    match = False
                    break
            # if all bytes match, stop there. end of file reached.
            if (match):
                return hidden_bytes
            else:
                hidden_bytes.append(byte)
        else:
            hidden_bytes.append(byte)
        offset += interval
    print(hidden_bytes)
    return hidden_bytes

def main():
    if len(sys.argv) >= 8:
        print("Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
        return

    wrapper_file = None
    hidden_file = None
    wrapper_bytes = None
    hidden_bytes = None

    operation = sys.argv[1]
    method = sys.argv[2]
    offset = int(sys.argv[3][2:])
    interval = 1
    if sys.argv[4].startswith("-i"):
        if (operation == "-r"):
            interval = int(sys.argv[4][2:])
            wrapper_file = sys.argv[5][2:]
        else:
            interval = int(sys.argv[4][2:])
            wrapper_file = sys.argv[5][2:]
            hidden_file = sys.argv[6][2:]
    else:

        if (operation == "-r"):
            wrapper_file = sys.argv[4][2:]
        else:
            wrapper_file = sys.argv[4][2:]
            hidden_file = sys.argv[5][2:]

    try:
        if operation == "-r":
            with open(wrapper_file, "rb") as wrapper_file:
                wrapper_bytes = bytearray(wrapper_file.read())
        else:
            with open(wrapper_file, "rb") as wrapper_file:
                wrapper_bytes = bytearray(wrapper_file.read())
            with open(hidden_file, "rb") as hidden_file:
                hidden_bytes = bytearray(hidden_file.read())
    except (FileNotFoundError):
        print("Error: File not found.")
        return
    
    if operation == "-s" and method == "-B":
        store_byte_method(wrapper_bytes, hidden_bytes + SENTINEL, offset, interval)
        sys.stdout.buffer.write(wrapper_bytes)
    elif operation == "-r" and method == "-B":
        hidden_data = retrieve_byte_method(wrapper_bytes, offset, interval)
        sys.stdout.buffer.write(hidden_data)
    elif operation == "-s" and method == "-b":
        store_bit_method(wrapper_bytes, hidden_bytes + SENTINEL, offset, interval)
        sys.stdout.buffer.write(wrapper_bytes)
    elif operation == "-r" and method == "-b":
        hidden_data = retrieve_bit_method(wrapper_bytes, offset, interval)
        sys.stdout.buffer.write(hidden_data)
    else:
        pass

if __name__ == "__main__":
    main()
