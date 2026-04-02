def polynomial_hash(message, base=31, mod=10**9 + 7):
    hash_value = 0
    power = 1

    for char in message:
        hash_value = (hash_value + ord(char) * power) % mod
        power = (power * base) % mod

    return hash_value