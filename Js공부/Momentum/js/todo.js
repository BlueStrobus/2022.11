const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = toDoForm.querySelector("input");
const toDos = [];
const TODOS_KEY = "todos";
const savedToDos = localStorage.getItem(TODOS_KEY);
if(savedToDos != null) {
  const parsedToDos = JSON.parse(savedToDos); //함수는() parse는 배열임
  console.log(parsedToDos);
  parsedToDos.forEach((item) => console.log("Hello", item)); //배열.위치(함수명)
  //배열 안의 각각의 요소(item)앞에 Hello 붙여서 출력
}

function handleToDoSubmit(event) {
    event.preventDefault();
  //  console.log(toDoInput.value); //콘솔확인
    const newToDo = toDoInput.value;
    toDoInput.value = "";
    toDos.push(newToDo); //문자열에 입력된 뉴투두를 투두스에 넣기   콘솔창에 toDos치고 엔터누르면 (3) ['1', '2', '3'] 나옴
    paintToDO(newToDo);
    saveToDos();
} 
function paintToDO(newToDo) {
    const li =document.createElement("li");
    const span =document.createElement("span")
    const button = document.createElement("button");
      //버튼 만들기
    button.innerText = "❌" //이모지는 윈도우 + 점.  
    button.addEventListener("click", deleteToDo);
    li.appendChild(span); //spen이 할일 문자
    li.appendChild(button); //삭제버튼 이모지 보이게 만들기
    span.innerText = newToDo;  // span에 적은 text를 newToDo로 만듦...추가?
    toDoList.appendChild(li); // 투두리스트에 자식으로 li넣기
}

// X 버튼 누르면 삭제됨
function deleteToDo(event) {
  //console.log(event) //콘솔에 이벤트 눌러서 타겟(버튼), 페런트 엘레멘탈이 뭔지 찾아서 삭제할 수 있게 만들기
  const li = event.target.parentElement;
  li.remove();
}

function saveToDos() {
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos)); //제이슨 형태의 스트리밍으로 바꿔줌???
}


toDoForm.addEventListener("submit", handleToDoSubmit);

//할일 추가함, 새로고침 누르면 할일 리스트 삭제됨
//appendChild : 부모 자식에 자식 노드를 추가하는 메서드


//  html에서 가져오는 부분
// <from id="todo-form">
//       <input type="text" placeholder="write a To Do and Prese enter" required/>
//     </from>
//     <ul id="todo-list"></ul>



{/* <바디>

    //createElement
    //<li></li>   //const li =document.createElement("li");
    //<spen></spen>   //const span =document.createElement("span")
    //<button></button>   //const button = document.createElement("button");

    <ul id="todo-list">   //ul은 리스트 모음
       <li> // toDoList.appendChild(li)  toDoList에 li(리스트)를 자식으로(?) 넣기
        <span></span> //li.appendChild(span);   li 리스트에 spen(할일 적은 텍스트)를 자식으로(?) 넣기
        <button></button> //li.appendChild(button); li 리스트에 button(❌)를 자식으로(?) 넣기

       </li>
    
    
      </ul>





</바디>  */}