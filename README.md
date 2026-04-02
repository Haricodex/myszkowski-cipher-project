# myszkowski-cipher-project
# Myszkowski Cipher with Custom Hash

## 📌 Theory

### Myszkowski Cipher
The Myszkowski cipher is a transposition cipher where repeated letters in the key share the same column ranking. The plaintext is written row-wise and read column-wise based on key order.

### Custom Hash Function
We implemented a Polynomial Rolling Hash:

H(s) = Σ (s[i] * p^i) mod M

Where:
- p = 31 (base)
- M = 1e9 + 7 (prime modulus)

This ensures:
- Good distribution
- Efficient computation
- Avoids collisions better than simple sums

---

## ▶️ How to Run

```bash
python test.py
