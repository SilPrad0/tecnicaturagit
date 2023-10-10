import products from "./products.mjs";
import cart from "./cart.mjs";

if (typeof document !== 'undefined') {
    document.addEventListener("DOMContentLoaded", function() {
        const shopContent = document.getElementById('shopContent');
        const cartContent = document.getElementById('cartContent');
        const totalDisplay = document.getElementById('totalDisplay');

        function updateCartDisplay() {
            console.log('[DEBUG] updateCartDisplay() called');
            cartContent.innerHTML = '';

            const cartItems = cart.getCart();
            console.log('[DEBUG] Cart Items:', cartItems);

            cartItems.forEach(item => {
                const cartItemDiv = document.createElement("div");
                cartItemDiv.className = "cart-item";
                cartItemDiv.innerHTML = `
                    <span>${item.name} x ${item.quantity}</span>
                    <span>$${item.price * item.quantity}</span>
                    <button data-id="${item.id}" class="remove-button">x</button>
                `;
                cartContent.append(cartItemDiv);
            });

            totalDisplay.textContent = `Total: $${cart.getTotalPrice().toFixed(2)}`;
            console.log('[DEBUG] updateCartDisplay() finished');
        }

        products.forEach((product) => {
            const productDiv = document.createElement("div");
            productDiv.className = "product";
            productDiv.innerHTML = `
                <img src="${product.img}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>Precio: $${product.price}</p>
                <p>Disponibles: ${product.quantity}</p>
                <button data-id="${product.id}" class="buy-button">Comprar</button>
            `;
            shopContent.append(productDiv);

            const buyButton = productDiv.querySelector(".buy-button");
            buyButton.addEventListener("click", (e) => {
                const productId = e.target.getAttribute("data-id");
                const selectedProduct = products.find(product => product.id === parseInt(productId, 10));

                if (selectedProduct && selectedProduct.quantity > 0) {
                    console.log('[DEBUG] Buy button clicked');
                    cart.addItem(selectedProduct);
                    selectedProduct.quantity--;
                    console.log('[DEBUG] Selected product:', selectedProduct);
                    updateCartDisplay();
                }
            });
        });

        // Eliminar productos del carrito
        cartContent.addEventListener("click", (e) => {
            if (e.target.classList.contains("remove-button")) {
                const productId = e.target.getAttribute("data-id");
                cart.removeItem(parseInt(productId, 10));
                const selectedProduct = products.find(product => product.id === parseInt(productId, 10));
                if (selectedProduct) {
                    selectedProduct.quantity++;
                }
                console.log('[DEBUG] Product removed:', selectedProduct);
                updateCartDisplay();
            }
        });

        // Actualizar
        updateCartDisplay();
    });
}
