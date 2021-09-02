from collections import deque
import copy


class VigenereCypher():

    def __init__(self, key):
        self.key = key.upper()
        self.header = deque([chr(unicode) for unicode in range(32, 91)])

    def encrypt(self, msg):
        msg = msg.upper()

        chave_completa = self._completa_chave(msg)

        encripted = []

        for col, lin in zip(msg, chave_completa):
            coluna = self.header.index(col)
            linha = self._shift_header(self.header.index(lin))
            encripted.append(linha[coluna])

        return ''.join(encripted)

    def decrypt(self, msg) :
        msg = msg.upper()

        chave_completa = self._completa_chave(msg)

        decripted = []

        for col, lin in zip(msg, chave_completa):
            coluna = self._shift_header(self.header.index(lin)).index(col)
            decripted.append(self.header[coluna])


        return ''.join(decripted)
    
    def _shift_header(self, n):
        header = copy.copy(self.header)
        i = 0
        while i < n:
            header.append(header.popleft())
            i += 1
        return list(header)

    def _completa_chave(self, msg):
        chave_completa = ''
        for i in range(len(msg)):
            chave_completa += self.key[i%len(self.key)]
        
        return chave_completa  



if __name__ == '__main__':
    frase = 'O video de demonstracao da cifra de vigenere pode ser encontrada no youtube atraves do link abaixo'
    vigenere_cypher = VigenereCypher(key='FTT Salvador Arena')

    print('Encripting {}'.format(frase))

    encripted_frase = vigenere_cypher.encrypt(frase)
    print('Encripted message: {}'.format(encripted_frase))

    decripted_frase = vigenere_cypher.decrypt(encripted_frase)
    print('Decripted message: {}'.format(decripted_frase))
    
