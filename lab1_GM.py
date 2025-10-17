import string
from base64 import b64decode

alphabet = string.ascii_lowercase

def caesar_shift(s, k):
    out = []
    for ch in s:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            idx = ord(ch) - ord(base)
            out.append(chr(ord(base) + (idx - k) % 26))
        else:
            out.append(ch)
    return ''.join(out)

def brute_force_caesar(s):
    return {k: caesar_shift(s, k) for k in range(26)}

def xor_bytes(data, key_bytes):
    out = bytearray()
    for i, b in enumerate(data):
        out.append(b ^ key_bytes[i % len(key_bytes)])
    return bytes(out)

if __name__ == "__main__":
    # Task 1
    cipher1 = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
    brute1 = brute_force_caesar(cipher1)
    print("Task 1: Caesar brute-force results (k: plaintext):")
    for k, t in brute1.items():
        print(f"{k:>2}: {t}")
    print("\nSelected (k=14):", brute1[14])

    # Task 2 — Step 1
    cipher2 = "mznxpz"
    brute2 = brute_force_caesar(cipher2)
    print("\nTask 2 / Step 1: Caesar on 'mznxpz'")
    for k, t in brute2.items():
        if t.isalpha():
            print(f"{k:>2}: {t}")
    print("Selected (k=21):", brute2[21], "→ anagram of 'secure'")

    # Task 2 — Step 3 (XOR)
    b64 = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
    data = b64decode(b64)
    key = b"secure"
    pt = xor_bytes(data, key)
    print("\nTask 2 / Step 3: XOR-decrypted with key 'secure' →", pt.decode())
