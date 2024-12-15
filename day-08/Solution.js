const input = require("fs").readFileSync("input.in", "utf-8");
const inputMap = input
    .trim()
    .split("\n")
    .map((line) => line.trim().split(""));
const width = inputMap[0].length;
const height = inputMap.length;
const antennas = {};
inputMap.forEach((row, y) => {
    row.forEach((cell, x) => {
        if (cell !== ".") {
            if (antennas[cell]) {
                antennas[cell].push({ x: x, y: y });
            } else {
                antennas[cell] = [{ x: x, y: y }];
            }
        }
    });
});
function isOutsideMap(point) {
    if (point.x < 0 || point.x >= width || point.y < 0 || point.y >= height) {
        return true;
    }
    return false;
}
function generateAntiNode(a1, a2) {
    const vector = { x: a2.x - a1.x, y: a2.y - a1.y };
    const antinodes = [];
    antinodes.push(a1);
    antinodes.push(a2);
    const firstForwardAntinode = { x: a1.x + vector.x, y: a1.y + vector.y };
    if (!isOutsideMap(firstForwardAntinode)) {
        antinodes.push(firstForwardAntinode);
    }
    let i = 1;
    while (true) {
        const newAntinode = { x: a1.x + vector.x * i, y: a1.y + vector.y * i };
        if (isOutsideMap(newAntinode)) {
            break;
        }
        antinodes.push(newAntinode);
        i++;
    }
    i = 1;
    const firstBackwardsAntinode = { x: a1.x - vector.x, y: a1.y - vector.y };
    if (isOutsideMap(firstBackwardsAntinode)) {
        return antinodes;
    }
    antinodes.push(firstBackwardsAntinode);
    while (true) {
        const newAntinode = { x: a1.x - vector.x * i, y: a1.y - vector.y * i };
        if (isOutsideMap(newAntinode)) {
            break;
        }
        antinodes.push(newAntinode);
        i++;
    }
    return antinodes
}
const mapAntinodes = {};
for (const key in antennas) {
    const positions = antennas[key];
    for (let i = 0; i < positions.length; i++) {
        for (let j = i + 1; j < positions.length; j++) {
            const a1 = positions[i];
            const a2 = positions[j];
            const antinodes = generateAntiNode(a1, a2);
            antinodes.forEach(antinode => {
                const key = JSON.stringify(antinode);
                mapAntinodes[key] = antinode
            })
        }
    }
}
function printMap() {
    const newMatrix = [...inputMap];
    for (const key in mapAntinodes) {
        const antinode = JSON.parse(key);
        newMatrix[antinode.y][antinode.x] = newMatrix[antinode.y][antinode.x] === "." ? "#" : newMatrix[antinode.y][antinode.x].toLowerCase();
    }
    for (let i = 0; i < height; i++) {
        let line = "";
        for (let j = 0; j < width; j++) {
            line += newMatrix[i][j];
        }
        console.log(line);
    }
}
console.log("Number of unique antinodes: ", Object.keys(mapAntinodes).length);
