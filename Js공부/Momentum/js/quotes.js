//명언
const quotes = [
    {
        quote: "큰 목표를 이루고 싶으면 허락을 구하지 마라.",  //오브젝트?
        author: "미상",
    },
    {
        quote: "일반적인 것을 잃을 위험을 감수하지 않으면 평범한 것에 만족해야 한다.",
        author: "짐 론",
    },
    {
        quote: "위대한 정신을 가진 사람들은 생각을 논한다. 평범한 사람들은 사건을 논한다. 마음이 좁은 사람들은 사람들을 논한다.",
        author: "엘리너 루즈벨트",
    },
    {
        quote: "간단하게 설명할 수 없으면 제대로 이해하지 못하는 것이다.",
        author: "알버트 아인슈타인",
    },
    {
        quote: "성공은 매일 반복한 작은 노력들의 합이다.",
        author: "로버트 콜리어",
    },
    {
        quote: "모든 성취의 시작점은 갈망이다.",
        author: "나폴레온 힐",
    },
];

const quote = document.querySelector("#quotes span:first-child"); //파일명
const authar = document.querySelector("#quotes span:last-child");

console.log(Math.floor(Math.random() * quotes.length)); //floor은 소숫점 아래 버림
const todayQuost = quotes[Math.floor(Math.random() * quotes.length)]
 

quote.innerText = todayQuost.quote;
authar.innerText = todayQuost.author;