from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

def node_keygen():
    priv = x25519.X25519PrivateKey.generate()
    pub = priv.public_key()
    return priv, pub

def encapsulate(pub):
    """生成会话密钥和封装"""
    eph_priv = x25519.X25519PrivateKey.generate()
    eph_pub = eph_priv.public_key()
    shared = eph_priv.exchange(pub)
    kdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b'GMK-KEM')
    k = kdf.derive(shared)
    return eph_pub.public_bytes_raw(), k

def decapsulate(priv, eph_pub_bytes):
    """解封装"""
    eph_pub = x25519.X25519PublicKey.from_public_bytes(eph_pub_bytes)
    shared = priv.exchange(eph_pub)
    kdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b'GMK-KEM')
    k = kdf.derive(shared)
    return k
