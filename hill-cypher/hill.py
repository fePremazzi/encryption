import numpy as np
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
alphabet = {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26,
}
cm = [[1,0,0], [1,3,1], [1,2,0]]#[[1,0,0], [1,3,1], [1,2,0]] ---[[2,3], [5,7]]
cm_inverse = np.linalg.inv(cm)%26 * 2
print(cm_inverse)
msg="oifellipe".upper()
to_matrix = []
for s in msg:
    to_matrix.append(alphabet.get(s))

chunks = list(split(to_matrix, int(len(to_matrix)/3)))
print(chunks)
cripted = []
cripted_msg = []
for chunk in chunks:
    bs = np.dot(cm_inverse, chunk)%26
    print(bs)
    for b in bs:
        cripted_msg.append(alphabet.get(b))

print(cripted_msg)



# matrix de criptografia
# cm = [[1,0,0], [1,3,1], [1,2,0]]
# cm_inverse = np.linalg.inv(cm)
# det_cmi = np.linalg.det(cm_inverse)
# I = -2

# decrypt_matrix = cm_inverse % 26

# print("t: " + str((det_cmi*(-2)%26)))
# print(decrypt_matrix)
# print(det_cmi)
# print(str(-0.5%26))
# print(int("a"))