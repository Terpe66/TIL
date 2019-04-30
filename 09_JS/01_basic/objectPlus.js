function makeArticle1(id, title, content) {
    return {
        id: id,
        title: title,
        content: content,
        makeOne: function () {
            return `${this.id}번 글: ${this.title} => ${this.content}`
        }
    }
}

function makeArticle2(id, title, content) {
    return { // key랑 value가 같으면 아래처럼 가능. 이 방식에선 웬만하면 function, arrow function( => )은 callback 함수 만들 때 사용
        id,
        title,
        content,
        makeOne () {
            return `${this.id}번 글: ${this.title} => ${this.content}`
        }
    }
}
