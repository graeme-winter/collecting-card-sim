import argparse
import random
import sys

import numpy as np


def simulate(N, M, P, R):
    """Simulate collection process of N unique items, with M gathered in
    in advance, with P unique per pack, leaving R, return number of packs"""
    collect = set(range(N - M))
    all = list(range(N))

    n = 0
    while len(collect) > R:
        pack = random.sample(all, P)
        collect -= set(pack)
        n += 1
    return n


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Collecting card simulator")
    parser.add_argument("--count", type=int, default=144)
    parser.add_argument("--collected", type=int, default=0)
    parser.add_argument("--iter", type=int, default=1000)
    parser.add_argument("--pack", type=int, default=4)
    parser.add_argument("--remain", type=int, default=0)

    args = parser.parse_args()

    population = np.array(
        [
            simulate(args.count, args.collected, args.pack, args.remain)
            for j in range(args.iter)
        ]
    )
    q = tuple(map(int, np.percentile(population, [25, 50, 75])))
    print(args.count, args.collected, population.min(), *q, population.max())
