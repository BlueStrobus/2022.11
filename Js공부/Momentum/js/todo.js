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
    const button = document.createElement("button");
      //버튼 만들기
    button.innerText = "❌" //이모지는 윈도우 + 점.  
    li.appendChild(span);
    li.appendChild(button); //삭제버튼 이모지 보이게 만들기
    span.innerText = newToDo;
    toDoList.appendChild(li); //부모 자식에 자식 노드를 추가하는 메서드
}
toDoForm.addEventListener("submit", handleToDoSubmit);

//할일 추가함, 새로고침 누르면 할일 리스트 삭제됨

//  html에서 가져오는 부분
// <from id="todo-form">
//       <input type="text" placeholder="write a To Do and Prese enter" required/>
//     </from>
//     <ul id="todo-list"></ul>