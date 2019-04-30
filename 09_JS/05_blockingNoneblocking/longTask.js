function complexTask() {
    for (let i = 0; i < 1000000000; i++) {
        if (i % 100000 === 0) {
            console.log(i)
        }
    }
    console.log("오-래 걸림");
}

setTimeout(() => console.log("JS"), 1);
complexTask();