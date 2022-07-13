import velha

# Testes para jogos impossíveis 


def testeJogoImpossivel_1():
    assert velha.JogoDaVelha([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == -2


def testeJogoImpossivel_2():
    assert velha.JogoDaVelha([[2, 2, 2], [2, 2, 2], [2, 2, 2]]) == -2


def testeJogoImpossivel_3():
    assert velha.JogoDaVelha([[1, 1, 2], [2, 1, 1], [1, 0, 2]]) == -2


def testeJogoImpossivel_4():
    assert velha.JogoDaVelha([[2, 2, 0], [0, 2, 2], [1, 0, 1]]) == -2


def testeJogoImpossivel_5():
    assert velha.JogoDaVelha([[2, 2, 2], [1, 1, 1], [0, 0, 0]]) == -2


# Testes para jogos indefinidos


def testeJogoIndefinido_1():
    assert velha.JogoDaVelha([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == -1


def testeJogoIndefinido_2():
    assert velha.JogoDaVelha([[0, 0, 0], [1, 2, 1], [2, 1, 2]]) == -1


def testeJogoIndefinido_3():
    assert velha.JogoDaVelha([[1, 2, 0], [2, 1, 0], [2, 1, 0]]) == -1


# Testes para jogos empatados


def testeJogoEmpatado():
    assert velha.JogoDaVelha([[1, 2, 2], [2, 1, 1], [1, 1, 2]]) == 0


# Testes para jogos com X ganhador


def testeJogoVencedorX_1():
    assert velha.JogoDaVelha([[1, 0, 0], [0, 1, 2], [0, 2, 1]]) == 1


def testeJogoVencedorX_2():
    assert velha.JogoDaVelha([[0, 2, 0], [1, 1, 1], [2, 0, 2]]) == 1


def testeJogoVencedorX_3():
    assert velha.JogoDaVelha([[1, 2, 0], [1, 1, 2], [1, 2, 0]]) == 1


