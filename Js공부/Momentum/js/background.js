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