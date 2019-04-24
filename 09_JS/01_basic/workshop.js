/*
    아래 Python 코드를 JS 코드로 변환해보자.
    Checkpoint
    1. 브라우저는 생각하지 않는다.
    2. 변수/함수 이름은 JS naming convention(lowerCamelCase) 을 따른다.
    3. F String => Template Literal.
 */

// # This is Comment
// def concat(str1, str2): return f'{str1} - {str2}'
// def check_long_str(string): if len(string) > 10: return True else: return False
// if check_long_str(concat('Happy', 'Hacking')): print('LONG STRING') else: print('SHORT STRING'

// This is Comment
function concat (str1, str2) {
    return `${str1} - ${str2}`;
}

const concat = (str1, str2) => `${str1} - ${str2}`;


function checkLongStr (string) {
    if (string.length > 10) {
        return true;
    }
    else {
        return false;
    }
}

/*
    const checkLongStr = string => {
        if (string.length > 10) {
            return true;
        }
        else {
            return false;
        }
    };
 */

const checkLongStr = string => string.length > 10;


if (checkLongStr(concat("Happy", "Hacking"))) {
    console.log("LONG STRING");
}
else {
    console.log("SHORT STRING");
}

checkLongStr(concat("Happy", "Hacking")) ? console.log("LONG STRING") : console.log("SHORT STRING");
console.log(checkLongStr(concat("Happy", "Hacking")) ? "LONG STRING" : "SHORT STRING");
