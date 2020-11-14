const removeDomCartItem = document.querySelectorAll(".remove-cart");
removeDomCartItem.forEach((removeItem) => {
  removeItem.addEventListener("click", (e) => {
    let productId = e.target.dataset.id;
    let action = e.target.dataset.action;

    if (user == "AnonymousUser") {
      alert("Please login");
    } else {
      removeCartItem(productId, action);
    }
  });
});

function removeCartItem(productId, action) {
  let url = "/remove_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId, action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      alert(data);
      window.location.reload();
    });
}
