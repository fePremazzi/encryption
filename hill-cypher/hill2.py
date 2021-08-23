import numpy as np

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


cripted_msg = 'SŢÕVŝØOƙóMŢÏEŰá'
key_to_encript = [[1,0,0], [1,3,1], [1,2,0]]
key_to_decrypt = np.linalg.inv(key_to_encript)
unicode_chars = [ord(char) for char in cripted_msg]

chunks = list(split(unicode_chars, int(len(unicode_chars)/3)))

extended_unicode = []

decripted_unicode = [extended_unicode.extend(np.dot(key_to_decrypt, chunk)) for chunk in chunks]


decripted_msg = [chr(int(u)) for u in extended_unicode]
print(''.join(decripted_msg))