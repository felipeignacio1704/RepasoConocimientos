//try catch para controlar errores en la consola
try {
    throw new Error("This is a test error");
} catch (error) {
    console.log(error.message);
    // Aquí puedes agregar más lógica para manejar el error, como enviar un reporte a un servidor
}