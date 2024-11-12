#!/usr/bin/env python3

import sys
import base64

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

    
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))

char = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("Here is your flag:")
print("".join(chr(c) for c in char))

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert the hex string to bytes and then decode to a string
print("Here is your flag:")
print(bytes.fromhex(hex_string).decode('utf-8'))

hex_string_base64 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# convert and decode
byte_data = bytes.fromhex(hex_string_base64)
#encode into base64
base64_encode = base64.b64encode(byte_data)
#find the flag
print("Flag 4:")
print(base64_encode.decode('utf-8'))