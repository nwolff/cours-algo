from collections import defaultdict
from itertools import cycle

connectivity = [
    (0, 1),
    (0, 2),
    (0, 4),
    (0, 9),
    (1, 3),
    (1, 5),
    (2, 3),
    (3, 6),
    (4, 5),
    (4, 8),
    (4, 10),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 9),
    (8, 9)
]


def build_connectivity_map():
    m = defaultdict(set)
    for a, b in connectivity:
        m[a].add(b)
        m[b].add(a)
    return m


neighbours = build_connectivity_map()


def can_play(state, color, hole):
    if state[hole] is not None:
        return False
    for neighbour in neighbours[hole]:
        if state[neighbour] == color:
            return False
    return True


def possible_plays(state, color):
    result = []
    for hole in range(11):
        if can_play(state, color, hole):
            new_state = state.copy()
            new_state[hole] = color
            result.append(new_state)
    return result


def print_state(state):
    print([(hole, color) for hole, color in enumerate(state) if color])


def main():
    state = ['W', None, None, None, None, 'B', None, None, 'W', 'B', None]
    print_state(state)
    for color in cycle(['W', 'B']):
        plays = possible_plays(state, color)
        for play in plays:
            print_state(play)
        return


if __name__ == '__main__':
    main()