'''Help for rex bot'''


def genpass():

    '''Gera uma pass aleatória de 10 caracteres dentro das normas dos Aquinos
Ignora caracteres no nome do utilizador caso o givenname não seja atribuido.

A pass é enviada por mensagem privada.

Exemplo: !genpass - Returns: qC/T40dQ#5 
Caracteres ignorados: w, i, l, s, o, n

Exemplo 2: !genpass wilsonmarques - Returns: qC/T40dQ#5
Caracteres ignorados: w, i, l, s, o, n, m, a, r, q, e

Boa sorte a decorar isto! :D'''

    print(genpass.__doc__)


genpass()
