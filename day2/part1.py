import os

fpath = os.path.join(os.path.dirname(__file__), 'input.txt')


def preprocess_inst(inst):
    direction, distance = inst.split(' ')
    return direction, int(distance)


def get_instructions():
    with open(fpath) as f:
        instructions = f.readlines()
    return [preprocess_inst(x) for x in instructions]


class Submarine:
    def __init__(self):
        # horizontal, depth
        self.pos = [0, 0]

    def process_instructions(self, instructions):
        for inst in instructions:
            self.move(*inst)

    def move(self, direction, distance):
        if direction == 'forward':
            self.pos[0] += distance
        elif direction == 'down':
            self.pos[1] += distance
        elif direction == 'up':
            self.pos[1] -= distance


def main():
    instructions = get_instructions()

    sub = Submarine()
    sub.process_instructions(instructions)
    print(sub.pos[0] * sub.pos[1])


if __name__ == '__main__':
    main()
