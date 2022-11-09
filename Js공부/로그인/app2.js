// 이벤트 찾기
// oneventname  마우스 카피...
const loginForm = document.getElementById("login-form"); //로그인폼
const loginInput = document.querySelector("#login-form input"); //로그인폼에 인풋
const greeting = documment.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";
function paintGreeting(username) {
    greeting.innerText = 'Hello ${username}';
    greeting.classList.remove(HIDDEN_CLASSNAME);
}


//const loginButten = document.querySelector("#login-form butten");

function onLoginSubmit (event) {
    event.preventDefault();
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username);
    paintGreeting(userName);
    loginForm.classList.add(HIDDEN_CLASSNAME);
    console.log(username);
}
const savedUserName = localStorage.getItem(USERNAME_KEY);

    if(savedUserName === null) {
        loginForm.classList.remove(HIDDEN_CLASSNAME);
        loginForm.addEventListener("submit", onLoginSubmit);
    } else {
        paintGreeting(savedUserName);
    }
    
console.dir(loginInput);    


