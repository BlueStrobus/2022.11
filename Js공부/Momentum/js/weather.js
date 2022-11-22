const API_KEY = "";
const ID_WEATHER = "weather";
navigator.geolocation.getCurrentPosition(onGeoOK, onGeoError); //위치 찾기
function onGeoOK(position) {
    const lat = position.coords.latitude;  //사용자 위치 찾기-위도,경도
    const lon = position.coords.longitude;
    const url = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    fetch(url)
    .then((response) => response.json());
    .then((data) => {
        console.log(data.name, data.weather[0].main);
        const weather = document.querySelector( #${ID_WEATHER} span:first-child);
        const city = document.querySelector( #${ID_WEATHER} span:last-child);
        weather.innerText = ${data.weather[0].main} / ${data.main.temp} ;
        city.innerText = data.name;
    });
}

function onGeoError() {   //위치 못찾았을 때
    alert("Can't find you. No weather for you.");
}











//http://openweathermap.org/