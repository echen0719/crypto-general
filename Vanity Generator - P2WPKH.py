# segwit_addr.py from https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py

from segwit_addr import * # error? read above in source
from wif import *
import ecdsa
import hashlib
import base58
import random

wanted = str(input("What pattern do you want (write bc1qxxxxxx)?: "))[4:]

while True:
    private_key_decimal = random.randint(0, 2**256)
    sign_key = ecdsa.SigningKey.from_secret_exponent(private_key_decimal, curve=ecdsa.SECP256k1)
    public_key = sign_key.get_verifying_key().to_string("compressed")
    # takes sha256 of public_key then ripemd160 of that
    ripemd160 = b"\x00" + hashlib.new("ripemd160", hashlib.sha256(public_key).digest()).digest()
    # removes 0b prefix, takes length, and pads it with 0's so it is 160 characters long
    ripemd160_binary = "0" * (160 - len(bin(int(ripemd160.hex(), 16))[2:])) + bin(int(ripemd160.hex(), 16))[2:]
    # Converts ripemd160 bytes to int and then binary. 160 minus the length of binary for 0's and then append that to binary without prefix.

    data = ""
    for x in range(0, 160, 5): # groups into 5 bits of ints
       data += "{:02x}".format(int(ripemd160_binary[x:x+5], 2)) # {:02x} makes sure '00' isn't '0', result 64ch
    data = "00" + data # result 66ch

    n_list = []
    for i in range(0, 66, 2): # 33 elements after finish
        n_list.append(int(data[i:i+2], 16)) # splits data into groups of 2 and converts hex to int and appends each group
    # Calculates the checksum using segwit_addr.py

    checksum = ""
    for x in bech32_create_checksum("bc", n_list, Encoding.BECH32):
        checksum += "{:02x}".format(x)
    new_data = data + checksum # data + checksum

    f_list = []
    for i in range(0, 78, 2): # 39 elements after finish
        f_list.append(int(new_data[i:i+2], 16)) # splits new_data into groups of 2 and converts hex to int and appends each group

    # Calculates the address using segwit_addr.py
    address = bech32_encode("bc", f_list, Encoding.BECH32M)[:-6]

    if (address.startswith("bc1q" + wanted)):
        with open("found.txt", "a") as found:
            found.write("{}. {}\n".format(wif(private_key_decimal), address))
        print("{}. {}".format(wif(private_key_decimal), address))
        break # comment out if you want multiple