import secrets, hashlib

def sha256(b): return hashlib.sha256(b).digest()

def generate_graph(n, p=0.1):
    """生成随机无向图"""
    """"""
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if secrets.randbelow(1000)/1000 < p:
                g[i].append(j)
                g[j].append(i)
    return g

def permute_graph(G, pi):
    """根据置换 π 生成同构图"""
    n = len(G)
    new = [[] for _ in range(n)]
    for i in range(n):
        new_i = pi[i]
        for nei in G[i]:
            new[new_i].append(pi[nei])
    return new

def invert_permutation(pi):
    """计算置换的逆"""
    inv = [0]*len(pi)
    for i,v in enumerate(pi): inv[v] = i
    return inv

def walk_degrees(G, start, steps, seed):
    """从起点出发，用seed控制伪随机游走，记录每步的度"""
    state = start
    degs = []
    for i in range(steps):
        degs.append(len(G[state]))
        if len(G[state]) == 0:
            continue
        r = int.from_bytes(sha256(seed + i.to_bytes(4,'big')), 'big')
        state = G[state][r % len(G[state])]
    return degs
