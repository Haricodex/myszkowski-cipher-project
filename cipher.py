import math


def get_order(key):
    key = key.upper()
    indexed = list(enumerate(key))

    sorted_key = sorted(indexed, key=lambda x: (x[1], x[0]))

    order = [0] * len(key)
    rank = 0

    for i, (idx, char) in enumerate(sorted_key):
        if i > 0 and char != sorted_key[i - 1][1]:
            rank += 1
        order[idx] = rank

    return order


# 🔐 ENCRYPT (MYSZKOWSKI)
def encryptMessage(msg, key):
    msg = msg.replace(" ", "").upper()

    col = len(key)
    row = int(math.ceil(len(msg) / col))

    # padding
    fill_null = (row * col) - len(msg)
    msg += "_" * fill_null

    # create matrix
    matrix = [list(msg[i:i + col]) for i in range(0, len(msg), col)]

    order = get_order(key)

    cipher = ""

    for r in sorted(set(order)):
        cols_same = [j for j in range(col) if order[j] == r]

        if len(cols_same) == 1:
            j = cols_same[0]
            for i in range(row):
                cipher += matrix[i][j]
        else:
            for i in range(row):
                for j in cols_same:
                    cipher += matrix[i][j]

    return cipher


# 🔓 DECRYPT (MYSZKOWSKI)
def decryptMessage(cipher, key):
    col = len(key)
    row = int(math.ceil(len(cipher) / col))

    order = get_order(key)

    matrix = [['' for _ in range(col)] for _ in range(row)]

    index = 0

    for r in sorted(set(order)):
        cols_same = [j for j in range(col) if order[j] == r]

        if len(cols_same) == 1:
            j = cols_same[0]
            for i in range(row):
                matrix[i][j] = cipher[index]
                index += 1
        else:
            for i in range(row):
                for j in cols_same:
                    matrix[i][j] = cipher[index]
                    index += 1

    msg = ""
    for i in range(row):
        for j in range(col):
            msg += matrix[i][j]

    return msg.replace("_", "")