a = []
for i in range(65, 91):
    a.append(chr(i))

p = input("Enter the Plain Text: ")

k = [[0, 0], [0, 0]]
for i in range(0, 2):
    for j in range(0, 2):
        k[i][j] = int(input("Enter: "))

# Ensure the length of p is even
if len(p) % 2 != 0:
    p = p + 'X'

# Divide the plain text into pairs
pairs = [p[i:i+2] for i in range(0, len(p), 2)]

print("Plain Text Pairs:", pairs)
# ... (previous code)

# Function to multiply a 2x2 matrix with a 2x1 matrix
def matrix_multiply(matrix1, matrix2):
    result = [0, 0]
    for i in range(2):
        for j in range(1):
            result[i] += matrix1[i][j] * matrix2[j]
    return result

# Encrypt each pair using the key matrix k
encrypted_pairs = []
for pair in pairs:
    # Convert pair to a 2x1 matrix (column vector)
    pair_matrix = [ord(pair[0]) - 65, ord(pair[1]) - 65]

    # Multiply key matrix with pair matrix
    result_matrix = matrix_multiply(k, pair_matrix)

    # Convert back to characters
    encrypted_pair = ''.join(chr(result + 65) for result in result_matrix)

    encrypted_pairs.append(encrypted_pair)

print("Encrypted Pairs:", encrypted_pairs)
