//if
var edad = 18;

if (edad >= 18) {
    console.log("Eres mayor de edad"); // Verifica si la edad es mayor o igual a 18
}
else {
    console.log("Eres menor de edad"); // Verifica si la edad es menor a 18
}

//switch
var dia = 3;
switch (dia) {
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miércoles");
        break;
    case 4:
        console.log("Jueves");
        break;
    case 5:
        console.log("Viernes");
        break;
    case 6:
        console.log("Sábado");
        break;
    case 7:
        console.log("Domingo");
        break;
    default:
        console.log("Día inválido");
}

//while
var contador = 0;
while (contador < 5) {
    console.log("Contador:", contador);
    contador++;
}

//for
for (var i = 0; i < 5; i++) {
    console.log("Número:", i); // Imprime números del 0 al 4
}

//do while
var j = 0;
do {
    console.log("Número de Do While:", j);
    j++;
} while (j < 5); // Imprime números del 0 al 4, asegurando que al menos una vez se ejecute el bloque de código
// Esta estructura garantiza que el bloque de código se ejecute al menos una vez, incluso si
// la condición es falsa desde el principio.    