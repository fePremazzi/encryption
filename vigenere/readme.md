# Cifra de Vigenere

## Introdução

A cifra de vigenere é uma das mais famosas cifras polialfabéticas que temos a disposição. Ela consiste em uma matriz alfabética onde cada uma das linhas dessa matriz é a linha anterior com o um deslocamento "n" aplicado e asism por diante. No fim da matriz a primeira letra da ultima deve ser a ultima letra da primeira linha. Além disso, é necessário uma chave para encriptografar e decriptografar a frase desejada. Segue abaixo uma matriz de vigenere de 26 letras indo de A até Z.

![Matriz de vigenere](matriz.png)

Essa matriz pode ser composta de qualquer alfabeto desde que seja quadrada, ou seja:

n_colunas = n_linhas

A criptografia é feita da seguinte maneira: na coluna e marcado o caractere da frase a ser encriptado e na linha é marcado o caractere da chave e, traçando as linhas de intersecção da linha com a coluna é possível encontrar o caractere cifrado. Veja o exemplo abaixo:

Frase para criptografar: ATACARBASESUL 

Escolhenda a chave "LIMAO" é necessário autocompletar a chave para ser do mesmo tamanho da frase, portanto:

Chave: LIMAOLIMAOLIM

Fazendo o processode intersecção é possivel chegar na seguinte frase cifrada:

Texto cifrado: 	LBMCOCJMSSDCX

## Software

Foi criado uma classe chamada `VigenereCypher` em que e necessário passar no construtor do objeto qual será a chave de criptografia. Esta classe contem dois métodos de acesso "público": `encrypt` e `decrypt`, fazedo o processar de criptografar e decriptografar a fraser, tendo ambos como parametro qual a frase a ser criptografa e decriptografada.

Além disso, diferente da matriz apresentada na seção de Introdução contendo um alfabeto de 26, este algoritmo foi desenvolvido para que suportasse um alfabeto masi extenso. Ele foi construído para que pudesse se adaptar de acordo com o usuário. Como um afabaeto padrão, ele contém os caracteres representados pelos unicode 32(" " espaço em branco) até o caractere 90("Z") e, neste caso sendo construída uma matriz quadrada de 59x59.

Segue abaixo um exemplo de uso:
```
    frase = 'O video de demonstracao da cifra de vigenere pode ser encontrada no youtube atraves do link abaixo'
    vigenere_cypher = VigenereCypher(key='FTT Salvador Arena')

    print('Encripting {}'.format(frase))

    encripted_frase = vigenere_cypher.encrypt(frase)
    print('Encripted message: {}'.format(encripted_frase))

    decripted_frase = vigenere_cypher.decrypt(encripted_frase)
    print('Decripted message: {}'.format(decripted_frase))
```

E, como saída no console temos:

```
Encripting O video de demonstracao da cifra de vigenere pode ser encontrada no youtube atraves do link abaixo
Encripted message: :TOI<+@V*.O;E3F8F:=:<AGA5<A,==R'R.8AAB@EF+C@A9C;EAJ/EA0G<OF:C<**OEOAP9H:@;> 9:C<<.GRD5R6<46T:B9/IJ
Decripted message: O VIDEO DE DEMONSTRACAO DA CIFRA DE VIGENERE PODE SER ENCONTRADA NO YOUTUBE ATRAVES DO LINK ABAIXO
```

Importante comentar que, a matriz nao é montada previamente, ou seja, ela é montada durante encriptação e, nao é montada inteira, devido a cada linha ser um deslocamento da linha anterior em 1 casa, podemos dizer que é uma cifra de césar da linah anterior de deslocamento 1 e por isso a linha deslocada é calculada em tempo de execução. Para mais detalhes, ver o video da demonstração.

## Explicação em vídeo

O video de demonstracao da cifra de vigenere pode ser encontrada no youtube atraves do link abaixo: 