// const fs = require('fs');
const readline = require("readline");
const rl = readline.createInterface({
  // input: fs.createReadStream('input.txt'),
  input: process.stdin,
  output: process.stdout,
});

let currentLine = 0;
let inputString = [];

rl.on("line", (line) => {
  inputString[currentLine++] = line;
}).on("close", () => {
  currentLine = 0;
  main();

  process.exit(0);
});

const readLine = () => {
  return inputString[currentLine++];
};

const sumUp = (total, num) => {
  return total + num;
};

function main() {
  // let problems = parseInt(readLine());
  // let total = 0;
  // while (problems--) {
  //   let sureArray = readLine();
  //   sureArray = sureArray.split(" ").map((str) => parseInt(str));
  //   const sum = sureArray.reduce(sumUp, 0);
  //   if (sum >= 2) {
  //     total += 1;
  //   }
  // }
  // console.log(total);
}
