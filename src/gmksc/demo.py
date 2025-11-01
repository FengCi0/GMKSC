import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gmksc.keygen import keygen
from gmksc.encrypt import encrypt
from gmksc.decrypt import decrypt

def demo():
    print("=== GMK-SC Non-Symmetric Demo ===")
    public, private = keygen(n=20, p=0.15)
    message = b"Hello, Graph Marker-KEM Stream Cipher!"
    packet = encrypt(public, message)
    recovered = decrypt(private, packet)
    print("Message:", message)
    print("Ciphertext:", packet["ciphertext"].hex())
    print("Recovered:", recovered.decode())
    if recovered == message:
        print("✅ Success")

if __name__ == "__main__":
    demo()
