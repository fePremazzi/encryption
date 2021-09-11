# Algoritmo RSA

## Introdução

O RSA é um algoritmo de criptografia de dados, que deve o seu nome a três professores do Instituto de Tecnologia de Massachusetts (MIT), Ronald Rivest, Adi Shamir e Leonard Adleman, fundadores da atual empresa RSA Data Security, Inc., que inventaram este algoritmo — até a data (2008) a mais bem-sucedida implementação de sistemas de chaves assimétricas, e fundamenta-se em teorias clássicas dos números. É considerado um dos mais seguros, já que mandou por terra todas as tentativas de quebrá-lo. Foi também o primeiro algoritmo a possibilitar criptografia e assinatura digital e uma das grandes inovações em criptografia de chave pública.

## Software

Foi criado um script em Python para encriptar e decifrar qualquer que seja a frase utilizando o algoritmo RSA de criptografia. Para isso, é necessário apenas a mensagem que deseja ser encriptada, pois, todos os paramêtros iniciais necessários para o algoritmo funcionar, serão gerados aleatoriamente, gerando assim, chaves publicas e privadas e cada vez que o algoritmo for utilizado.

Algumas funções de ajuda foram criadas, como por exemplo, is_primo, gcd(greatest common divisor), is_coprimo, procura_E (encontrar qual a chave publica), mod_inverse (encontrar a chave privada para decifrar a frase)

```
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
```

Inicialmente são gerados alguns numeros primos para que a operação possa ser controlada o suficiente para que nao exija muito processamento da maquina.

```
min_prime = 2
max_prime = 100
cached_primes = [i for i in range(min_prime,max_prime) if is_prime(i)]
```

Após isso, são escolhidos aleatoriamente os valores de ```p``` e ```q```, a partir dos numeros primos que foram gerados nó código acima.

```
p = random.choice(cached_primes[1:])
q = None

procura_novamente = True
while procura_novamente:
    q = random.choice(cached_primes)
    if q < p and q > 7:
        procura_novamente = False
```

Após isso, são calculados os demais coeficientes para poder gerar as chaves pública e privada.
```
N = p*q
L = (p-1)*(q-1)

E = procura_E(L,N)
D = mod_inverse(E, L)
```

Portanto, a chave pública é Chave(E, N) e a chave privada é Chave(D, N).

Após isso, é criada a variavel com a mensagem a ser encriptada e as demais operações a serem feitas para encriptar e decifrar a frase.
```
msg = "\"The information security is of significant importance to ensure the privacy of communications\""
print("Mensagem a ser encriptada: ", msg)
msg_asc = [ord(c) for c in msg]

msg_encriptada = [(uni**E)%N for uni in msg_asc]
print("Mensagem encriptada: ", r''.join([chr(uni) for uni in msg_encriptada]))

msg_decifrada = [(uni**D)%N for uni in msg_encriptada]
print("Mensagem decifrada: ", ''.join([chr(uni) for uni in msg_decifrada]))
```

## Explicação em vídeo

O video de demonstracao do algoritmo de RSA pode ser encontrado no youtube atraves do link abaixo: 

https://www.youtube.com/