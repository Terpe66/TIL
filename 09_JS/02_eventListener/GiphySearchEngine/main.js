/* 1. <input> 태그 안의 값을 잡는다. */
const init = () => {
    const inputArea = document.querySelector("#js-userinput");
    const button = document.querySelector("#js-go");

// 엔터 칠 때
    inputArea.addEventListener("keydown", e => {
        if (e.key === "Enter") {
            searchAndPush(inputArea.value);
        }
    });

    button.addEventListener("click", e => {
        searchAndPush(inputArea.value);
    });
};

/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */
const searchAndPush = keyword => {
// let keyword = document.querySelector("#js-userinput");
    const KEY = "064x7Ja5cBBPv1DwgKFah6VCcBCJpapw";
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;
// console.log(URL);

    const AJAXCall = new XMLHttpRequest();
    AJAXCall.open("GET", URL);
    AJAXCall.send(); // 발사
    AJAXCall.addEventListener("load", e => {
        const parseData = JSON.parse(e.target.response);
        pushToDOM(parseData);
    });

    const pushToDOM = dataset => {
        const resultArea = document.querySelector("#result-area");
        resultArea.innerHTML = null;
        const dataArray = dataset.data;
        let imageURL, element;
        for (const imgData of dataArray) {
            imageURL = imgData.images.fixed_height.url;
            element = document.createElement("img"); // img 태그 만들기
            element.classList.add("container-image"); // img 태그의 클래스명
            element.src = imageURL;
            element.alt = imgData.title;
            // resultArea.innerHTML += `<img src="${imageURL}">`;
            resultArea.appendChild(element);
        }
    };
};

init();

// AJAX 요청을 보낸다.
/*
    기존의 요청
    1. 링크를 누른다.
    2. href로 요청이 간다.
    3. 브라우저가 새로고침 되며, 응답을 render 한다.

    AJAX 요청
    1. 어떤 event가 발생한다.
    2. 요청을 전송하고, 응답이 도착할 때까지 기다린다. 화면 전환은 없다.
    3. 응답이 오면 지금 문서에서 응답 내용을 추가로 render한다.
 */
// const AJAXCall = new XMLHttpRequest(); // AJAX 요청을 보내줄 친구
// AJAXCall.open("GET", URL); // 요청을 보낼 준비가 끝났다
// AJAXCall.send(); // 발사
// AJAXCall.addEventListener("load", e => { // load를 기다리며... res가 오면,
//     const parseData = JSON.parse(e.target.response);
//     pushToDOM(parseData);
// });

/* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */
// const pushToDOM = dataset => {
//     const dataArray = dataset.data;
//     for (const imgData of dataArray) {
//         imageURL = imgData.images.fixed_height.url;
//         resultArea.innerHTML += `<img src="${imageURL}">`;
//     }
// };