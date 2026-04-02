def custom_hash(message):
    h = 0
    for ch in message:
        h = (h * 37 + ord(ch)) % 1000000007
    return h