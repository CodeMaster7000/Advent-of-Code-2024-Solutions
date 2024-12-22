import heapq
import pyperclip as pc
import re
import sys
from collections import defaultdict, Counter, deque
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
infile = sys.argv[1] if len(sys.argv)>=2 else 'input.in'
Part1 = 0
Part2 = 0
D = open(infile).read().strip()
G = D.split('\n')
R = len(G)
C = len(G[0])
SEEN = set()
for r in range(R):
    for c in range(C):
        if (r,c) in SEEN:
            continue
        Q = deque([(r,c)])
        area = 0
        perim = 0
        PERIM = dict()
        while Q:
            r2,c2 = Q.popleft()
            if (r2,c2) in SEEN:
                continue
            SEEN.add((r2,c2))
            area += 1
            for dr,dc in DIRS:
                rr = r2+dr
                cc = c2+dc
                if 0<=rr<R and 0<=cc<C and G[rr][cc]==G[r2][c2]:
                    Q.append((rr,cc))
                else:
                    perim += 1
                    if (dr,dc) not in PERIM:
                        PERIM[(dr,dc)] = set()
                    PERIM[(dr,dc)].add((r2,c2))
        sides = 0
        for k,vs in PERIM.items():
            SEEN_PERIM = set()
            old_sides = sides
            for (pr,pc) in vs:
                if (pr,pc) not in SEEN_PERIM:
                    sides += 1
                    Q = deque([(pr,pc)])
                    while Q:
                        r2,c2 = Q.popleft()
                        if (r2,c2) in SEEN_PERIM:
                            continue
                        SEEN_PERIM.add((r2,c2))
                        for dr,dc in DIRS:
                            rr,cc = r2+dr,c2+dc
                            if (rr,cc) in vs:
                                Q.append((rr,cc))
        Part1 += area*perim
        Part2 += area*sides
print("Part 1 solution:", Part1)
print("Part 2 solution:", Part2)
