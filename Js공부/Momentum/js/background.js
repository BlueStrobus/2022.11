//배경

const images = [
    "3.jfif",
    "blue2.jfif",
    "blueMoon.jfif"
];

const chosenImage = images[Math.floor(Math.random() * images.length)];
const bgImage = document.createElement("img");
bgImage.src = `img/${chosenImage}`;
console.log(bgImage);

 
//콘솔창에 세로고침 하면 이미지 이름 바뀌는것 확인



// const quote = document.querySelector("#quotes span:first-child"); //파일명
// const authar = document.querySelector("#quotes span:last-child");

// console.log(Math.floor(Math.random() * quotes.length)); //floor은 소숫점 아래 버림
// const todayQuost = quotes[Math.floor(Math.random() * quotes.length)]
 

// quote.innerText = todayQuost.quote;
// authar.innerText = todayQuost.author;