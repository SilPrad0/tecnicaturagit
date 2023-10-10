// tipos de datos en js
var nombre = "silvina"; //STR
console.log(typeof nombre);
nombre = 7;
var numero = 10; // tipo num
console.log(typeof nombre);
// tipo objeto
var objeto = {
    nombre: "sil", apellido: "prado", tel: "3245643"
}
console.log(typeof objeto);
//tipo booleano data
var bandera = true;
console.log(bandera);

//tipo de dato funcion
function  miFuncion(){}
console.log(typeof miFuncion);7

//symbol
var simbolo = Symbol("simbolo js");
console.log(typeof simbolo);

//clases
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);
//tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

//null: ausencia de valor
var y = null;  //null no es un tipo de dato, pero su origen es object
console.log(y);

//Tipo de dato array
var autos = ['Citroen','Fiat','Peugeot'];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z);