const cart = {
    items: [],

addItem(product) {
    const existingItem = this.items.find(item => item.id === product.id);

    if (existingItem) {
        existingItem.quantity++;
    } else {
        const newItem = {
            id: product.id,
            name: product.name,
            price: product.price,
            quantity: 1
        };
        this.items.push(newItem);
    }
},

removeItem(productId) {
    const index = this.items.findIndex(item => item.id === productId);

    if (index !== -1) {
        this.items.splice(index, 1);
    }
},

getTotalPrice() {
    return this.items.reduce((total, item) => total + item.price * item.quantity, 0);
},

getCart() {
        return this.items;
    },
};

export default cart;
