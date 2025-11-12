#!/usr/bin/env bash
set -euo pipefail

# ===== Applied Cryptography – Midterm Lab (Weeks 1–4) =====
# This script assumes: OpenSSL 1.1+ installed
# It creates outputs in ./outputs/

mkdir -p outputs

echo "== Task 1A: AES-128-CBC encrypt secret.txt with passphrase =="
# Choose a passphrase interactively or export PASSPHRASE beforehand.
# Example (INSECURE for demo): export PASSPHRASE="MyStrongPassw0rd!"
: "${PASSPHRASE:?Set PASSPHRASE environment variable}"
openssl enc -aes-128-cbc -salt -pbkdf2 -iter 100000 -in secret.txt -out outputs/secret.enc -pass env:PASSPHRASE

echo "== Task 1B: Decrypt and verify =="
openssl enc -d -aes-128-cbc -pbkdf2 -iter 100000 -in outputs/secret.enc -out outputs/secret.decrypted.txt -pass env:PASSPHRASE
echo "Original:"
cat secret.txt
echo "Decrypted:"
cat outputs/secret.decrypted.txt
diff -u secret.txt outputs/secret.decrypted.txt && echo "Match ✔" || echo "Mismatch ✗"

echo "== Task 2A: ECC generate keys (prime256v1) =="
openssl ecparam -name prime256v1 -genkey -noout -out outputs/ecc_private.pem
openssl ec -in outputs/ecc_private.pem -pubout -out outputs/ecc_public.pem

echo "== Task 2B: Sign and verify ecc.txt =="
# SHA256 ECDSA signature
openssl dgst -sha256 -sign outputs/ecc_private.pem -out outputs/ecc.sig ecc.txt
# Verify
openssl dgst -sha256 -verify outputs/ecc_public.pem -signature outputs/ecc.sig ecc.txt

echo "== Task 3A: SHA-256 hash (also provided via Python) =="
openssl dgst -sha256 data.txt | tee outputs/data_sha256_openssl.txt

echo "== Task 3B: HMAC-SHA256 with key 'secretkey123' =="
# Use -mac HMAC with -macopt key:value (OpenSSL 1.1+)
openssl dgst -sha256 -mac HMAC -macopt key:secretkey123 data.txt | tee outputs/data_hmac_sha256_openssl.txt

echo "== Task 3C: Integrity check (modify one letter) =="
cp data.txt outputs/data_modified.txt
# Simple substitution: change 'verify' -> 'verifx'
sed -i 's/verify/verifx/' outputs/data_modified.txt
openssl dgst -sha256 -mac HMAC -macopt key:secretkey123 outputs/data_modified.txt | tee outputs/data_modified_hmac_sha256_openssl.txt
echo "Note: HMAC changed => integrity/authenticity breach detected."

echo "== Task 4A: Diffie-Hellman via OpenSSL (optional alternate to Python) =="
# Generate DH params (can be slow). You can also use a pre-defined group with -2.
# openssl dhparam -out outputs/dhparam.pem 2048
# For speed in class, we skip generation and use built-in group via pkeyparam where supported.
# OpenSSL modern approach uses 'pkey' for DH; many systems still use 'genpkey' + 'pkey'.
# Example (OpenSSL 3):
#   openssl genpkey -genparam -algorithm DH -pkeyopt dh_paramgen_prime_len:2048 -out outputs/dhparams.pem
#   openssl genpkey -paramfile outputs/dhparams.pem -out outputs/alice_dhkey.pem
#   openssl pkey -in outputs/alice_dhkey.pem -pubout -out outputs/alice_dhpub.pem
#   openssl genpkey -paramfile outputs/dhparams.pem -out outputs/bob_dhkey.pem
#   openssl pkey -in outputs/bob_dhkey.pem -pubout -out outputs/bob_dhpub.pem
#   openssl pkeyutl -derive -inkey outputs/alice_dhkey.pem -peerkey outputs/bob_dhpub.pem -out outputs/alice_shared.bin
#   openssl pkeyutl -derive -inkey outputs/bob_dhkey.pem -peerkey outputs/alice_dhpub.pem -out outputs/bob_shared.bin
#   cmp outputs/alice_shared.bin outputs/bob_shared.bin && echo "Shared secrets match ✔" || echo "Mismatch ✗"

echo "All done."