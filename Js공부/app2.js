const loginForm = document.getElementById("login-form");
const loginInput = document.querySelector("#login-form input");
const loginButten = document.querySelector("#login-form rutten");

function onLoginSubmit(event) {
    event.preventDefault(); //새로고침 막음
}

loginForm.addEventListener("submit", onLoginSubmit) //submit은 기본적으로 새로고침 기능이 있음. 매개변수(파라미트) 따로 지정 안해주면 새로고침 실행함
console.dir(loginInput);    
    
    
    
    
    
    
    /*const username = loginInput.value;
    if(username ==="") (
        alert("Please write your name.")
    ) else if (username.length > 15){
        is tool length.");
    }
    console.log("unlock");
}
loginButten.addEventListener("click", onloginBtnClick);
console.dir(loginInput)
*/
