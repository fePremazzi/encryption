from collections import deque
import copy


class VigenereCypher():

    def __init__(self, key):
        self.key = key.upper()
        self.header = deque([chr(unicode) for unicode in range(65, 91)])
        self.header.append(' ')

    def encrypt(self, msg):
        msg = msg.upper()

        chave_completa = self._completa_chave(msg)

        encripted = []

        for col, lin in zip(msg, chave_completa):
            coluna = self.header.index(col)
            linha = self._shift_header(self.header.index(lin))
            encripted.append(linha[coluna])

        return encripted    

    def decrypt(self, msg) :
        msg = msg.upper()

        chave_completa = self._completa_chave(msg)

        decripted = []

        for col, lin in zip(msg, chave_completa):
            coluna = self._shift_header(self.header.index(lin)).index(col)
            decripted.append(self.header[coluna])


        return decripted  
    
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
    vegenere_cypher = VigenereCypher(key='ohayou')
    print('Encripting {}'.format('fellipe premazzi'))
    print('Encripted message: {}'.format(vegenere_cypher.encrypt('fellipe premazzi')))
    print('Decripted message: {}'.format(vegenere_cypher.decrypt(''.join(vegenere_cypher.encrypt('fellipe premazzi')))))
    
