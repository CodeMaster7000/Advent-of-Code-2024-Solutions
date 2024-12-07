const fs = require('fs');

function Part1() {
	fs.readFile('./input.in', (err, data) => {
		const words = data
			.toString()
			.replace(/\r/g, '')
			.trimEnd()
			.split('\n')
			.map(row => row.split(''));
		const regex = /(?=(XMAS|SAMX))/g;
		let wordCount = 0;
		function rotate90(matrix) {
			return matrix[0].map((val, index) =>
				matrix.map(row => row[index]).reverse()
			);
		}
		function rotate45(data, fromBottom) {
			const length = { x: data[0].length, y: data.length };
			length.max = Math.max(length.x, length.y);

			const rotated = [];

			for (let k = 0; k <= 2 * (length.max - 1); k++) {
				const tempRow = [];
				for (let y = length.y - 1; y >= 0; y--) {
					let x = k - (fromBottom ? length.y - y : y);
					x >= 0 && x < length.x && tempRow.push(data[y][x]);
				}
				tempRow.length > 0 && rotated.push(tempRow);
			}
			return rotated;
		}
		words.forEach(
			wordRow => (wordCount += [...wordRow.join('').matchAll(regex)].length)
		);
		rotate90(words).forEach(
			wordRow => (wordCount += [...wordRow.join('').matchAll(regex)].length)
		);
		rotate45(words).forEach(
			wordRow => (wordCount += [...wordRow.join('').matchAll(regex)].length)
		);
		rotate45(words, true).forEach(
			wordRow => (wordCount += [...wordRow.join('').matchAll(regex)].length)
		);
		console.log(wordCount);
	});
}
Part1();

function Part2() {
	fs.readFile('./input.in', (err, data) => {
		const puzzle = data
			.toString()
			.replace(/\r/g, '')
			.trimEnd()
			.split('\n')
			.map(row => row.split(''));
		let = xmasCount = 0;
		for (let y = 1; y < puzzle.length - 1; y++) {
			for (let x = 1; x < puzzle[0].length - 1; x++) {
				if (puzzle[y][x] === 'A') {
					if (
						((puzzle[y - 1][x - 1] === 'M' && puzzle[y + 1][x + 1] === 'S') ||
							(puzzle[y - 1][x - 1] === 'S' && puzzle[y + 1][x + 1] === 'M')) &&
						((puzzle[y + 1][x - 1] === 'M' && puzzle[y - 1][x + 1] === 'S') ||
							(puzzle[y + 1][x - 1] === 'S' && puzzle[y - 1][x + 1] === 'M'))
					) {
						xmasCount++;
					}
				}
			}
		}
		console.log(xmasCount);
	});
}
Part2();
