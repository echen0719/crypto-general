# Elliptic curve parameters (for secp256k1, which is used in Bitcoin)
P = 115792089237316195423570985008687907853269984665640564039457584007908834671663  # prime modulus
A = 0  # secp256k1 curve parameter
B = 7  # secp256k1 curve parameter
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240  # Gx for secp256k1
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424  # Gy for secp256k1

def modinv(a, p=P):
    """ Fermat's Little Theorem to calculate modular inverse """
    return pow(a, p - 2, p)

def multiply(k):
    result_x = 0
    result_y = 0
    base_x = Gx
    base_y = Gy

    while k > 0:
        if k & 1:  # If the lowest bit is 1
            if result_x == 0 and result_y == 0:
                result_x = base_x
                result_y = base_y
            else:
                slope = (result_y - base_y) * modinv(result_x - base_x) % P
                result_x, result_y = point_add(result_x, result_y, base_x, base_y, slope)

        slope = (3 * base_x ** 2) * modinv(2 * base_y) % P
        base_x, base_y = point_double(base_x, base_y, slope)

        k >>= 1  # Right shift by 1 (divide by 2)

    return result_x, result_y

def point_add(x1, y1, x2, y2, slope):
    """ Adds two points (x1, y1) and (x2, y2) on the secp256k1 curve. """
    new_x = (slope ** 2 - x1 - x2) % P
    new_y = (slope * (x1 - new_x) - y1) % P
    return new_x, new_y

def point_double(x, y, slope):
    """ Doubles the point (x, y) on the secp256k1 curve. """
    new_x = (slope ** 2 - 2 * x) % P
    new_y = (slope * (x - new_x) - y) % P
    return new_x, new_y

private_key = 3572348754320758732478057

import time
start_time = time.time()
public_x, public_y = multiply(private_key)
end_time = time.time()

print("Public Key:")
print(f"X: {public_x}")
print(f"Y: {public_y}")

print(f"Time taken: {end_time - start_time:.10f} seconds")