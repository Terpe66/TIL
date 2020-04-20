typeof 1 // "number"
typeof (typeof 1) // "string"

typeof (() => {}) // "function"
typeof function(){} // "function"
typeof (function() {}) // "function"

typeof (NaN) // "number" 숫자 연산이 잘못돼서 나오는 number
// "a" / 100 처럼 숫자 연산이 안 되는 경우에 NaN
// 200 + "a"는 200a
// "123" + 1은 1231
// "123" * 0은 0, "123" * 1은 123
// 100 / 0은 다른 언어에서 멈추지만, JS에서는 Infinity

aa = {
    a : 1,
    b : 2,
}
aa.c // undefined 몰라!
// null과 undefined는 비슷하지만 "비어있다"와 "모른다"의 차이가 있다
typeof null // object
typeof {} // object
typeof [] // object