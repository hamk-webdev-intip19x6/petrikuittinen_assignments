let cart = [];

function findProduct(id) {
    for(let product of products) {
	if (product.id == id) {
	    return product;
	}
    }
}

function updateCart() {
    let text = "<table border='1'><tr><th>Product<th>Price<th>Amount"
    for(let p of cart) {
	let product = findProduct(p.id);
	console.log(product);
	text += "<tr><td>"+product.name+"<td>"+product.price/100;
	text += "<td>"+p.amount;
    }	
    text += "</table>";
    document.getElementById("cart").innerHTML = text;
}

function buy(id) {
    console.log("Buying: "+id);
    let found = false;
    for(let p of cart) {
	if (p.id == id) {
	    p.amount++; // if found, increase amount by one
	    found = true;
	}
    }
    if(!found) { // if not found, add to cart
	cart.push({id: id, amount: 1});
    }
    console.log(cart);
    updateCart();
}

function buildInventoryList() {
    let text = "<table border='1'><tr><th>Product<th>Price<th>Order";
    for(let product of products) {
	text += "<tr><td>"+product.name+
	    "<td>"+(product.price/100)+" euros"+
	    "<td><input type='button' value='Buy' onclick='buy(\""+
	    product.id+"\")'>";
}
    text += "</table>"
    document.getElementById("inventory").innerHTML = text;
}

buildInventoryList();
