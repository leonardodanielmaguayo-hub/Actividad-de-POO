Calculadora
Aplicación de escritorio desarrollada en Java que permite sumar y multiplicar números enteros. Cuenta con una interfaz gráfica construida con Swing y AWT, y utiliza el patrón MVC (Modelo-Vista-Controlador) para separar los cálculos, la interfaz y la gestión de las acciones.

Funcionalidades
Sumar un número al total actual.
Multiplicar el total actual por un número.
Mostrar el resultado en la ventana.
Restablecer el total a 1 y limpiar el campo de entrada.
Mostrar un mensaje si el valor ingresado no es un número entero válido.
Manejar enteros grandes mediante BigInteger.

REQUISITOS
REQUISITOS FUNCIONALES
1. El sistema debe permitir poner valores en un campo de texto
2. El sistema debe poder mostrar el resultado de la operacion en un campo de texto
3. El sistema debe mostrar un boton clean para restablecer el valor total al inicio.
4. El sistema debe poder procesar multiplicaciones con numeros de gran tamaño.

REQUISITOS NO FUNCIONALES
1. Lenguaje de Programación: La aplicación debe estar desarrollada íntegramente en el lenguaje de programación Java.
2. Interfaz Gráfica: La interfaz de usuario debe construirse utilizando los componentes de las bibliotecas Java Swing y AWT

3. Cómo ejecutar
Desde la carpeta raíz del proyecto, compila los archivos:
javac -d out .\Calculadora\CalcController.java .\Calculadora\CalcModel.java .\Calculadora\vista.java .\Calculadora\principal.java
Luego, inicia la aplicación:
java -cp out Calculadora.principal

Estructura de la carpeta
principal.java: inicia la aplicación y crea el modelo, la vista y el controlador.
CalcModel.java: conserva el total y realiza las operaciones.
vista.java: construye la interfaz gráfica y muestra los resultados.
CalcController.java: coordina las acciones de la interfaz con el modelo.

Uso
Escribe un número en el campo Input y pulsa Sumar o Multiply para actualizar el total. Pulsa Clear para restablecerlo a 1 y borrar la entrada.
