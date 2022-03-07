var accessToken =
  "BQDiDyDY36B2K1xXqB124KQc9dzVl97vqftj7kCYUi2y9EY6q0tnUz7ja2L13hRt_0f0Wkzab4mioawl2BHHHZV5vGzltPIawbyrEJFJGKkFejWtU3Lcl3OmoBLvez5X_iGZe-CEPK2n01lU2uPFOuB4xWkvC7v-e2_eQLho1UVtS_uagh7CPM9fvQ";
$.ajax({
  url: "https://api.spotify.com/v1/search?q=eight&type=artist,track&include_external=audio&limit=1",
  type: "GET",
  headers: {
    Authorization: "Bearer " + accessToken,
  },
  success: function (data) {
    console.log(data);
  },
});

$.ajax({
  type: "GET",
  url: "http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=709156e8033c3ec6ce56b13372f7a1bd",
  data: {},
  success: function (response) {
    console.log(response);
  },
});
