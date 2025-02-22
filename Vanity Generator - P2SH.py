# download wif.py as well or include it manually in this program

from wif import *
import ecdsa
import hashlib
import base58
import random

wanted = str(input("What pattern do you want (write 3xxxxxx)?: "))

while True:
    private_key_decimal = random.randint(0, 2**256)
    sign_key = ecdsa.SigningKey.from_secret_exponent(private_key_decimal, curve=ecdsa.SECP256k1)
    public_key = sign_key.get_verifying_key().to_string("compressed")

    # https://secretscan.org/PrivateKeySegwit

    # sha256 hash the public key, then ripemd160, then adds 0014 to beginning
    result_one = b"\x00\x14" + hashlib.new("ripemd160", hashlib.sha256(public_key).digest()).digest()
    # sha256 hash the previous variable, then ripemd160 again, and then add 05 to beginning
    result_two = b"\x05" + hashlib.new("ripemd160", hashlib.sha256(result_one).digest()).digest()

    # takes a double sha256 on result_two and then takes first 4 bytes (8 characters)
    double_sha = hashlib.sha256(hashlib.sha256(result_two).digest()).digest()[:4]
    address = base58.b58encode(result_two + double_sha).decode("utf-8") # combine both variables and encodes to utf

    print("{}. {}".format(private_key_decimal, address))

    if (address.startswith(wanted)):
        with open("found.txt", "a") as found:
            found.write("{}. {}\n".format(wif(private_key_decimal), address))
        print("{}. {}".format(wif(private_key_decimal), address))
        break # comment out if you want multiple