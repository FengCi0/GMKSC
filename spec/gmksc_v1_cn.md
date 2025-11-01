# 📘 GMK-SC v1 中文规范文档  


## 一、概述

**GMK-SC（Graph Marker-KEM Stream Cipher）** 是一种基于**图同构问题（Graph Isomorphism, GI）** 的**非对称流加密算法**。  
它将图结构视为密钥空间，通过**节点级公私钥系统（Marker-KEM）**建立加密通道，并利用图上**随机游走（Random Walk）**生成密钥流，实现高安全性、抗量子攻击的通信机制。

算法名称：**GMK-SC（Graph Marker-KEM Stream Cipher）**  
版本：**v1.0 (Draft)**  
发布日期：2025-11-01  

---

## 二、核心思想

GMK-SC 的安全性建立在两个主要难题上：

1. **图同构问题 (GI Problem)**：已知两张图 G₁ 与 G₂，判断它们是否同构是 NP 问题，目前没有多项式时间算法。GMK-SC 使用同构关系作为密钥陷门。
2. **伪随机游走密钥流 (PRW Keystream)**：在图上基于节点度数与结构进行确定性随机游走，生成与密钥绑定的加密流。

通过将 GI 与 KEM 机制结合，GMK-SC 在加密时只需公钥图 G_pub，而解密需要私钥图 G_priv 及其映射 π⁻¹，从而实现非对称安全性。

---

## 三、算法结构

### 3.1 密钥生成（KeyGen）

输入：节点数 `n`，边生成概率 `p`  
输出：`(PublicKey, PrivateKey)`

过程：
1. 生成随机图 **G₀(V, E)**。  
2. 生成随机置换 **π: V → V'**，并计算 **G_pub = π(G₀)**。  
3. 为每个节点生成一对节点级密钥对：  
   `MarkerKEM.KeyGen()` → (pkᵢ, skᵢ)
4. 公钥：`{G_pub, {pkᵢ}}`  
   私钥：`{G₀, {skᵢ}, π⁻¹}`

---

### 3.2 加密（Encaps + Encrypt）

输入：公钥图 G_pub，明文 M，随机盐值 S。  
输出：密文 C = {Enc_KEM, Ciphertext, Salt, StartNode}

过程：
1. 通过盐值 S 和明文长度 L，计算起点节点编号：  
   `start = H(S || L) mod |V(G_pub)|`
2. 在起点节点执行 KEM 封装：  
   `(Enc_KEM, k) = MarkerKEM.Encaps(pk_start)`
3. 使用 k 作为种子，对图执行伪随机游走：  
   `degrees = Walk(G_pub, start, len(M), seed=k)`
4. 根据度数序列派生密钥流：  
   `keystream = Hash(k || degrees)`
5. 加密：  
   `Cₜ = M ⊕ keystream`

最终输出：
```
C = {
  Enc_KEM: 加密封装结果,
  Salt: 盐值,
  StartNode: 起点节点索引,
  Ciphertext: 密文字节流
}
```

---

### 3.3 解密（Decaps + Decrypt）

输入：私钥 `{G₀, π⁻¹, {skᵢ}}`，收到的 C。  
输出：明文 M。

过程：
1. 通过 π⁻¹ 计算起点节点在 G₀ 中的索引。  
2. 使用对应的 sk_start 解封装恢复会话密钥：  
   `k = MarkerKEM.Decaps(sk_start, Enc_KEM)`
3. 重复相同的随机游走生成度数序列：  
   `degrees = Walk(G₀, start, len(Cₜ), seed=k)`
4. 重建密钥流并解密：  
   `M = Cₜ ⊕ Hash(k || degrees)`

---

## 四、符号说明

| 符号 | 含义 |
|------|------|
| G₀ | 私钥图 (Private Graph) |
| G_pub | 公钥图 (Public Graph) |
| π | 图同构置换函数 |
| π⁻¹ | 反置换 (恢复同构关系) |
| pkᵢ / skᵢ | 第 i 个节点的公/私钥 |
| Enc_KEM | 节点级密钥封装结果 |
| k | 会话密钥 (Session Key) |
| S | 随机盐值 (Salt) |
| degrees | 随机游走生成的节点度序列 |
| keystream | 密钥流 (由 k 和 degrees 生成) |

---

## 五、安全性分析

1. **非对称性保证**：解密需要 π⁻¹ 与节点私钥，无法从 G_pub 推导。  
2. **随机性增强**：盐值 + PRNG 种子确保密文唯一性。  
3. **抗量子攻击潜力**：GI 问题的复杂度高于数论问题（RSA/ECC）。  
4. **不可逆性**：无法由 keystream 推回 k 或图结构。  

---

## 六、性能与应用

- 节点数量 `n ≈ 100–500` 可在毫秒级生成密钥。  
- 可扩展为 AEAD（如 ChaCha20-Poly1305）模式。  
- 可用于后量子安全通信、分布式密钥管理、区块链签名协议等。

---

## 七、未来方向

- 改进图结构选择（支持正则图与随机几何图）。  
- 实现基于哈希的图映射防碰撞机制。  
- 研究可证明安全性模型（IND-CCA 安全）。  
- 发布 GMK-SC v2，加入抗量子签名模块。

---

## 八、参考实现

Python 参考实现：`src/gmksc/` 目录  
运行示例：
```bash
python -m gmksc.demo
```

输出：
```
=== GMK-SC Demo ===
Salt: e08a215290332774
Start node: 19
Session key: fa97...d26e
Ciphertext: e39754d2a9c6aee9...
Recovered plaintext: Hello Graph Cipher!
```

---

## 九、许可

GMK-SC 在 **Apache License 2.0** 下开源。  
版权所有 © 2025 GMK-SC Research Group.

