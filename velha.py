def JogoDaVelha(matriz):
    qntd_X, qntd_O, qntd_branco = QuantidadesTermos(matriz)
    ganhador = VerificaGanhador(matriz)
    if qntd_branco == 9:
        return -1
    elif qntd_X > qntd_O + 1 or qntd_O > qntd_X or ganhador == 'impossivel':
        return -2
    elif ganhador == "indefinidoOUempatado":
        if qntd_branco == 0:
            return 0
        else:
            return -1
    else:
        return ganhador


def QuantidadesTermos(matriz):
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


def VerificaGanhador(matriz):
    contadorGanhadores = 0
    ganhador = 0
    for i in range(0, 3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2]:
            if matriz[i][0] != 0:
                ganhador = matriz[i][0]
                contadorGanhadores += 1
        if matriz[0][i] == matriz[1][i] == matriz[2][i]:
            if matriz[0][i] != 0:
                ganhador = matriz[0][i]
                contadorGanhadores += 1
    diagonalPrincipal = matriz[0][0] == matriz[1][1] == matriz[2][2]
    diagonalSecundaria = matriz[0][2] == matriz[1][1] == matriz[2][0]
    if diagonalPrincipal or diagonalSecundaria:
        if matriz[1][1] != 0:
            ganhador = matriz[1][1]
            contadorGanhadores += 1
    if contadorGanhadores == 0:
        return "indefinidoOUempatado"
    elif contadorGanhadores > 1:
        return 'impossivel'
    else:
        return ganhador

# Finalizado
