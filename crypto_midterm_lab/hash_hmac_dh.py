#!/usr/bin/env python3
import hashlib, hmac, secrets, json

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def write(path, s):
    with open(path, "w") as f:
        f.write(s)

# Task 3
data = "Never trust, always verify.\n"
write("data.txt", data)
h1 = sha256_file("data.txt")
hmac1 = hmac.new(b"secretkey123", data.encode(), hashlib.sha256).hexdigest()

write("data_modified.txt", data.replace("verify", "verifx"))
hmac2 = hmac.new(b"secretkey123", open("data_modified.txt","rb").read(), hashlib.sha256).hexdigest()

write("task3_results.txt", f"""=== Task 3: Hash & HMAC ===
SHA-256(data.txt): {h1}
HMAC-SHA256(data.txt, key="secretkey123"): {hmac1}
HMAC-SHA256(data_modified.txt, key="secretkey123"): {hmac2}

Explanation:
HMAC changes after even a 1-letter edit because it authenticates content with a secret key.
""")
with open("task3_outputs.json","w") as f:
    json.dump({"sha256(data.txt)":h1, "hmac(data.txt)":hmac1, "hmac(data_modified.txt)":hmac2}, f, indent=2)

# Task 4: DH simulate with RFC 3526 group 14 (2048-bit), g=2
p_hex = (
    "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
    "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
    "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
    "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
    "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
    "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"
    "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
    "670C354E4ABC9804F1746C08CA18217C32905E462E36CE3B"
    "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9"
    "DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
    "15728E5A8AACAA68FFFFFFFFFFFFFFFF"
)
p = int(p_hex, 16); g = 2
a = secrets.randbits(256); A = pow(g, a, p)
b = secrets.randbits(256); B = pow(g, b, p)
sA = pow(B, a, p); sB = pow(A, b, p)
assert sA == sB
shared_hex = format(sA, "x")

write("task4_results.txt", f"""=== Task 4: Diffie-Hellman (Python) ===
Group: MODP 2048-bit (RFC 3526 group 14), g=2
Alice public A: {A}
Bob public B: {B}
Shared secrets equal: YES
Shared secret (hex, first 64 chars): {shared_hex[:64]}...
""")
print("Task 3 & 4 completed. See task3_results.txt and task4_results.txt")