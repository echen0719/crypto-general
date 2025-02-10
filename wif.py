import hashlib
import base58

def wif(decimal):
    hex_value = hex(decimal)[2:]
    check = "80" + "0" * (64 - len(hex_value)) + hex_value + "01"
    checksum = hashlib.sha256(hashlib.sha256(bytes.fromhex(check)).digest()).digest()[:4]
    wif = base58.b58encode(bytes.fromhex(check) + checksum).decode("utf-8")
    return wif