import secrets
from .graph_utils import generate_graph, permute_graph, invert_permutation
from .kem import node_keygen

def keygen(n=50, p=0.1):
    """生成公私钥"""
    G0 = generate_graph(n, p)
    pi = list(range(n))
    secrets.SystemRandom().shuffle(pi)
    G_pub = permute_graph(G0, pi)
    pi_inv = invert_permutation(pi)

    node_privs, node_pubs = [], []
    for _ in range(n):
        priv, pub = node_keygen()
        node_privs.append(priv)
        node_pubs.append(pub)

    # 发布时对齐π
    pub_nodes = [None]*n
    for i in range(n):
        pub_nodes[pi[i]] = node_pubs[i]

    private = {"G0": G0, "pi": pi, "pi_inv": pi_inv, "node_privs": node_privs}
    public = {"G_pub": G_pub, "node_pubs": pub_nodes}
    return public, private
