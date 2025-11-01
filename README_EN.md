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
cd gmksc
pip install -e .
```

---

## ▶️ Quick Demo

```bash
python -m gmksc.demo
```

Example output:
```
=== GMK-SC Non-Symmetric Demo ===
Message: b'Hello, Graph Marker-KEM Stream Cipher!'
Ciphertext: 3a8f...da92...
Recovered: Hello, Graph Marker-KEM Stream Cipher!
✅ Success
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
- [📄 Chinese Version (gmksc_v1_cn.md)](spec/gmksc_v1_cn.md)  
- [📄 English Version (gmksc_v1_en.md)](spec/gmksc_v1_en.md)

---

## 📜 License
Apache License 2.0

---

## 🤝 Contributors
We welcome contributions from cryptography researchers and enthusiasts.  
Submit issues or pull requests to: [GitHub Repository](https://github.com/YourName/gmksc)

---
