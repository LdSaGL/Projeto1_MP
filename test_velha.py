#import pytest
import velha

def teste():
    assert velha.JogoDaVelha([[2, 0, 1], [0, 2, 0], [1, 0, 1]]) == -1