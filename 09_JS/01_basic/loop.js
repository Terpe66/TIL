let i = 0;

// while loop
while (i < 10) {
    console.log(`i: ${i}`);
    i++;
}

// for loop
for (let j = 0; j < 10; j++) {
    console.log(`j: ${j}`)
}
/*
    sum = 0
    for number in [1, 2, 3]:
        sum += number

    print(sum)
 */

let sum = 0;
for (let number of [1, 2, 3]) {
    sum += number;
}
console.log(sum);

for (const char of "JS2JS") {
    console.log(char);
}
