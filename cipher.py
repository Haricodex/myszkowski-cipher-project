def get_order(key):
    sorted_key = sorted(list(enumerate(key)), key=lambda x: (x[1], x[0]))
    order = [0] * len(key)

    current = 0
    prev_char = None

    for i, (idx, char) in enumerate(sorted_key):
        if char != prev_char:
            current = i
        order[idx] = current
        prev_char = char

    return order


def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    cols = len(key)
    rows = (len(plaintext) + cols - 1) // cols

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    # Fill matrix row-wise
    k = 0
    for i in range(rows):
        for j in range(cols):
            if k < len(plaintext):
                matrix[i][j] = plaintext[k]
                k += 1

    order = get_order(key)
    ciphertext = ""

    for num in sorted(set(order)):
        for j in range(cols):
            if order[j] == num:
                for i in range(rows):
                    if matrix[i][j]:
                        ciphertext += matrix[i][j]

    return ciphertext


def decrypt(ciphertext, key):
    cols = len(key)
    rows = (len(ciphertext) + cols - 1) // cols

    order = get_order(key)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for num in sorted(set(order)):
        for j in range(cols):
            if order[j] == num:
                for i in range(rows):
                    if index < len(ciphertext):
                        matrix[i][j] = ciphertext[index]
                        index += 1

    plaintext = ""
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                plaintext += matrix[i][j]

    return plaintext