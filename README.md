I have always been interested in cryptocurrency and cryptography since I was young. But recently, I got more interested in the algorithms used by Bitcoin and other cryptocurrencies to generate private keys, public keys, and addresses. This led me into one rabbit one until another which is why I have this repository. 

## Explaination of Files

### Bitcoin Puzzle #67 - 1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9.py
I looked at puzzles I could attempt and found puzzle #67 which had 67 bits of entropy or in other words, was in the range from 2<sup>66</sup> to 2<sup>77</sup>. The program I made is really simple but did take me sometime to understand how to use the ecdsa, hashlib, and base58 libraries. I used help from online through documentation and Reddit to make this. This is made only for P2PKH wallets within this range.

**Step 1**: Generate a random number between 2<sup>66</sup> and 2<sup>67</sup>.

```python
i = random.randint(73786976294838206464, 147573952589676412929)
```

**Step 2**: Get the public key (in bytes) from the private key using the [SECP256K1 graph](https://ecdsa.readthedocs.io/en/latest/ecdsa.keys.html).

```python
sign_key = ecdsa.SigningKey.from_secret_exponent(i, curve=ecdsa.SECP256k1)
public_key = sign_key.get_verifying_key().to_string("compressed")
```

**Step 3**: Takes SHA256 hash, then the RIPEMD-160 hash of the public key and then adds "00" to the front.

```python
result = b"\x00" + hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
```

**Step 4**: Gets a checksum by taking the last 4 bytes (8 characters) from a double SHA256 of the result from Step 3.

```python
checksum = hashlib.sha256(hashlib.sha256(result).digest()).digest()[:4]
```

**Step 5**: Finds the address by taking the Base58 encoding of result from Step 3 with the checksum added at the end.

```python
address = base58.b58encode(result + checksum).decode("utf-8")
```

**Step 6**: Prints the private key and address in decimal and checks if the address is equal to the target. If so, itself, the address, and hex of the decimal are added to a file.

```python
print("{}. {}".format(i, address))

    if (address == "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9"):
        with open("found.txt", "a") as file:
            file.write("{}. {} ({})".format(i, address, hex(i)))
        break
```

Helpful diagram for visulation: (https://i.sstatic.net/AcXYt.png)

<br>**Exmaple Execution**</br>
<br> **Step 1**: i = 138583296239394589403 </br>
<br> **Step 2**: public_key = b'\x02\x10\x89j^\x158\x16\xdb\x97=s,\xf4!\x1b\x04\xf4=_C\x8b\xc2\x7fFq\xdd\xe26Uf$\r' </br>
<br> **Step 3**: result = "00" + ripemd160(sha256(public_key)) = b'\x00{\xee\xecd|_{\x8b\t\n\xfb;\xb6\xb6\xbaV\xfc*\xfc\xb7' </br>
<br> **Step 4**: checksum = sha256(sha256(result))[:4] = b'\xaa[[4' </br>
<br> **Step 5**: address = base58encode(result + checksum) = 1CJJLHWKrVUBrRkLuVbsUEenjFk8pqRmxo </br>
<br> **Step 6**: ```138583296239394589403. 1CJJLHWKrVUBrRkLuVbsUEenjFk8pqRmxo```, then repeat </br>

### Bitcoin Puzzle #135 - 16RGFo6hjq9ym6Pj7N5H7L1NR1rVPJyw2v.py
Similar story to puzzle #67. I found that puzzle #135 was a popular puzzle for people to attempt with 135 bits of entropy from 2<sup>134</sup> to 2<sup>13</sup>. However, I don't understand the Bitcoin ecliptic curve yet so I don't know how to use Kangaroo or BSGS (baby step, giant step) algorithms to solve it. I basically used the same code from #67 to made this. The only difference is that the public key is already avaliable.

**Step 1**: Generate a random number between 2<sup>134</sup> and 2<sup>135</sup>.

```python
i = random.randint(21778071482940061661655974875633165533184, 43556142965880123323311949751266331066367)
```

**Step 2**: Get the public key (in bytes) from the private key using the [SECP256K1 graph](https://ecdsa.readthedocs.io/en/latest/ecdsa.keys.html).

```python
sign_key = ecdsa.SigningKey.from_secret_exponent(i, curve=ecdsa.SECP256k1)
public_key = sign_key.get_verifying_key().to_string("compressed")
```

**Step 3**: Prints the public key and then checks if the key is equal to the target. If so, it adds it to a file.

```python
print("{}. {}".format(i, public_key))

    if (public_key == "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16"):
        with open("found.txt", "a") as file:
            file.write("{}. {} ({})".format(i, address, hex(i)))
        break
```

<br>**Exmaple Execution**</br>
<br> **Step 1**: i = 28103724769903762385746599697081239237441 </br>
<br> **Step 2**: public_key = 032b7d5bd3894c5cadb3e22e5f28178a56cb9cba28185b04980978a956b3859125 </br>
<br> **Step 3**: ```28103724769903762385746599697081239237441. 032b7d5bd3894c5cadb3e22e5f28178a56cb9cba28185b04980978a956b3859125```, then repeat </br>

### Vanity Generator - P2SH.py
P2SH (Pay to Script Hash) is a popular Bitcoin address type. A quarter of all Bitcoin are stored in these addresses. These addresses always start with a 3 and are encoded in Base58 which means vanity address are possible. So, it is possible to convert an integer from 0 to 2<sup>256</sup> into one of these addresses and then into a Wallet Import Format. 

**Step 1**: Prompts user for a pattern they want in the format of 3xxxxxx.

```python
wanted = str(input("What pattern do you want (write 3xxxxxx)?: "))
```

**Step 2**: Generate a random number between 0 and 2<sup>256</sup>.

```python
private_key_decimal = random.randint(0, 2**256)
```

**Step 3**: Get the public key (in bytes) from the private key using the [SECP256K1 graph](https://ecdsa.readthedocs.io/en/latest/ecdsa.keys.html).

```python
sign_key = ecdsa.SigningKey.from_secret_exponent(i, curve=ecdsa.SECP256k1)
public_key = sign_key.get_verifying_key().to_string("compressed")
```

**Step 4**: Takes SHA256 hash, then the RIPEMD-160 hash of the public key and then adds "0014" to the front.

```python
ripemd160 = b"\x00\x14" + hashlib.new("ripemd160", hashlib.sha256(public_key).digest()).digest()
```

**Step 5**: Takes SHA256 hash of the previous step, then the RIPEMD-160 hash of the public key and then adds "05" to the front.

```python
ripemd160_two = b"\x05" + hashlib.new("ripemd160", hashlib.sha256(ripemd160).digest()).digest()
```

**Step 6**: Gets a checksum by taking the first 4 bytes (8 characters) from a double SHA256 of the result from Step 4.

```python
double_sha = hashlib.sha256(hashlib.sha256(ripemd160_two).digest()).digest()[:4]
```

**Step 7**: Finds the address by taking the Base58 encoding of result from Step 4 with the checksum added at the end.

```python
address = base58.b58encode(ripemd160_two + checksum).decode("utf-8")
```

**Step 8**: Prints the private key in decimal and the address and checks if the address starts with the pattern. If so, it adds itself and the WIF (Wallet Import Format) to a file.

```python
print("{}. {}".format(private_key_decimal, address))

    if (address.startswith(wanted)):
        with open("found.txt", "a") as found:
            found.write("{}. {}\n".format(wif(private_key_decimal), address))
        print("{}. {}".format(wif(private_key_decimal), address))
        break
```

<br>**Exmaple Execution**</br>
<br> **Step 1**: wanted = string input = 3Bitcoin
<br> **Step 2**: private_key_decimal = 85441557252791501953011245756207152215152197022773595262379450122289495056139 </br>
<br> **Step 3**: public_key = b'\x03\xe6P\xe6\x89O=\x10j\xd7]GB \xd3-\xd6\xbd=\x97\xc1v\x17YT\xc0\xe2\x87\x1c\x0f\x99\xa1\xa7' </br>
<br> **Step 4**: result_one = "0014" + ripemd160(sha256(public_key)) = b'\x00\x14\xed\x84^%6\xdb,yG\xce0\xb1|\xc6R\xf1\xb3\x83@\xa4' </br>
<br> **Step 5**: result_two = "05" + ripemd160(sha256(ripemd160)) = b'\x05\xe4\xae\xef\xdb\xcf\xefy"\x1e\x17r\xa7\x12^\xea\xfe\xa7\xef$ ' </br>
<br> **Step 6**: checksum = sha256(sha256(result_two))[:4] = b'\xac\x9d\x15x'</br>
<br> **Step 7**: address = base58encode(result_two + checksum) = 3NYBZ7XSH2WR4EmpyxwWWjufv4uaHCi25M </br>
<br> **Step 8**: ```85441557252791501953011245756207152215152197022773595262379450122289495056139. 3NYBZ7XSH2WR4EmpyxwWWjufv4uaHCi25M```, then repeat </br>
