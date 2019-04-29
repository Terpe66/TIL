// ES5 for loop
// var avengers = [
//     { name: "Tony Stark" },
//     { name: "Steve Rogers" },
//     { name: "Thor" }
// ];
//
// var avenger;
//
// for (var i = 0; i < avengers.length; i ++) {
//     if (avengers[i].name === "Steve Rogers") {
//         avenger = avengers[i];
//         break
//     }
// }
// console.log(avenger);

// ES6 +
const avengers = [
    {name: "Tony Stark"},
    {name: "Steve Rogers"},
    {name: "Thor"}
];

const a = avengers.find(avenger => avenger.name === "Steve Rogers");

console.log(a);