const numbers = [1, 2, 3, 4,];

numbers[0] // 1
numbers[-1] // 불가능. undefined
numbers[4] // 불가능. undefined
numbers.length; // 4. len(numbers)

/* 원본이 달라지는 methods */
numbers.reverse(); // [4, 3, 2, 1,]
numbers // [4, 3, 2, 1,]
numbers.reverse(); // [1, 2, 3, 4,]

numbers.push("a"); // 5. [1, 2, 3, 4, a,].length

numbers.pop(); // "a". [1, 2, 3, 4,]
numbers.unshift("a"); // 5. [a, 1, 2, 3 ,4]

numbers.shift(); // "a". [1, 2, 3, 4]


/* copy, 다른 결과 return */
numbers.includes(1);
numbers.includes(0);

numbers.push("a", "a"); // test
numbers.indexOf("a"); // 4
numbers.indexOf("b"); // -1 => 없음

numbers.join("-"); // 1-2-3-4-a-a
numbers.join(""); // 1234aa
numbers.join(); // 1,2,3,4,a,a
