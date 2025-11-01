import hashlib, hmac
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from .graph_utils import walk_degrees
from .kem import decapsulate

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

def decrypt(private, packet):
    G0 = private["G0"]
    pi_inv = private["pi_inv"]
    node_privs = private["node_privs"]

    start_pub = packet["start"]
    start_priv = pi_inv[start_pub]

    eph_pub = packet["eph_pub"]
    salt = packet["salt"]
    ciphertext = packet["ciphertext"]

    k = decapsulate(node_privs[start_priv], eph_pub)
    degrees = walk_degrees(G0, start_priv, len(ciphertext) - 16, k)
    info = b",".join(d.to_bytes(2,"big") for d in degrees)
    k_stream = hkdf(k, info=info, length=32)

    nonce = hashlib.sha256(salt + k).digest()[:12]
    aead = ChaCha20Poly1305(k_stream)
    plaintext = aead.decrypt(nonce, ciphertext, salt)
    return plaintext
