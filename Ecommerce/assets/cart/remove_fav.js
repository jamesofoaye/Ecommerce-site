const removeFav = document.querySelectorAll(".remove-favourites");
removeFav.forEach((DOMFav) => {
  DOMFav.addEventListener("click", (e) => {
    let productName = e.target.dataset.name;
    let action = e.target.dataset.action;

    if (user == "AnonymousUser") {
      alert("Please login");
    } else {
      removeFavourite(productName, action);
    }
  });
});

function removeFavourite(productName, action) {
  let url = "/remove_favorite/";

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
