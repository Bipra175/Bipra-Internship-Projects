// # The function adds selected item to cart
function addToCart(item) {
  alert(item + " added to cart!");
}

// # The function sends contact form message
function sendMessage(e) {
  e.preventDefault();
  alert("Thank you! Your message has been sent.");
  e.target.reset();
}
