import re
Coordinates = tuple[int, int]
def Part1(raw_input: str) -> int:
    inputs = parse_input(raw_input)
    return sum([price_inputs(calculate_required_inputs(*input)) for input in inputs])
def Part2(raw_input: str) -> int:
    inputs = parse_input(raw_input)
    return sum([price_inputs(calculate_required_inputs(*modify_input_for_Part2(input))) for input in inputs])
def parse_input(raw_input: str) -> list[tuple[Coordinates, Coordinates, Coordinates]]:
    matcher = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
    sections = raw_input.strip().split("\n\n")
    results = []
    for section in sections:
        matches = matcher.match(section)
        results.append(((int(matches.group(1)), int(matches.group(2))),
                        (int(matches.group(3)), int(matches.group(4))),
                        (int(matches.group(5)), int(matches.group(6)))))
    return results
def modify_input_for_Part2(config: tuple[Coordinates, Coordinates, Coordinates]) -> tuple[Coordinates, Coordinates, Coordinates]:
    return config[0], config[1], (config[2][0] + 10000000000000, config[2][1] + 10000000000000)
def calculate_required_inputs(button_a: Coordinates, button_b: Coordinates, prize: Coordinates) -> tuple[int, int] | None:
    x_equation = (button_a[0], button_b[0], prize[0])
    y_equation = (button_a[1], button_b[1], prize[1])
    scaled_x_equation = (x_equation[0] * y_equation[0],
                         x_equation[1] * y_equation[0],
                         x_equation[2] * y_equation[0])
    scaled_y_equation = (y_equation[0] * x_equation[0],
                         y_equation[1] * x_equation[0],
                         y_equation[2] * x_equation[0])
    difference = (scaled_x_equation[1] - scaled_y_equation[1],
                  scaled_x_equation[2] - scaled_y_equation[2])
    b, r = divmod(difference[1], difference[0])
    if r != 0:
        return None
    if x_equation[1] == 0:
        a, r = divmod((y_equation[2] - y_equation[1] * b), y_equation[0])
    else:
        a,r  = divmod((x_equation[2] - x_equation[1] * b), x_equation[0])
    if r == 0 and a >= 0 and b >= 0:
        return a, b
    return None
def price_inputs(button_presses: tuple[int, int]) -> int:
    if button_presses is None:
        return 0
    return 3 *  button_presses[0] + button_presses[1]
def main():
    with open("./day-13/input.in") as f:
        raw_input = f.read()
    print(f"Part 1 solution: {Part1(raw_input)}")
    print(f"Part 2 solution: {Part2(raw_input)}")
if __name__ == "__main__":
    main()
