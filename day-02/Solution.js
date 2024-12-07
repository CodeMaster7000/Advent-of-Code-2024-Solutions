const fs = require('fs');
function Part1() {
	fs.readFile('./input.in', (err, data) => {
		const reports = data
			.toString()
			.replace(/\r/g, '')
			.trimEnd()
			.split('\n')
			.map(levels => levels.split(/\s+/));
		let safeReports = 0;
		outer: for (let i = 0; i < reports.length; i++) {
			const increaseLevels = reports[i].toSorted((a, b) => a - b);
			const decreaseLevels = reports[i].toSorted((a, b) => b - a);
			if (
				increaseLevels.every((a, index) => a === reports[i][index]) ||
				decreaseLevels.every((a, index) => a === reports[i][index])
			) {
				for (let j = 0; j < reports[i].length; j++) {
					if (j < reports[i].length - 1) {
						const difference = Math.abs(reports[i][j] - reports[i][j + 1]);
						const check = difference >= 1 && difference <= 3;
						if (!check) {
							continue outer;
						}
					}
				}
				safeReports++;
			}
		}

		console.log(safeReports);
	});
}

Part1();

function Part2() {
	fs.readFile('./input.txt', (err, data) => {
		const reports = data
			.toString()
			.replace(/\r/g, '')
			.trimEnd()
			.split('\n')
			.map(levels => levels.split(/\s+/));
		let safeReports = 0;
		for (let i = 0; i < reports.length; i++) {
			const possible = [reports[i]];
			for (let j = 0; j < reports[i].length; j++) {
				const copy = reports[i].slice();
				copy.splice(j, 1);
				possible.push(copy);
			}
			const isPossible = possible.some(x => {
				const sign = Math.sign(x[0] - x[1]);
				for (y = 1; y < x.length; y++) {
					if (Math.abs(x[y - 1] - x[y]) < 1) return false;
					if (Math.abs(x[y - 1] - x[y]) > 3) return false;
					if (Math.sign(x[y - 1] - x[y]) != sign) return false;
				}
				return true;
			});
			if (isPossible) {
				safeReports++;
			}
		}
		console.log(safeReports);
	});
}

Part2();
