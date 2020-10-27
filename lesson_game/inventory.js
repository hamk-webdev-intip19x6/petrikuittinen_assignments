let inventory = []; // contains {id: item_id, amount: amount_of_those }

function finditem(id) {
    for (let item of items) {
        if (item.id == id) {
            return item;
        }
    }
}

function updateInventory() {
    let price = 0; // total price counter
    let weight = 0; // total weight counter
    let text = "<table border='1'><tr><th>Item<th>Weight<th>Price<th>Amount<th>Remove"
    for (let p of inventory) {
        let item = finditem(p.id);
        text += `<tr><td>${item.name}<td>${item.weight}`;
        text += `<td>${item.price / 100}`;
        text += `<td>${p.amount}`;
        text += `<td><input type='button' value='Remove' `
        text += `onclick='remove("${p.id}")'>`
        price += item.price * p.amount;
        weight += item.weight * p.amount;
    }
    text += "</table>";
    document.getElementById("id_inventory").innerHTML = text;
    document.getElementById("id_price").innerHTML = price / 100;
    document.getElementById("id_weight").innerHTML = weight;
}

function get(id) {
    let found = false;
    for (let p of inventory) {
        if (p.id == id) {
            p.amount++; // if found, increase amount by one
            found = true;
        }
    }
    if (!found) { // if not found, add to cart
        inventory.push({ id: id, amount: 1 });
    }
    updateInventory();
}

function remove(id) {
    for (let p of inventory) {
        if (p.id == id) {
            inventory = inventory.filter(x => x !== p); // remove it
            updateInventory();
            break;
        }
    }
}

function buildItemList() {
    let text = "<table border='1'><tr><th>Item<th>Weight<th>Price<th>Order";
    for (let item of items) {
        text += `<tr><td>${item.name}` +
            `<td>${item.weight} g`+
            `<td>${item.price / 100} gold ` +
            `<td><input type='button' value='Get'` +
            `onclick='get("${item.id}")'>`;
    }
    text += "</table>"
    document.getElementById("id_items").innerHTML = text;
}

