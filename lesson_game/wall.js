// examples of how to OOP wall tiles
let wall1 = {
    name: "hard wood",
    hp: 30,
    solid: true,
    bitmap: "hardwood.png"
}
let wall2 = {
    name: "stone",
    hp: 100,
    solid: true,
    bitmap: "stone.png"
}
let wall3 = {
    name: "illusionary wall",
    hp: 0,
    solid: false,
    bitmap: "stone.png"
}
// Let's assume one wall tile be 32x32 pixels
// object will need 0.5 kilobytes RAM memory
// one 1920x1080 screen will fit 60x33.75 (34) tiles
// one screen will require 1020 kilobytes = 1 Megabyte
// massive level with 10x10 screens will require
// 100 Megabytes

// on very memory-limited devices, you might consider following:
tile = 0x00000000; // 32-bit int
// bits 0-7     tile bitmap number 0-255
// bits 8-15    tile capabilities e.g. bit 8 = solid (1)
// bits 16-31   hit points (0-65535)
// then one screen will need only 8160 bytes = 8 kilobytes
// 10x10 screen massive level needs ~800 kb
