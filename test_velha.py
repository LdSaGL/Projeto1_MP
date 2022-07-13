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
