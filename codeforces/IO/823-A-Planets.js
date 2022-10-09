// "use strict";

// process.stdin.resume();
// // process.stdin.setEncoding("utf-8");

// let inputString = "";
// let currentLine = 0;

// process.stdin.on("data", (inputStdin) => {
//   inputString += inputStdin;
// });

// process.stdin.on("close", (_) => {
//   inputString = inputString
//     .trim()
//     .split("\n")
//     .map((string) => {
//       return string.trim();
//     });

//   main();
// });

// function readline() {
//   return inputString[currentLine++];
// }

// function main() {
//   const t = readline();
//   for (let i = 0; i < t; i++) {
//     let price = 0;
//     const [n, c] = readline()
//       .split(" ")
//       .map((x) => parseInt(x));
//     const a = readline()
//       .split(" ")
//       .map((x) => parseInt(x));

//     let obj = {};

//     a.forEach((e) => {
//       if (obj[e] == undefined) obj[e] = 1;
//       else obj[e]++;
//     });

//     Object.keys(obj).forEach((key) => {
//       if (obj[key] <= c) price += obj[key];
//       else price += c;
//     });

//     console.log(price);
//   }
// }
const fs = require('fs');
const readline = require('readline');
const rl = readline.createInterface({
  input: fs.createReadStream('sample.txt'),
  output: process.stdout,
});
reader = fs.createReadStream('input.txt');
// rl.prompt();

rl.on('line', (line) => {
  
      console.log(`Say what? I might have heard '${line.trim()}'`);
  
  
}).on('close', () => {
  console.log('Have a great day!');
  process.exit(0);
});