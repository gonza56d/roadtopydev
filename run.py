#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def binary_search(elements, begin, end, score):
    if len(elements) == 1:
        if elements[0] > score:
            return end
        else:
            return begin
    first_half = elements[:len(elements) // 2]
    if first_half and first_half[-1] <= score:
        end = len(elements) // 2
        return binary_search(first_half, begin, end, score)
    second_half = elements[len(elements) // 2:]
    if second_half and second_half[0] >= score:
        begin += len(elements) // 2
        return binary_search(second_half, begin, end, score)
    if first_half[-1] > score > second_half[0]:
        end -= len(second_half)
    return end


def climbing_leaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    ret = []
    for score in player:
        begin = 0
        end = len(ranked)
        ranking = binary_search(ranked[::-1], begin, end, score) + 1
        ret.append(ranking)
    return ret


if __name__ == '__main__':
    result = climbing_leaderboard(
        [100, 90, 90, 80, 75, 60],
        [50, 65, 77, 90, 102]
    )
    print(result)
