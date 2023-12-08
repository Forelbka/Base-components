from functools import lru_cache
from math import ceil

def moves(h):
    """
    Возвращает все доступные ходы
    """
    a, b = h
    return (a+1, b+2), (a+2, b+1), (a*2, b), (a, b*2)

@lru_cache(None)
def game(h):
    """
    Рекурсивная функция, проверяющая кто победит при данной входной куче
    """
    a, b = h
    if a + b >= 47: return 'W'                                                  # Проверка победы
    if any(game(m) == 'W' for m in moves(h)): return 'P1'                       # Если хотябы один ход выигрышный - выигрывает Петя
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'                      # Если все ходы проигрышные - выигрывает Ваня
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'                      # Если хотябы один их ходов ведет в ход, где все ходы проигрышные - выигрывает Петя
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'   # Если все пути ведут в выигрышный ход первой или второй глубины - выигрывает Ваня

for s in range(1, 37):
    h = (10, s)
    if game(h) == 'B2':
        print(s, game(h))