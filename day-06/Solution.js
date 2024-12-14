import {degrees_to_radians, inputToPlayingField, readInput} from "../util.js";
let input = readInput("./input.in");
let playingField
function loadPlayingfield() {
    playingField =  inputToPlayingField(input)
}
loadPlayingfield()
console.log(playingField)
function findGuard(field){
    for(let x = 0; x < field.length; ++x){
        for(let y = 0;y < field[0].length; ++y){
            if(playingField[x][y] == "^"){
                return {
                    x:x,
                    y:y
                }
            }
        }
    }
}
console.log(findGuard(playingField))
let currentFacing = 0;
function getDirection(faccing){
    return {
        x: -Math.round(Math.sin(degrees_to_radians(-faccing))),
        y: -Math.round(Math.cos(degrees_to_radians(-faccing)))
    }
}
function isInBounds(pos){
    return pos.x < 0 || pos.y < 0 || pos.x >= playingField.length || pos.y >= playingField[0].length;
}
function isObsticale(pos){
    return  playingField[pos.x][pos.y] == "#"
}
function printPlayingField(){
    for(let y in playingField[0]){
        let line =""
        for (let x in playingField){
            line+=playingField[x][y]
        }
        console.log(line)
    }
}
export function checkLoop() {
    let visitedSquares = new Map()
    let visitedSquaresAndRotations = new Map()

    let guard = findGuard(playingField)
    if(!guard){
        return false
    }
    guard.rotation = 0;
    while (true) {
        if (visitedSquaresAndRotations.has(JSON.stringify({
            x: guard.x,
            y: guard.y,
            rotation: guard.rotation
        }))) {
            return true;
            break
        }
        visitedSquares.set(JSON.stringify({
            x: guard.x,
            y: guard.y
        }), true)

        visitedSquaresAndRotations.set(JSON.stringify({
            x: guard.x,
            y: guard.y,
            rotation: guard.rotation
        }), true)
        let step = getDirection(guard.rotation)
        let newPos = {
            x: guard.x + step.x,
            y: guard.y + step.y
        }
        if (isInBounds(newPos)) {
            return false;
            break
        }
        if (isObsticale(newPos)) {
            guard.rotation += 90;
            guard.rotation %= 360;
        } else {
            guard.x = newPos.x
            guard.y = newPos.y
        }
    }
    console.log(visitedSquares.size)
}
let counter = 0;
for(let x in playingField){
    console.log("Test" + counter)
    for(let y in playingField[0]){
        let old = playingField[x][y]
            playingField[x][y] = "#"
            if(checkLoop()){
                counter++;
            }
            playingField[x][y] = old

        }
}
checkLoop()
console.log(counter)
console.log("Test")
