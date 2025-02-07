import ecdsa
import random

# 1. Generate public_key from low, high + 1
# 2. Check if public_key is equal to given
# 3. Stop loop and save to file called found.txt (if found [which is never])

while True:
    i = random.randint(21778071482940061661655974875633165533184, 43556142965880123323311949751266331066367)
    sign_key = ecdsa.SigningKey.from_secret_exponent(i, curve=ecdsa.SECP256k1) # signs it (x, y)
    public_key = sign_key.get_verifying_key().to_string("compressed").hex() # converts pbk to pvk result in bytes

    print("{}. {}".format(i, public_key))

    if (public_key == "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16"):
        with open("found.txt", "a") as file:
            file.write("{}. {} ({})".format(i, address, hex(i)))
        break
