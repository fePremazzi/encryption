import random

def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def procura_E(L,N):
    for numero in range(2, L):
        if is_coprime(numero, L) and is_coprime(numero, N):
            return numero

def mod_inverse(E, L):     
    for x in range(1, L):
        if (((E%L) * (x%L)) % L == 1):
            return x
    return -1


min_prime = 2
max_prime = 100
cached_primes = [i for i in range(min_prime,max_prime) if is_prime(i)]

p = random.choice(cached_primes[1:])
q = None

procura_novamente = True
while procura_novamente:
    q = random.choice(cached_primes)
    if q < p and q > 7:
        procura_novamente = False

N = p*q
L = (p-1)*(q-1)

E = procura_E(L,N)
D = mod_inverse(E, L)

print("p: ", p)
print("q: ", q)
print("N: ", N)
print("L: ", L)
print("E: ", E)
print("D: ", D)

print("Chave publica: ({0},{1})".format(E,N))
print("Chave privada: ({0},{1})".format(D,N))

msg = "\"The information security is of significant importance to ensure the privacy of communications\""
print("Mensagem a ser encriptada: ", msg)
msg_asc = [ord(c) for c in msg]

msg_encriptada = [(uni**E)%N for uni in msg_asc]
print("Mensagem encriptada: ", r''.join([chr(uni) for uni in msg_encriptada]))

msg_decifrada = [(uni**D)%N for uni in msg_encriptada]
print("Mensagem decifrada: ", ''.join([chr(uni) for uni in msg_decifrada]))