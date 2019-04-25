// fetch.js ES6+
const DOMAIN = "https://jsonplaceholder.typicode.com/";
const RESOURCE = "posts";
const QUERY_STRING = "";

const URL = DOMAIN + RESOURCE + QUERY_STRING;

// (만들고) => 정보를 담고 => 보내고 => 기다리고 => 처리한다

const getRequest = (URL) => {
    fetch(URL) // 만들고 => 정보를 담고 => 보내고
        .then(response => response.json()) // 기다리고 => 도착한 데이터를 파싱
        .then(parseData => console.log(parseData));
}; // then으로 연결하는 게 chaining인데 이 코드 잘 안 씀

const postRequest = URL => {
    fetch(URL, { // POST 방식엔 오브젝트가 추가 되어야 한다. 만들고 => 정보를 담고 => 보내고
        method: "POST",
        body: JSON.stringify({
            title: "new post",
            content: "new content",
            userId: 1
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then(response => response.json()) // 기다리고 => 도착한 데이터를 파싱
        .then(parseData => console.log(parseData));
};