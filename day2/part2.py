from day2.part1 import Submarine, get_instructions


class AimSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move(self, direction, distance):
        if direction == 'up':
            self.aim -= distance
        elif direction == 'down':
            self.aim += distance
        elif direction == 'forward':
            self.pos[0] += distance
            self.pos[1] += (distance * self.aim)


def main():
    instructions = get_instructions()

    sub = AimSubmarine()
    sub.process_instructions(instructions)
    print(sub.pos[0] * sub.pos[1])


if __name__ == '__main__':
    main()
