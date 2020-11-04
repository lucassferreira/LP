import re

def inverte(palavra):
    if re.match(r'^\w+$', palavra):
        return palavra[::-1]
    return palavra

frase = 'O espaço entre a teoria e a prática não é tão grande como é, a teoria na prática.'
invertida = ''.join(inverte(palavra) for palavra in re.split(r'(\W+)', frase))
print (frase)
print(invertida)