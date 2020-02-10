var product1 = {name: "hammer", price: 1499};
var product2 = {name: "6 inch nail", price: 10};
var hoover = {name: "Hoover", price: 1800};
var inventory = [
    {id: "hammer", info: product1, amount: 3},
    {id: "nail", info: product2, amount: 100},
    {id: "hoover", info: hoover, amount: 1}
];
var money = 10000;
var cart = [];
var first = inventory[0];
money = money-first.info.price;
cart.push(first.info);
first.amount--;


monster = {name: "ghost", hp: 3};
monster.heal = function(amount) {hp
