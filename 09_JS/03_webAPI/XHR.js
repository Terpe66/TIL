// XHR.js
// const URL = "https://jsonplaceholder.typicode.com/posts";
const DOMAIN = "https://jsonplaceholder.typicode.com/";
const RESOURCE = "posts";
const QUERY_STRING = "";

const URL = DOMAIN + RESOURCE + QUERY_STRING;

// req 대리인 XQR 객체 생성
const XHR = new XMLHttpRequest();
// XHR 요청 전송 준비 (method, url 같이 넘겨줘야 함)

// 요청 만들고, 정보를 담고, 보내고, 기다리고
XHR.open("POST", URL);

// POST 요청일 때 뭘 보낸 건지 명시해줘야 한다
XHR.setRequestHeader(
    "Content-Type",
    "application/json;charset=UTF-8"
);
// 데이터는 body에 있고 관련 정보는 header에 있다

// XHR 요청 전송
// XHR.send(); // GET일 때
// POST일 때 여기로 JSON을 보내야 함
XHR.send( // serializing (파싱과 상반되는 것)
    JSON.stringify({ "title": "NewPost", "body": "This is New Post", "userId": 1 })
);

XHR.addEventListener("load", e => {
    // const rawData = e.target.response; // 이 상태에서는 rawData를 쓸 수 없음
    // const parseData = JSON.parse(rawData) // 파싱해줘서 이제 쓸 수 있음
    const parseData = JSON.parse(e.target.response);
    console.log(parseData);
});