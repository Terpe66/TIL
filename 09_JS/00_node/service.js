const utility = require("./utility");
const accountA = 100;
const accountB = 200;
const accountC = 400;
const totalAccounts = utility.addAll([accountA, accountB, accountC]);

console.log(totalAccounts);
console.log(utility.phoneNumber);