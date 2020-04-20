/*
    def my_function(arg1, arg2):
        ...
        return value

    func = lambda arg1, arg2: value
 */


// 1. 함수 키워드 정의
// def를 function으로 바꿈
function add (num1, num2) {
    return num1 + num2;
}

// 2. 변수에 함수 로직 할당
const sub = function (num1, num2) {
    return num1 - num2;
};

// 3. 함수 표현식 2가지
const multi = function (num1, num2) {
    return num1 * num2;
};

/*
    step 1: function 키워드를 없앤다.
    step 2: ()와 로직{} 사이에 =>를 넣는다.
 */
const multi = (num1, num2) => {
    return num1 * num2;
};

/*
    추가 refactoring
    step 1: 인자가 단 하나라면, ()가 생략 가능
    step 2: 함수 블록 안의 코드가 return문 한 줄이라면 {}와 return 삭제 가능
 */

let square = function (num) {
    return num ** 2;
};

square = num => num ** 2;
square(3);

let noArgs = () => {
    return "nothing";
};

noArgs = () => "nothing";
oneArgs = a => "one";
manArgs = (a, b, c, d, e) => "wow";


/* Default Args */
function sayHello (name="JS") {
    return `hi ${name}!`;
}

const sayHello = (name="JS") => `hi ${name}`;

(num => num ** 2)(4); // 익명 함수를 실행하는 방법
