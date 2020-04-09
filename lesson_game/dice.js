// utility functions to do dice rolls, by Petri Kuittinen 2020

// return random integer 1...sides of dice
function dice(sides=6) {
    return Math.floor(sides*Math.random()+1);
}
// return the sum of sides sided dice rolls
function die(n, sides) {
    let total = 0;
    while (n-- > 0) {
	total += dice(sides);
    }
    return total;
}
// short cuts for most popular die e.g. d6() one 6-sided dice
// d6(20) rolls 20 times 6-sided die and returns sum of the dice rolls
let d4 = (n=1) => die(n, 4);
let d6 = (n=1) => die(n, 6);
let d8 = (n=1) => die(n, 8);
let d10 = (n=1) => die(n, 10);
let d12 = (n=1) => die(n, 12);
let d20 = (n=1) => die(n, 20);
let d100 = (n=1) => die(n, 100);
