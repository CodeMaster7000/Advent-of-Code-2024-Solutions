from re import findall
from re import compile
data = open("input.in").read()
mul_pattern = compile(r"mul\((\d+),(\d+)\)")
print("Part 1 solution:", sum(int(g[0])*int(g[1]) for g in findall(mul_pattern, data)))
data = " ".join(part.split("don't()")[0] for part in data.split("do()"))
print("Part 2 solution:", sum(int(g[0])*int(g[1]) for g in findall(mul_pattern, data)))
