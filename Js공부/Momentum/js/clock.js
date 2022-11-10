const clock = document.querySelector("h2#clock");

function getClock(){
    const date = new Date();
    const hours = String(date.getHours()).padStart(2, "0"); //문자열로 바꿈, 문자열은 pad스타트 쓸 수 있음,
    //(2, "0") 문자 길이가 2보다 작으면 앞에 0을 붙여라
    const minutes  = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");
    clock.innerText = `${hours}:${minutes}:${seconds}`;
}

getClock();
setInterval(getClock, 1000); // 1000ms(미리세컨드) = 1초마다


//setTimeout 은 한번만 실핻하는 것
//셋인터널 - 타이머,시간