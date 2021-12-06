import os

fpath = os.path.join(os.path.dirname(__file__), 'input.txt')


def count_increasing(nums):
    total = 0
    current_num = nums.pop(0)
    while len(nums):
        new_num = nums.pop(0)
        if new_num > current_num:
            total += 1
        current_num = new_num
    return total


def main():
    with open(fpath) as f:
        lines = f.readlines()
    nums = [int(l) for l in lines]

    print(count_increasing(nums))


if __name__ == '__main__':
    main()
