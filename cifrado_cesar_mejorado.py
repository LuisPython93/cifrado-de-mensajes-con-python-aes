import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# --- Funciones de seguridad ---

def derivar_clave(password: str, salt: bytes) -> bytes:
    """Genera una clave fuerte a partir de una contraseña usando PBKDF2"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def cifrar_texto(texto: str, password: str) -> bytes:
    """Cifra el texto usando AES y una clave derivada"""
    salt = os.urandom(16)
    clave = derivar_clave(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding manual
    texto_bytes = texto.encode()
    padding_length = 16 - (len(texto_bytes) % 16)
    texto_bytes += bytes([padding_length]) * padding_length

    cifrado = encryptor.update(texto_bytes) + encryptor.finalize()
    return base64.b64encode(salt + iv + cifrado)

def descifrar_texto(datos_cifrados: bytes, password: str) -> str:
    """Descifra los datos cifrados usando AES y la clave derivada"""
    datos = base64.b64decode(datos_cifrados)
    salt, iv, cifrado = datos[:16], datos[16:32], datos[32:]
    clave = derivar_clave(password, salt)
    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    texto_bytes = decryptor.update(cifrado) + decryptor.finalize()
    padding = texto_bytes[-1]
    return texto_bytes[:-padding].decode()

# --- Funciones de interfaz ---

def guardar_archivo():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Vacío", "No hay texto para guardar.")
        return
    password = simpledialog.askstring("Clave", "Ingrese una clave para cifrar:", show='*')
    if not password:
        return
    datos_cifrados = cifrar_texto(texto, password)
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Texto", "*.txt")])
    if archivo:
        with open(archivo, "wb") as f:
            f.write(datos_cifrados)
        messagebox.showinfo("Éxito", "Texto cifrado y guardado.")

def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Texto", "*.txt")])
    if not archivo:
        return
    password = simpledialog.askstring("Clave", "Ingrese la clave para descifrar:", show='*')
    if not password:
        return
    try:
        with open(archivo, "rb") as f:
            datos_cifrados = f.read()
        texto_descifrado = descifrar_texto(datos_cifrados, password)
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, texto_descifrado)
        messagebox.showinfo("Éxito", "Texto descifrado correctamente.")
    except Exception:
        messagebox.showerror("Error", "No se pudo descifrar. Clave incorrecta o archivo dañado.")

# --- Interfaz gráfica ---

root = tk.Tk()
root.title("Cifrado Seguro con AES")
root.geometry("500x400")

tk.Label(root, text="Texto para cifrar/descifrar:").pack()
entrada_texto = tk.Text(root, height=5, width=60)
entrada_texto.pack()

tk.Button(root, text="Guardar como archivo cifrado", command=guardar_archivo).pack(pady=5)
tk.Button(root, text="Cargar archivo cifrado", command=cargar_archivo).pack(pady=5)

tk.Label(root, text="Resultado:").pack()
salida_texto = tk.Text(root, height=5, width=60)
salida_texto.pack()

root.mainloop()
