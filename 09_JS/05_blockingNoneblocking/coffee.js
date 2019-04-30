function makeCoffee(order, serve) {
    let cup;

    // 커피 기계 밑에서 걸리는 시간
    setTimeout(() => {
        cup = order;
        serve(cup)
    }, 2000);
    return cup;
}

// console.log(makeCoffee("Americano"));

const myCoffee = makeCoffee("latte", console.log);