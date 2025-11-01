"""
GMK-SC: Graph Marker-KEM Stream Cipher
--------------------------------------
A novel asymmetric encryption algorithm based on Graph Isomorphism and Marker-KEM.

This package provides:
- Graph-based key generation
- Marker-KEM (node-level key encapsulation)
- Graph random walk encryption/decryption
"""

__version__ = "1.0.0"
__author__ = "FengCi0"
__license__ = "Apache-2.0"

from .keygen import keygen
from .encrypt import encrypt
from .decrypt import decrypt
