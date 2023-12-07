import sys
import os
from simple_colors import *
from pathlib import Path
parent_dir = os.path.dirname(Path(os.path.abspath(__file__)).parent)
sys.path.append(parent_dir)
import utils
from collections import defaultdict, Counter

def get_type(card):
    
    # For the submission
    # counts = {}
    # for c in card[0]:
    #     counts[c] = counts.get(c, 0) + 1
    
    # After submission
    counts = Counter(card[0])

    if sorted(counts.values()) == [5]:
        # five of a kind
        card.append(9)
    elif sorted(counts.values()) == [1, 4]:
        # four of a kind
        card.append(8)
    elif sorted(counts.values()) == [2, 3]:
        # full house
        card.append(7)
    elif sorted(counts.values()) == [1, 1, 3]:
        # three of a kind
        card.append(6)
    elif sorted(counts.values()) == [1, 2, 2]:
        # two pairs
        card.append(5)
    elif sorted(counts.values()) == [1, 1, 1, 2]:
        # one pair
        card.append(4)
    elif sorted(counts.values()) == [1, 1, 1, 1, 1]:
        # high card
        card.append(3)
    else:
        print("ERROR")
        print(counts)
        sys.exit(1)

    c = 57
    card[0] = card[0].replace("T", chr(c + 1)).replace("J", chr(c + 2)).replace("Q", chr(c + 3)).replace("K", chr(c + 4)).replace("A", chr(c + 5))


@utils.time_decorator
def do(data):
    
    cards = []
    for d in data:
        d = d.split()
        cards.append([d[0],int(d[1])])
    
    for c in cards:
        get_type(c)

    sorted_cards = sorted(cards, key=lambda x: (x[2], x[0]))
    # print(sorted_cards)

    res = 0
    for i, (card, value, _) in enumerate(sorted_cards):
        res += value * (i + 1)
    return res

with open("2023/07/input.txt") as f:
    print(red("Part 1:"))
    data = f.read().splitlines()
#     data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".split("\n")
    res = do(data)  
    print("Result should be (🤞):", res)