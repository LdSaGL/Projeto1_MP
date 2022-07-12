def JogoDaVelha (matriz):
    qntd_X, qntd_O, qntd_branco = PosicoesJogo(matriz)
    ganhador = VerificaGanhador(matriz)
    if qntd_X >= qntd_O + 2 or qntd_O > qntd_X:
        return -2
    elif ganhador == 0:
        if qntd_branco == 0:
            return 0
        else:
            return -1
    else:
        return ganhador

def PosicoesJogo (matriz):
    qntd_X = 0
    qntd_O = 0
    for i in matriz:
        for j in i:
            if j == 1:
                qntd_X += 1
            elif j == 2:
                qntd_O += 1
    qntd_branco = 9 - qntd_X - qntd_O
    return qntd_X, qntd_O, qntd_branco


def VerificaGanhador (matriz):
    for i in range(0, 3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2]:
            if matriz[i][0] != 0:
                return matriz[i][0]
        if matriz[0][i] == matriz[1][i] == matriz[2][i]:
            if matriz[0][i] != 0:
                return matriz[0][i]
    if matriz[0][0] == matriz[1][1] == matriz[2][2] or matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[1][1] != 0:
            return matriz[1][1]
    return 0

entrada = [[1, 0, 0], 
           [2, 1, 2], 
           [0, 0, 1]]

print(JogoDaVelha(entrada))


