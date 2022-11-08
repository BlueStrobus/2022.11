const loginForm = document.getElementById("login-form");
const loginInput = document.querySelector("#login-form input");
const loginButten = document.querySelector("#login-form rutten");

function onloginBtnClick() {
    const username = loginInput.value;
    if(username ==="") (
        alert("Please write your name.")
    ) else if (username.length > 15){
        is tool length.");
    }
    console.log("unlock");
}
loginButten.addEventListener("click", onloginBtnClick);
console.dir(loginInput)

