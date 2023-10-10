// let persona3 = new Persona('ADSF','sdgs'); no se puede acceder persona before initialization
// no se aplica el concepto de hoisting para clases, pero si para funciones y variables

class Persona{   // clase padre

    static contadorPersonas = 0;
    //email = 'valor default email';  //atributo no estatico

    static get MAX_OBJ(){  // metodo para simular una constante
        return 5;
    }

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        //Persona.contadorObjetosPersona++;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
             this.idPersona = ++Persona.contadorPersonas;
        }
        else{
            console.log('No se pueden crear mas personas');
        }
       

        //console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
    }

    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    
    nombreCompleto(){
        return this.idPersona+' '+this._nombre+' '+this._apellido;
    }
    // Sobreescribiendo el metodo de la clase padre (object)
    toString(){
        // Aca se aplica el polimorfismo: multiples formas en tiempo de ejecucion
        //El método que se ejecuta depende si es una ref del tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log('Saludos desde metodo static');
    }
    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
    }

}

class Empleado extends Persona{
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }

    // Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
    }


}

let persona1 = new Persona('Sil', 'Prado');
persona1.nombre = 'Silvina';
console.log(persona1);

let persona2 = new Persona('Dora', 'Martinez');
console.log(persona2.nombre);
//tarea
persona1.apellido = 'Prado Martinez';
console.log(persona1);

let empleado1 = new Empleado('Silvina', 'Prado', 'Sistemas');
console.log(empleado1.nombreCompleto());

// object.prototype.toString // esta es la manera de acceder a atrib y metodos dinamicamente
console.log(empleado1.toString());
console.log(persona1.toString());

// persona1.saludar(); // no se utiliza desde el objeto pero si desde la clase

Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

console.log(Persona.contadorObjetosPersona);

console.log(persona1.email);
console.log(empleado1.email);   
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);

let persona3 = new Persona('Felipe', 'Prado');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);

let persona4 = new Persona('Armando', 'Paredes');   
console.log(persona4.toString());   
let persona5 = new Persona('Esteban', 'Quito');
console.log(persona5.toString());