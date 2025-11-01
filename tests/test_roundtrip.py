import sys
import os
import pytest

# Add the src directory to the Python path to find the gmksc module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gmksc import keygen, encrypt, decrypt

def test_roundtrip():
    # 1️⃣ 生成密钥
    pub, priv = keygen(n=30, p=0.1)

    # 2️⃣ 测试明文
    plaintext = "Graph Cipher Roundtrip Test".encode('utf-8')

    # 3️⃣ 加密
    enc_packet = encrypt(pub, plaintext)

    # 4️⃣ 解密
    recovered = decrypt(priv, enc_packet)

    # 5️⃣ 验证结果
    assert recovered == plaintext, "Decryption failed — plaintext mismatch!"
    print("Test Passed — Roundtrip successful!")

if __name__ == "__main__":
    test_roundtrip()
