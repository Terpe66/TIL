/*
    #1) function sleep_3s() 정의
    #2) console.log("Start Sleeping") 실행
    #3) sleep_3s() 실행, 내부 console.log("INVOKE") 실행
    #4) console.log("End of Program") 실행
    #5) 3초 후 console.log("Wake up!") 실행

    만약 실제로 3초를 기다리는 동안 아무 일도 일어나지 않으면?
    브라우저 클릭 등 작업이 하나도 되지 않을 거다
 */

function sleep_3s() {
    console.log("INVOKE");

    setTimeout(() => {
        console.log("Wake up!")
    }, 3000)
}

console.log("Start Sleeping");
sleep_3s();
console.log("End of Program");

// const logEnd = () => {
//     console.log("End of Program")
// };
//
// console.log("zZzZZ");
// setTimeout(logEnd, 3000);
// console.log("End of Program");

