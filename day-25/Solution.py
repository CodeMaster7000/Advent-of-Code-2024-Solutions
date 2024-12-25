items = [{i for i, c in enumerate(item) if c == '#'}
    for item in open('input.in').read().split('\n\n')]
print("Solution: ",sum(not k&l for k in items for l in items)//2)
