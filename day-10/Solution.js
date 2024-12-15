function pt() {
    const input = require('fs').readFileSync('./input.in', 'utf-8');
    const matrix = input.split('\n').map(row => row.split('').map(Number));
    const withinMatrix = (pos) => pos[0] >= 0 && pos[0] < matrix.length && pos[1] >= 0 && pos[1] < matrix[pos[0]].length;
    const charAt = (pos) => pos && withinMatrix(pos) ? matrix[pos[0]][pos[1]] : -1;
    const walk = (step, previous, endPoints) => {
        if (!withinMatrix(step)) return 0;
        const stepNum = charAt(step);
        const prevNum = charAt(previous);
        if (stepNum - prevNum !== 1) return 0;
        if (stepNum === 9) {
            endPoints.add(step.join(','));
            return 1;
        }
        const [x, y] = step;
        return  walk([x + 1, y], step, endPoints) +
                walk([x, y + 1], step, endPoints) +
                walk([x - 1, y], step, endPoints) +
                walk([x, y - 1], step, endPoints);
    }
    const findEndPoints = (start) => {
        const endPoints = new Set();
        const trails = walk(start, undefined, endPoints);
        return {endpoints: endPoints.size, trails: trails};
    }
    let endpoints = 0;
    let trails = 0;
    matrix.forEach((row, i) => row.forEach((num, j) => {
        if (num === 0) {
            const trailLog = findEndPoints([i, j]);
            endpoints += trailLog.endpoints;
            trails += trailLog.trails;
        }
    }));
    console.log('Part 1 solution:', endpoints);
    console.log('Part 2 solution:', trails);
}
pt();
