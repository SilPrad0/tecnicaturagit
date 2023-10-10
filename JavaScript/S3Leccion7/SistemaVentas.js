//SistemasVentas
// create new class for SistemaVentas that has idProducto, nombre, precio. And its getters and setters
//mostrar id de cada producto y precio de cada producto

class Producto {
    static contadorProductos = 0;   //creo que este static contador faltaba para que no mostrara NaN en id
    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto() {
        return this._idProducto;
    }
    set idProducto(idProducto) {
        this._idProducto = idProducto;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get precio() {
        return this._precio;
    }
    set precio(precio) {
        this._precio = precio;
    }
    toString(){
        return `idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: ${this._precio}`;
    }
}

class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS(){
        return 5;
    }
    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }
    get idOrden(){
        return this._idOrden;
    }

    agregarProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(producto);
        } 
        else{
            console.log("no se puede agregar mas productos");
        }
    }  //fin del metodo agregarProducto

    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
        }
        return totalVenta;
    } // fin del metodo calcularTotal

    mostrarOrden(){
        let productoOrdenes = "";
        for(let producto of this._productos){
            productoOrdenes += `idProducto: ${producto._idProducto}, nombre: ${producto.nombre}, precio: ${producto.precio}\n`;	
        } // fin del for
        return `Orden: ${this._idOrden}, Total: ${this.calcularTotal()}, productos: ${productoOrdenes}`;
    } // fin del metodo mostrarOrden


} //fin de la clase Orden

let producto1 = new Producto("Pantalón", 5000);
let producto2 = new Producto("Remera", 6000);
let producto3 = new Producto("Billetera", 7000);
let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden2.agregarProducto(producto3);  
console.log(orden1.mostrarOrden());
