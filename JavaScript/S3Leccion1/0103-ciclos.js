// while
let contador = 0;
while(contador <3){
    console.log(contador);
    contador++;
}
console.log("fin del ciclo while")

// do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("fin del ciclo do while");

//for
for( let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log("fin del ciclo for");

//BREAK
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando)
        break;
    }
}
console.log('fin de for cuando encuentra el primer par')
//sin el break ejecuta hasta que encuentra todos los pares en 0-10

//CONTINUE
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; //va a la siguiente iteracion
    }
    console.log(contando)
}
console.log('termina el ciclo')

// etiquetas o labels
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue inicio; //va a la siguiente iteracion
    }
    console.log(contando)
}
console.log('termina el ciclo')