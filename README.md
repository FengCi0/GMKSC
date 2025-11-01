# 🧩 GMK-SC：基于图同构的非对称流加密算法  

[中文](README.md) | [ENGLISH](README_EN.md)

---

## 📘 简介

**GMK-SC（Graph Marker-KEM Stream Cipher）** 是一种创新的加密算法，  
将**图同构（Graph Isomorphism）问题**与**公钥封装机制（KEM）**相结合，  
实现非对称密钥交换 + 图上流式加密。  

该算法的特点：
- 🌐 使用图结构作为密钥空间  
- 🔐 采用节点级公私钥（Marker-KEM）  
- 🧮 在图上进行随机游走生成密钥流  
- ⚙️ 支持 AEAD（如 ChaCha20-Poly1305）  
- 🚀 可用于后量子方向的研究与原型验证  

---

## 🧱 项目结构

```
gmksc/
├─ src/gmksc/
│   ├─ graph_utils.py     # 图生成、游走算法
│   ├─ kem.py             # 节点级 KEM (X25519)
│   ├─ keygen.py          # 公钥图 / 私钥图生成
│   ├─ encrypt.py         # 封装 + 加密
│   ├─ decrypt.py         # 解封装 + 解密
│   └─ demo.py            # 示例程序
│
├─ spec/
│   ├─ gmksc_v1_cn.md     # 中文规范文档
│   └─ gmksc_v1_en.md     # English version
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

## ⚙️ 安装

```bash
git clone https://github.com/FengCi0/GMKSC.git
cd GMKSC
pip install -e .
```

---

## ▶️ 运行示例

```bash
python -m gmksc.demo
```

输出示例：
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

## 🧠 算法简介

1️⃣ **密钥生成 (KeyGen)**  
 生成私钥图 G₀、随机置换 π、公钥图 G_pub，以及每节点的公私钥。  

2️⃣ **加密 (Encaps + Encrypt)**  
 Alice 使用 G_pub 与起点节点公钥执行 Marker-KEM 封装，生成会话密钥 k；  
 再在图上执行随机游走，用 k 生成密钥流并对称加密明文。  

3️⃣ **解密 (Decaps + Decrypt)**  
 Bob 根据 π⁻¹ 找到起点对应的私钥节点，解封装恢复 k；  
 使用相同算法生成密钥流，完成解密。  

---

## 📚 技术规范

详见：
- [📄 中文版规范 (gmksc_v1_cn.md)](spec/gmksc_v1_cn.md)

---

## 📜 许可协议
Apache License 2.0

---

## 🤝 贡献者 | Contributors
欢迎研究者、密码学爱好者共同完善 GMK-SC。  
Issues / Pull Requests 欢迎提交到：[GitHub Repository](https://github.com/FengCi0/GMKSC)

---