import java.math.BigInteger;
import java.security.SecureRandom;
import java.security.Security.addProvider(new BouncyCastleProvider());

/* i = random.randint(1,  2**256)
    sign_key = ecdsa.SigningKey.from_secret_exponent(i, curve=ecdsa.SECP256k1)
    public_key = sign_key.get_verifying_key().to_string("compressed")

    result = b"\x00" + hashlib.new("ripemd160", hashlib.sha256(public_key).digest()).digest()
    checksum = hashlib.sha256(hashlib.sha256(result).digest()).digest()[:4]
    address = base58.b58encode(result + checksum).decode("utf-8") */

public class VanityGeneratorP2PKH {
    public static void main(String[] args) {
        BigInteger priv = Keys.createEcKeyPair().getPrivateKey();
        System.out.println(priv);
    }
}