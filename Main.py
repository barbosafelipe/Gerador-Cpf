'''
Objetivo criar cpf validos
'''
cpflist = []
while True:
    try:
        aleatorio = str(input('Escolha nove numeros aleatorios :')) #Entrada de 9 numeros aleatorios
        if len(aleatorio) > 9 or len(aleatorio) < 9:
            print('Só pode ser nove numeros ! ')
        else:
            break
    except:
        pass

for x in aleatorio:
    x = int(x)
    cpflist.append(x)


#Criando o primeiro Digito e adicionando a lista do cpf

pValidador = (cpflist[0] * 10 ) + (cpflist[1] * 9 ) + (cpflist[2] * 8 ) + (cpflist[3] * 7 ) + (cpflist[4] * 6 )\
    + (cpflist[5] * 5 ) + (cpflist[6] * 4 ) + (cpflist[7] * 3 ) + (cpflist[8] * 2 )

pDigito = (pValidador * 10) % 11
cpflist.append(pDigito)

#Segundo Digito criando
sValidador = (cpflist[0] * 11 ) + (cpflist[1] * 10 ) + (cpflist[2] * 9 ) + (cpflist[3] * 8 ) + (cpflist[4] * 7 )\
    + (cpflist[5] * 6 ) + (cpflist[6] * 5 ) + (cpflist[7] * 4 ) + (cpflist[8] * 3 ) + (cpflist[9] * 2)

sDigito = (sValidador *10) % 11
cpflist.append(sDigito)

contador = 0
tcont = 0
for c in cpflist:
    print(f'{c}', end='')
    contador += 1
    if contador == 3 and tcont < 2:
        print('.' , end='')
        contador = 0
        tcont += 1
    elif tcont == 2 and contador == 3:
        print('-',end='')
