function hi() {

}

const bye = () => {

};

const me = {
    name : "우너",
    phone : "01012345678",
    email : "terpe66@gmail.com",
    intro : function () {
        return `Hi my name is ${this.name}`
        // function 안에 있는 this는 intro랑 같이 있기 때문에 정상적으로 작동한다
    }
};

const you = {
    name : "지또니",
    phone : "01012345678",
    email : "jiji@gmail.com",
    intro : () => {
        return `Hi my name is ${this.name}`
        // => 안에 있는 this는 intro가 아니라 상위 레벨인 you를 바라보기 때문에 작동하지 않는다
    },
    wait : function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    }
};

console.log(me.intro());
console.log(you.intro());
console.log(you.wait());

// javascript의 객체는 {}, key랑 value로 이루어져 있다.

// [1, 2, 3, 4, 5].length [1, 2, 3, 4, 5]라는 object에 length라는 key가 있어서 .length는 메소드가 아니라 key로 value를 호출하는 형식으로 실행 됨