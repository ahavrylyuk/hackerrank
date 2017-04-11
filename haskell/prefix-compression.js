const fs = require('fs');

const [l1, l2] = fs.readFileSync('prefix-compression.in').toString().split('\n');

let pref = 0;
while (pref < l1.length && l1[pref] === l2[pref]) pref++; 

console.log(pref);
