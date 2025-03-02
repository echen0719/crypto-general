import ecdsa
import hashlib
import base58
import time

i = 3572348754320758732478057
sign_key = ecdsa.SigningKey.from_secret_exponent(i, curve=ecdsa.SECP256k1)
public_key = sign_key.get_verifying_key().to_string("compressed")

start = time.time()

result = b"\x00" + hashlib.new("ripemd160", hashlib.sha256(public_key).digest()).digest()
checksum = hashlib.sha256(hashlib.sha256(result).digest()).digest()[:4]
address = base58.b58encode(result + checksum).decode("utf-8")

end = time.time()

print("{}. {}".format(i, address))
print(f"Time taken: {(int)((end - start)*1000000):.10f} microseconds")