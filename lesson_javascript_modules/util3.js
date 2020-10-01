// Module export for Modern Browsers
const INCH_IN_CM = 2.54;
export function inchesToCm(inch) {
    return inch * INCH_IN_CM;
}
export function cmToInches(cm) {
    return cm / INCH_IN_CM;
}

import { inchesToCm, cmToInches } from './util3.js';
console.log(inchesToCm(12));
import * as Util from './util3.js';
console.log(Util.inchesToCm(12)); 
console.log(Util.cmToInches(10));
import { inchesToCm as inchConversion } from './util3.js';
console.log(inchConversion(12));
