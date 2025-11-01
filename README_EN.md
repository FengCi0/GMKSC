# 🧩 GMK-SC: Graph Marker-KEM Stream Cipher  

[中文](README.md) | [ENGLISH](README_EN.md)

---

## 📘 Overview

**GMK-SC (Graph Marker-KEM Stream Cipher)** is an innovative asymmetric encryption algorithm that integrates the **Graph Isomorphism (GI)** problem with **Key Encapsulation Mechanism (KEM)** principles, enabling asymmetric key exchange and graph-based stream encryption.

### Key Features:
- 🌐 Uses graph structures as keyspace  
- 🔐 Employs node-level public/private key pairs (Marker-KEM)  
- 🧮 Generates keystream through random walks on graphs  
- ⚙️ Supports AEAD (e.g., ChaCha20-Poly1305)  
- 🚀 Designed for post-quantum research and prototype validation  

---

## 🧱 Project Structure

```
gmksc/
├─ src/gmksc/
│   ├─ graph_utils.py     # Graph generation and walks
│   ├─ kem.py             # Node-level KEM (X25519)
│   ├─ keygen.py          # Key generation (G₀ / G_pub)
│   ├─ encrypt.py         # Encapsulation + encryption
│   ├─ decrypt.py         # Decapsulation + decryption
│   └─ demo.py            # Demonstration script
│
├─ spec/
│   ├─ gmksc_v1_cn.md     # Chinese specification
│   └─ gmksc_v1_en.md     # English specification
│
├─ tests/
│   └─ test_roundtrip.py
│
├─ README.md
├─ README_EN.md
├─ LICENSE
└─ requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/YourName/gmksc.git
cd GMKSC
pip install -e .
```

---

## ▶️ Quick Demo

```bash
python -m gmksc.demo
```

Example output:
```
=== Demo GMK-SC ===
Graph nodes: 20
Salt: 30e7bb5044bd03ba794968b0
Start node: 3
Session key k: 5871d4e7ec515d75f9bcb0a2e0c914fd26012eea ...
Degrees: [4, 5, 4, 5, 4, 4, 3, 2, 4, 2, 3, 2, 4, 5, 2, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 3, 5, 3, 2, 4, 2, 4, 5, 3, 4, 2, 4, 5]
Ciphertext (hex): be8ce32b8aa742fff17908abe74471fd9893625a42bec5535f05721f63f7 ...
Recovered plaintext: Hello, Graph Marker-KEM Stream Cipher!
Success: OK
```

---

## 🧠 Algorithm Overview

1️⃣ **Key Generation (KeyGen)**  
Generate private graph G₀, random permutation π, public graph G_pub, and per-node keypairs.

2️⃣ **Encryption (Encaps + Encrypt)**  
Alice uses G_pub and a node’s public key to perform Marker-KEM encapsulation, generating a session key k.  
Then performs random walks on G_pub using k to derive the keystream for AEAD encryption.

3️⃣ **Decryption (Decaps + Decrypt)**  
Bob uses π⁻¹ to find the corresponding private node, decapsulates to recover k,  
and performs the same random walk on G₀ to reproduce the keystream for decryption.

---

## 📚 Specification

See also:  
- [📄 English Version (gmksc_v1_en.md)](spec/gmksc_v1_en.md)

---

## 📜 License
Apache License 2.0

---

## 🤝 Contributors
We welcome contributions from cryptography researchers and enthusiasts.  
Submit issues or pull requests to: [GitHub Repository](https://github.com/YourName/gmksc)

---
