function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b;
}

// Llamo a la funcion
miFuncion(5, 3);

let resultado = miFuncion(6, 7);
console.log(resultado)
// funcion tipo expresion
let x = function(a, b){return a + b};
resultado = x(21, 34);
console.log(resultado);

// F tipo self e invoking
(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 8);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments);
}

miFuncionDos(3, 5, 67); 

// toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

// funciones flecha 
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(45, 67);
console.log(resultado);

let sumar = function(a, b){
    console.log(arguments[0]); //muestro los parametros
    console.log(arguments[1]);
}

resultado = sumar(3);
//como solo pongo un argumento por default es el a. El b queda undefined

// Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 6, 56, 43);    //LLAMO a la F antes de ser creada: HOISTING
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma;
}

// tipos primitivos 
//paso por valor
let k = 10;
function cambiarValor(a){
    a = 20;
}

cambiarValor(k);
// paso por ref
const persona = {
    nombre: 'Dan',
    apellido: 'Djarin'
}

function cambiarValorObjeto(p1){
    p1.nombre = 'Cacho'
    p1.apellido = 'Etc'
}
cambiarValorObjeto(persona);
console.log(persona);
