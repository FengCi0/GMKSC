import secrets, hashlib, hmac
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from .graph_utils import walk_degrees
from .kem import encapsulate

def hkdf_extract(salt, ikm):
    return hmac.new(salt, ikm, hashlib.sha256).digest()

def hkdf_expand(prk, info, length):
    okm, t = b"", b""
    counter = 1
    while len(okm) < length:
        t = hmac.new(prk, t + info + bytes([counter]), hashlib.sha256).digest()
        okm += t
        counter += 1
    return okm[:length]

def hkdf(ikm, info=b"", length=32):
    return hkdf_expand(hkdf_extract(b"\x00"*32, ikm), info, length)

def encrypt(public, plaintext: bytes):
    G = public["G_pub"]
    node_pubs = public["node_pubs"]
    n = len(G)

    salt = secrets.token_bytes(12)
    start = int.from_bytes(hashlib.sha256(salt).digest(), "big") % n
    eph_pub, k = encapsulate(node_pubs[start])

    degrees = walk_degrees(G, start, len(plaintext), k)
    info = b",".join(d.to_bytes(2,"big") for d in degrees)
    k_stream = hkdf(k, info=info, length=32)

    aead = ChaCha20Poly1305(k_stream)
    nonce = hashlib.sha256(salt + k).digest()[:12]
    ciphertext = aead.encrypt(nonce, plaintext, salt)

    return {"salt": salt, "start": start, "eph_pub": eph_pub, "ciphertext": ciphertext, "k": k, "degrees": degrees}
