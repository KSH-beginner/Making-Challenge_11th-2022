# OpenWeather API 불러오기

### 1. OpenWeather에서 원하는 API 선택

[Weather API](https://openweathermap.org/api)

### 2. Ajax로 api 얻기

홈페이지에서 나온 api 주소는 다음과 같다.

`api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}`

`{city name}` 에는 정보를 얻고자 하는 도시 이름 / `{API key}` 에는 자신의 ID Key

이렇게 넣고 Ajax로 console에 찍어봤다.

```java
$.ajax({
  type: "GET",
  url: "api.openweathermap.org/data/2.5/weather?q=Seoul&appid=709156e8033c3ec6ce56b13372f7a1bd",
  data: {},
  success: function (response) {
    console.log(response);
  },
});
```

👉 콘솔에 찍히지 않고, GET 404 오류가 발생했다. → 이는 URL에 오류가 있다는 것.

💡 구글링도 하고 엄청 삽질했는데 앞에 `http://` 가 없어서 발생한 오류였다...

`url:"http://api.openweathermap.org/data/2.5/weatherq=Seoul&appid=709156e8033c3ec6ce56b13372f7a1bd"`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25844755-56cc-4614-8ea2-be124696e62d/Untitled.png)

### 3. 가져올 정보 추출

response에 정보들이 담기므로 response를 잘 제어하면 된다.

**※ 가져올 리스트 이름에는 `""`을 붙여서 가져와야 한다.**

`response[weather]` (X)

`response["weather]` (O)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1df2bfc3-11ee-4869-9b33-072e1032ad53/Untitled.png)

---

### OpenWeather API 날씨 종류

`main` : Clear / Clouds(few clouds, overcast clouds) / Rain(light rain, moderate rain) / 

`description` : few clouds / clear sky / overcast clouds / light rain / moderate rain

[Weather Conditions](https://openweathermap.org/weather-conditions)

→ ID 번호로 나누면 될듯??

ID 200~299 : Thunderstorm (폭풍우)

ID 300~399 : Drizzle (이슬비)

ID 500~ 599 : Rain(비)

👉 **ID 200~599 : Rainy으로 묶기**

ID 600~699 : Snow (눈)

👉 **ID 600~699 : Snowy로 묶기**

ID 700~799 : mist(안개)

ID 801~804 : Clouds (흐림)

👉 **ID 700~804 : Cloudy로 묶기**

ID 800 : Clear (맑음)

👉 **ID 800 : Sunny**
