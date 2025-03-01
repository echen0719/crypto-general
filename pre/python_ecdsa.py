import ecdsa
import time

start_time = time.time()

sign_key = ecdsa.SigningKey.from_secret_exponent(3572348754320758732478057, curve=ecdsa.SECP256k1)
public_key = (sign_key.get_verifying_key().to_string("compressed")).hex()

end_time = time.time()

print(public_key)
print(f"Time taken: {end_time - start_time:.10f} seconds")