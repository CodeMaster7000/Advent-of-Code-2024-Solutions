from collections import defaultdict

p1, p2 = open('input.in').read().split('\n\n')
updates = [list(map(int, line.split(','))) for line in p2.splitlines()]
orders = defaultdict(list)
for order in p1.splitlines():
    before, after = order.split('|')
    orders[int(before)].append(int(after))
Part1 = 0
Part2 = 0
for pages in updates:
    sorted_pages = sorted(pages, key=lambda page: -len([order for order in orders[page] if order in pages]))
    if pages == sorted_pages:
        Part1 += pages[len(pages) // 2]
    else:
        Part2 += sorted_pages[len(sorted_pages) // 2]
print('Part 1 solution:', Part1)
print('Part 2 solution:', Part2)
