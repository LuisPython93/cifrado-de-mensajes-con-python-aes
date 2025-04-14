# Proyecto: Cifrado de Archivos con AES y Python
Proyecto de cifrado y descifrado con interfaz gráfica usando Python y AES

## Descripción
Este es un proyecto de cifrado y descifrado de textos mediante AES en modo CBC, utilizando claves derivadas de contraseñas con PBKDF2HMAC. Incluye una interfaz gráfica construida con tkinter para facilitar su uso.

Ideal para aprender criptografía aplicada en Python, proteger archivos sensibles y explorar el uso de interfaces GUI.

📁 Características

- Cifrado de texto mediante AES (clave de 256 bits).

- Derivación de clave a partir de contraseña del usuario (PBKDF2).

- Cifrado seguro con salt e IV aleatorios.

- Interfaz gráfica amigable con tkinter.

- Guardado y carga de archivos cifrados.

- Clave maestra de acceso al programa.

🚀 Requisitos

- Python 3.8+

- Librería cryptography

- Puedes instalar la dependencia con:
```bash
pip install cryptography
```
📑 Uso del programa
1. Clona este repositorio:

```bash
git clone https://github.com/LuisPython93/cifrado-de-mensajes-con-python-aes.git
cd cifrado-de-mensajes-con-python-aes
```
2. Ejecuta el script principal:

```bash
python cifrado_cesar_mejorado.py
```
3. ingresa la clave maestra al iniciar (configurable en código).
4. Puedes:
- Escribir texto y guardarlo cifrado.
- Cargar un archivo cifrado e ingresar la clave para descifrarlo.

🔐 Seguridad

- Utiliza AES con bloques de 128 bits.
- La clave no se guarda nunca directamente, sino que se deriva de la contraseña del usuario.
- Usa salt e IV aleatorios en cada cifrado.

😎 Autor
Luis - @LuisPython93

💚 Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
