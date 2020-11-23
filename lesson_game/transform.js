// translate a coordinate relative new origin
function translate(coord, xOrigin=0, yOrigin=0) {
    let x = coord.x + xOrigin;
    let y = coord.y + yOrigin;
    return {x, y};
}

// rotate coordinate around orin by angle radians
function rotate(coord, angle=0) {
    let cosA = Math.cos(angle);
    let sinA = Math.sin(angle);
    let x = coord.x*cosA - coord.y*sinA;
    let y = coord.y*cosA + coord.x*sinA;
    return {x, y};
}

// scale a coordinate
function scale(coord, xScale=1.0, yScale=1.0) {
    let x = coord.x*xScale;
    let y = coord.y*yScale;
    return {x, y};
}

// apply 3x3 2D transformation matrix to coordinate
// Since the bottom row of transformation matrix is always 0 0 1
// we only need 6 numbers: a, b, c for top row and
// d, e, f for 2nd row
function transform(coord, a=0, b=0, c=0, d=0, e=0, f=0) {
    let x = coord.x*a+coord.y*b+c;
    let y = coord.x*d+coord.y*e+f;
    return {x, y}
}

// do it all
function translateScaleRotate(coord, xOrigin, yOrigin, xScale, yScale, angle) {
    let a = Math.cos(angle)*xScale;
    let b = -Math.sin(angle)*xScale;
    let c = xOrigin;
    let d = Math.sin(angle)*yScale;
    let e = Math.cos(angle)*yScale;
    let f = yOrigin;
    return transform(coord, a, b, c, d, e, f);
}
