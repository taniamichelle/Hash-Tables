import time
import hashlib


n = 1000000
key = b"STR"

for _ in range(10):
    print(hash(key)) # python's built-in 'hash()' function
print("\n")

for _ in range(10):
    print(hashlib.sha256(key)) # sha256 hash function
print("\n")

for _ in range(10):
    print(hashlib.sha256(key).hexdigest()) # enable visualization of hash
print("\n")

for _ in range(10):
    print(int(hashlib.sha256(key).hexdigest(), 16)) # enable visualization of 16 digits of hash
print("\n")