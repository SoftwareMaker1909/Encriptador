from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def guardar_clave(clave, nombre_archivo="clave.txt"):
    with open(nombre_archivo, "wb") as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave(nombre_archivo="clave.key"):
    return open(nombre_archivo, "rb").read()

def encriptar_contenido(contenido, clave):
    cifrador = Fernet(clave)
    return cifrador.encrypt(contenido.encode())

def desencriptar_contenido(contenido_encriptado, clave):
    cifrador = Fernet(clave)
    return cifrador.decrypt(contenido_encriptado).decode()

def main():
    # Generar o cargar la clave
    try:
        clave = cargar_clave()
    except FileNotFoundError:
        clave = generar_clave()
        guardar_clave(clave)

    # Abrir el archivo de texto
    archivo_path = "archivo.txt"
    with open(archivo_path, "r") as archivo:
        contenido = archivo.read()

    # Encriptar el contenido
    contenido_encriptado = encriptar_contenido(contenido, clave)

    # Pedir la clave para desencriptar y mostrar el contenido
    while True:
        intento_clave = input("Introduce la clave para ver el contenido: ")
        try:
            if desencriptar_contenido(contenido_encriptado, intento_clave) == contenido:
                print("Contenido desencriptado:")
                print(contenido)
                break
            else:
                print("Clave incorrecta. Inténtalo de nuevo.")
        except Exception as e:
            print("Error al desencriptar: {}".format(str(e)))
            break

if __name__ == "__main__":
    main()
