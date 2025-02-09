I have always been interested in cryptocurrency and cryptography since I was young. But recently, I got more interested in the algorithms used by Bitcoin and other cryptocurrencies to generate private keys, public keys, and addresses. This led me into one rabbit one until another which is why I have this repository. 

## Explaination of Files

### Bitcoin Puzzle #67 - 1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9.py
I looked at puzzles I could attempt and found puzzle #67 which had 67 bits of entropy or in other words, was in the range from 2<sup>66</sup> to 2<sup>77</sup>. The program I made is really simple but did take me sometime to understand how to use the ecdsa, hashlib, and base58 libraries. I used help from online through documentation and Reddit to make this.

**Step 1**: Generate a random number between 2<sup>66</sup> and 2<sup>67</sup>.
**Step 2**: Get the public key (in bytes) from the private key using the [SECP256K1 graph](https://ecdsa.readthedocs.io/en/latest/ecdsa.keys.html).
**Step 3**: Takes SHA256 hash, then the RIPEMD-160 hash of the public key and then adds "00" to the front.
**Step 4**: Gets a checksum by taking the last 4 bytes (8 characters) from a double SHA256 of the result from Step 3.
**Step 5**: Finds the address by taking the Base58 encoding of result from Step 3 with the checksum added at the end.
**Step 6**: Prints the private key in decimal and then checks if the address is equal to the target. If so, it adds it to a file.

Helpful image for visulation 

![](https://i.sstatic.net/AcXYt.png)
