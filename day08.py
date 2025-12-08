import operator
from functools import reduce

from utils import run_puzzle

EXAMPLE_DATA = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


def parse(data):
    return [tuple(map(int, line.split(','))) for line in data.splitlines() if line.strip()]


def build_edges(points):
    edges = []
    n = len(points)

    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz
            edges.append((dist2, i, j))
    return sorted(edges, key=lambda e: e[0])


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra  # ensure ra is the larger rank

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True


def part_a(points):
    n = len(points)
    edges = build_edges(points)
    uf = UnionFind(n)

    limit = 10 if n < 50 else 1000  # between example and real

    for dist2, u, v in edges[:limit]:
        uf.union(u, v)

    comp_sizes = {}
    for i in range(n):
        root = uf.find(i)
        comp_sizes[root] = uf.size[root]

    top3 = sorted(comp_sizes.values(), reverse=True)[:3]
    return reduce(operator.mul, top3)


def part_b(points):
    n = len(points)
    edges = build_edges(points)
    uf = UnionFind(n)

    for dist2, u, v in edges:
        uf.union(u, v)
        if max(uf.size) == n:  # fully connected
            return points[u][0] * points[v][0]

    return None


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=8,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=40,    # 131150
        expected_ans_b=25272  # 2497445
    )
