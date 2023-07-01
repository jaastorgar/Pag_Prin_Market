// Variables globales para almacenar los productos del carrito y el precio total
let cartItems = [];
let totalPrice = 0;

// Función que se ejecuta al hacer clic en el botón "Añadir al carrito" de un producto
function addToCart(productName, addButton) {
  // Obtener el elemento del producto actual
  const product = addButton.parentNode.parentNode;
  
  // Obtener el nombre y el precio del producto
  const name = product.querySelector(".product-details h3").textContent;
  const price = parseFloat(product.querySelector(".price").textContent.replace("$", ""));
  
  // Comprobar si el producto ya existe en el carrito
  const existingItem = cartItems.find((item) => item.name === name);
  if (existingItem) {
    // Incrementar la cantidad del producto si ya existe en el carrito
    existingItem.quantity++;
  } else {
    // Agregar el producto al carrito si no existe
    cartItems.push({ name: name, quantity: 1, price: price });
  }

  // Actualizar el precio total
  totalPrice += price;

  // Actualizar la visualización del carrito
  updateCart();

  // Mostrar el contenedor del carrito
  const cartContainer = document.getElementById("cart-container");
  cartContainer.style.display = "block";

  // Cambiar el texto del botón a "Añadir otro"
  addButton.textContent = "Añadir otro";
}

// Función para actualizar la visualización del carrito
function updateCart() {
  // Obtener los elementos del carrito
  const cartItemsElement = document.getElementById("cart-items");
  const cartTotalElement = document.getElementById("cart-total");

  // Limpiar el contenido previo del carrito
  cartItemsElement.innerHTML = "";

  // Iterar sobre los productos del carrito
  cartItems.forEach((item) => {
    // Crear un elemento <li> para mostrar cada producto en el carrito
    const li = document.createElement("li");
    
    // Establecer el texto del <li> con el nombre, cantidad y precio del producto
    li.textContent = `${item.name} (${item.quantity}) - Precio: $${item.price.toFixed(2)}`;

    // Crear los botones "+" y "-"
    const incrementButton = document.createElement("button");
    const decrementButton = document.createElement("button");
    
    // Establecer el texto y las clases de los botones
    incrementButton.textContent = "+";
    decrementButton.textContent = "-";
    incrementButton.classList.add("quantity-button");
    decrementButton.classList.add("quantity-button");

    // Asignar eventos de clic a los botones
    incrementButton.addEventListener("click", () => incrementCartItem(item));
    decrementButton.addEventListener("click", () => decrementCartItem(item));

    // Agregar los botones al elemento <li>
    li.appendChild(decrementButton);
    li.appendChild(incrementButton);

    // Agregar el elemento <li> al carrito
    cartItemsElement.appendChild(li);
  });

  // Actualizar el precio total del carrito
  cartTotalElement.textContent = `Total: $${totalPrice.toFixed(2)}`;
}

// Función para incrementar la cantidad de un producto en el carrito
function incrementCartItem(item) {
  item.quantity++;
  totalPrice += item.price;
  updateCart();
}

// Función para decrementar la cantidad de un producto en el carrito
function decrementCartItem(item) {
  if (item.quantity > 1) {
    item.quantity--;
    totalPrice -= item.price;
  } else {
    // Eliminar el producto del carrito si la cantidad es 1
    const itemIndex = cartItems.findIndex((i) => i.name === item.name);
    cartItems.splice(itemIndex, 1);
    totalPrice -= item.price;
  }
  updateCart();
}

// Función para realizar la compra
function checkout() {
  if (cartItems.length === 0) {
    // Mostrar una alerta si el carrito está vacío
    alert("El carrito está vacío. Añade productos antes de realizar la compra.");
  } else {
    // Mostrar una alerta de compra exitosa y reiniciar el carrito
    alert("Compra realizada con éxito. ¡Gracias por tu compra!");
    cartItems = [];
    totalPrice = 0;
    updateCart();

    // Ocultar el contenedor del carrito
    const cartContainer = document.getElementById("cart-container");
    cartContainer.style.display = "none";
  }
}
