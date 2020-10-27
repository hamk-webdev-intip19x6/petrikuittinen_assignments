// utility functions to do dice rolls, by Petri Kuittinen 2020

// just a wrapper, so Math.random can be replaced easily
if (typeof MersenneTwister !== "undefined") {
    __mersenne = new MersenneTwister();
    function random() {
        return __mersenne.random();
    }
} else {
    function random() {
        return Math.random();
    }
}

// return random integer from a to b (not included)
function randRange(a, b) {
    return Math.floor((b - a) * random() + a);
}

// return random integer from a to b (b included)
function randInt(a, b) {
    return randRange(1, b + 1);
}

// return random integer 1...sides of dice
function dice(sides = 6) {
    return Math.floor(sides * random() + 1);
}
// return the sum of sides sided dice rolls
function die(n, sides) {
    let total = 0;
    while (n-- > 0) {
        total += dice(sides);
    }
    return total;
}

// shuffle a using Fisher-Yates shuffle (or Knuth's shuffle)
function shuffle(a) {
    for (let i = 0; i < a.length - 1; i++) {
        let j = randRange(i, a.length);
        // swap the array elements
        [a[i], a[j]] = [a[j], a[i]];
    }
}

// short cuts for most popular die e.g. d6() one 6-sided dice
// d6(20) rolls 20 times 6-sided die and returns sum of the dice rolls
let d4 = (n = 1) => die(n, 4);
let d6 = (n = 1) => die(n, 6);
let d8 = (n = 1) => die(n, 8);
let d10 = (n = 1) => die(n, 10);
let d12 = (n = 1) => die(n, 12);
let d20 = (n = 1) => die(n, 20);
let d100 = (n = 1) => die(n, 100);
