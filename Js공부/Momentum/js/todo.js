const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = toDoForm.querySelector("input");


function handleToDoSubmit(event) {
    event.preventDefault();
  //  console.log(toDoInput.value); //콘솔확인
    const newToDo = toDoInput.value;
    toDoInput.value = ""
    paintToDO(newToDo);
} 
function paintToDO(newToDo) {
    const li =document.createElement("li");
    const span =document.createElement("span")
    li.appendChild(span);
    span.innerText = newToDo;
    console.log(li);
}
toDoForm.addEventListener("submit", handleToDoSubmit);



//  html에서 가져오는 부분
// <from id="todo-form">
//       <input type="text" placeholder="write a To Do and Prese enter" required/>
//     </from>
//     <ul id="todo-list"></ul>