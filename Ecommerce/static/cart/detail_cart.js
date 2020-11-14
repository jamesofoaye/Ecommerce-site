const addCartsBtn = document.querySelectorAll(".btn-add-cart");

addCartsBtn.forEach((addCart) => {
  addCart.addEventListener("click", (e) => {
    const DOMQuantity = document.querySelector(".quantity_value").value;

    let productId = e.target.dataset.id;
    let action = e.target.dataset.action;
    let quantity = DOMQuantity;

    if (user == "AnonymousUser") {
      alert("Please login");
    } else {
      updateUserOrder(productId, action, quantity);
    }
  });
});

function updateUserOrder(productId, action, quantity) {
  console.log("User logged in sending data");

  let url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId, action, quantity }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      alert(data);
      window.location.reload();
    });
}

const mainImg = document.querySelector(".main-img");
const subImg = document.querySelectorAll(".sub-img");

subImg.forEach((img) => {
  img.addEventListener("click", (e) => {
    imgSrc = img.src;
    mainImg.src = imgSrc;
  });
});
