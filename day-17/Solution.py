import pathlib
def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.in", 'r').read().split('\n')[:-1]

def simulate(program, A):
  l = [0, 1, 2, 3, A, 0, 0, -1]
  out = []
  i = 0
  while i < len(program):
    op = program[i]
    operand = program[i + 1]
    if op == 0:
      l[4] = int(l[4] / (2 ** l[operand]))
    elif op == 1:
      l[5] = l[5] ^ operand
    elif op == 2:
      l[5] = l[operand] % 8
    elif op == 3:
      if l[4] != 0:
        i = operand
        continue
    elif op == 4:
      l[5] = l[5] ^ l[6]
    elif op == 5:
      out.append(l[operand] % 8)
    elif op == 6:
      l[5] = int(l[4] / (2 ** l[operand]))
    elif op == 7:
      l[6] = int(l[4] / (2 ** l[operand]))
    i += 2
  return out

def Part1():
  f = reader()
  program = list(map(int, f[4][(f[4].find(': ') + 2):].split(',')))
  print("Part 1 solution: ",','.join(map(str, simulate(program, int(f[0][(f[0].find(': ') + 2):])))))

def Part2():
  f = reader()
  program = list(map(int, f[4][(f[4].find(': ') + 2):].split(',')))
  def backtrack(A=0, j=-1):
    if -j > len(program):
      return A
    m = float('inf')
    for i in range(8):
      t = (A << 3) | i
      if simulate(program, t)[j:] == program[j:]:
        m = min(m, backtrack(t, j - 1))
    return m

  print("Part 2 solution: ",backtrack())
  
Part1()
Part2()
