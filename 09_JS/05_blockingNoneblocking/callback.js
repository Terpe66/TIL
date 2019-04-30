// function listUsers() {
//     setTimeout(() => {
//         const users = [
//             {id: 1, githubID: "eduyu"},
//             {id: 2, githubID: "edujohn"},
//         ];
//         return users;
//     }, 2000);
// }

// getUser(1, listUsers());

function getUser(id, callback) { // non-blocking 함수에서 불러온 값을 쓰기 위해서 callback 함수를 사용
    setTimeout(() => {
        const users = [
            {id: 1, githubID: "eduyu"},
            {id: 2, githubID: "edujohn"},
        ];
        const user = users.find(user => user.id === id);
        console.log("Data Loaded!");
        console.log(user);
        // console.log(user);
        callback(user);
    }, 2000);
}

const getRepos = (user, callback) => {
    setTimeout(() => {
        const repos = [
            "TIL",
            "Workshop_HW",
            "Python",
            "JS"
        ];
        console.log("Data Loaded");
        console.log(repos);
        callback(repos)
    }, 2000)
};

// console.log("Start Program");
// const user = getUser(1); // 백오피스로 넘어가기 때문에 return으로 넘겨받은 게 없음
// console.log(user);
// console.log("End of Program");

function getCommits(repo, callback) {
    setTimeout(() => {
        const commits = [
            "Init repo",
            "Make index.html"
        ];
        console.log("Data Loaded!");
        console.log(commits);
        callback(commits);
    }, 2000)
}


getUser(1, user => {
    getRepos(user, repos => {
        getCommits(repos[0], commits => {
            console.log(`${commits.length} commits!`)
        })
    })
});

// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])
// time = getTimeFromCommit(commits[0])