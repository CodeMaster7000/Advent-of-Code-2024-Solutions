import pyperclip as pc
import sys
import re
from collections import defaultdict, Counter, deque
def pt(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'input.in'
Part1 = 0
Part2 = 0
D = open(infile).read().strip()
def is_valid(target, ns, Part2):
    if len(ns) == 1:
        return ns[0]==target
    if is_valid(target, [ns[0]+ns[1]] + ns[2:], Part2):
        return True
    if is_valid(target, [ns[0]*ns[1]] + ns[2:], Part2):
        return True
    if Part2 and is_valid(target, [int(str(ns[0])+str(ns[1]))] + ns[2:], Part2):
        return True
    return False
for line in D.strip().split('\n'):
    target, ns = line.strip().split(':')
    target = int(target)
    ns = [int(x) for x in ns.strip().split()]
    if is_valid(target, ns, Part2=False):
        Part1 += target
    if is_valid(target, ns, Part2=True):
        Part2 += target
pt("Part 1 solution:",Part1)
pt("Part 2 solution:",Part2)
