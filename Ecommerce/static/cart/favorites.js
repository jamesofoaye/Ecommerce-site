const addDOMFav = document.querySelectorAll(".favbtn");

addDOMFav.forEach((addFav) => {
  addFav.addEventListener("click", (e) => {
    let productName = e.target.dataset.name;
    let action = e.target.dataset.action;

    if (user == "AnonymousUser") {
      alert("Please login");
    } else {
      addToFavourite(productName, action);
    }
  });
});

function addToFavourite(productName, action) {
  console.log("User logged in sending data");

  let url = "/add_fav/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productName, action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      alert(data);
      window.location.reload();
    });
}
