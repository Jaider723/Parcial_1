alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
            'U', 'V', 'W', 'X', 'Y', 'Z']

class Cesar:
    def __init__(self, k, mensaje):
        self.key = k
        self.mensaje = mensaje.upper()  
        
    def cifrar(self):
        mensaje_cifrado = []
        for caracter in self.mensaje:
            if caracter.isspace():
                mensaje_cifrado.append(caracter)
            else:
                indice = (alfabeto.index(caracter) - self.key) % 26
                mensaje_cifrado.append(alfabeto[indice])
        guardar_mensaje("".join(mensaje_cifrado))
        return "".join(mensaje_cifrado)
                
    def descifrar(self):
        mensaje_descifrado = []
        for caracter in self.mensaje:
            if caracter.isspace():
                mensaje_descifrado.append(caracter)
            else:
                indice = (alfabeto.index(caracter) + self.key) % 26
                mensaje_descifrado.append(alfabeto[indice])
        guardar_mensaje("".join(mensaje_descifrado))
        return "".join(mensaje_descifrado)           
        
def get_mensaje():
    mensaje = input("Ingrese el mensaje: ")  
    k = int(input("Ingrese la llave (desplazamiento): "))
    guardar_mensaje(mensaje)
    return mensaje, k

def guardar_mensaje(mensaje):
    with open("mensajes.txt", "a") as archivo:
        archivo.write(f"{mensaje}\n")
    
def main():
    while True:
        print("\n---MENU---")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("0. Salir")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == '1':
            mensaje, k = get_mensaje()
            cesar = Cesar(k, mensaje)
            print("Mensaje cifrado:", cesar.cifrar())
        elif opcion == '2':
            mensaje, k = get_mensaje()
            cesar = Cesar(k, mensaje)
            print("Mensaje descifrado:", cesar.descifrar())
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
