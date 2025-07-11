#!/usr/bin/node

const nums = process.argv.slice(2).map(n => parseInt(n));
if (nums.length < 2) {
  console.log(0);
} else {
  let max1 = -Infinity;
  let max2 = -Infinity;
  for (const n of nums) {
    if (n > max1) {
      max2 = max1;
      max1 = n;
    } else if (n > max2 && n < max1) {
      max2 = n;
    }
  }
  console.log(max2);
}
