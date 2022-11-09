from collections import defaultdict
from itertools import cycle

connectivity = {
    0: [1, 2, 4, 9],
    1: [3, 5, 9],
    2: [3],
    3: [6],
    4: [5, 8, 10],
    5: [6],
    6: [7, 8],
    7: [9],
    8: [9]
}


def build_connectivity_map():
    m = defaultdict(set)
    for a, elems in connectivity.items():
        for b in elems:
            m[a].add(b)
            m[b].add(a)
    return m


neighbours = build_connectivity_map()


def print_state(state):
    print([(hole, color) for hole, color in enumerate(state) if color])
    

def next_color(color):
    if color == "W":
        return "B"
    else:
        return "W"


def can_play(state, color, hole):
    if state[hole] is not None:
        return False
    for neighbour in neighbours[hole]:
        if state[neighbour] == color:
            return False
    return True


def find_possible_holes(state, color):
    return [hole for hole in range(11) if can_play(state, color, hole)]


def generate_plays(state, color):
    ph = find_possible_holes(state, color)
    if not ph:
        print(f"{color} loses")
        print_state(state)
        return
    new_color = next_color(color)
    for hole in possible_hole:
        generate_plays(new_state, new_color)


def main():
    state = ['W', None, None, None, None, 'B', None, None, 'W', 'B', None]
    generate_plays(state, 'W')


if __name__ == '__main__':
    main()