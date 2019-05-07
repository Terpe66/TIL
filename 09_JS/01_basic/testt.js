function func1 (cb1, cb2) {
    console.log(1);
    cb1(cb2(cb1))
}
function func2 (callback) {
    console.log(2);
}
function func3 (callback) {
    console.log(3);
}

func1(func2, func3)