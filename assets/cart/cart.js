const addCartsBtn = document.querySelectorAll(".btn-add-cart");

addCartsBtn.forEach((addCart) => {
  addCart.addEventListener("click", (e) => {
    let productId = e.target.dataset.id;
    let action = e.target.dataset.action;

    if (user == "AnonymousUser") {
      alert("Please login");
    } else {
      updateUserOrder(productId, action);
    }
  });
});

function updateUserOrder(productId, action) {
  console.log("User logged in sending data");

  let url = "/update_item/";

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
