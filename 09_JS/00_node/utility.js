// function addAll (numbers=[]) {
//     let sum = 0;
//     numbers.forEach(number => sum += number);
//     return sum;
// }
//
// function subAll (numbers=[]) {
//     let sum = 0;
//     numbers.forEach(number => sum -= number);
//     return sum
// }
//
// function mulAll (numbers=[]) {
//     let mul = 1;
//     numbers.forEach(number => mul *= number);
//     return mul
// }

// module.exports = { // 이렇게 써 줘야 다른 데에서 import 할 수 있다
//     addAll,
//     subAll,
//     mulAll
// };

module.exports = {
    addAll(numbers = []) {
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },

    subAll(numbers = []) {
        let sum = 0;
        numbers.forEach(number => sum -= number);
        return sum;
    },

    mulAll(numbers = []) {
        let mul = 1;
        numbers.forEach(number => mul *= number);
        return mul;
    },

    name: "JS"
};

phoneNumber = "01020304050";

module.exports.phoneNumber = phoneNumber;