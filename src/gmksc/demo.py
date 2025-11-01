import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gmksc.keygen import keygen
from gmksc.encrypt import encrypt
from gmksc.decrypt import decrypt

def demo():
    print("=== Demo GMK-SC ===")
    public, private = keygen(n=20, p=0.15)
    
    message = "Hello, Graph Marker-KEM Stream Cipher!".encode('utf-8')
    packet = encrypt(public, message)
    
    recovered = decrypt(private, packet)

    print(f"Graph nodes: {len(public['G_pub'])}")
    print(f"Salt: {packet['salt'].hex()}")
    print(f"Start node: {packet['start']}")
    print(f"Session key k: {packet['k'].hex()[:40]} ...")
    print(f"Degrees: {packet['degrees']}")
    print(f"Ciphertext (hex): {packet['ciphertext'].hex()[:60]} ...")
    print(f"Recovered plaintext: {recovered.decode('utf-8')}")

    if recovered == message:
        print("Success: OK")

if __name__ == "__main__":
    demo()
