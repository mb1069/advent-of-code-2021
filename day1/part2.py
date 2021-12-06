from day1.part1 import count_increasing, fpath
import re
from collections import OrderedDict


def lines_to_window_depths(lines):
    nums = [int(l) for l in lines]
    nums = [sum(nums[i:i+3]) for i in range(len(nums)-2)]
    return nums


def main():
    with open(fpath) as f:
        lines = f.readlines()

    nums = lines_to_window_depths(lines)
    print(count_increasing(nums))


if __name__ == '__main__':
    main()
