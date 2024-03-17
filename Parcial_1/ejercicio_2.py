import os

class Usuario:
    def __init__(self,nombre,edad,residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

class Gestor:
    def __init__(self,nombre):
        self.nombre = nombre
            
    def crear_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        edad = input("Ingrese la edad del usuario: ")
        residencia = input("Ingrese el lugar de residencia: ")
        usuario = Usuario(nombre, edad, residencia)
        with open(self.nombre, 'a') as archivo:
            archivo.write(f"{usuario.nombre},{usuario.edad},{usuario.residencia}\n")
        print("Usuario creado.")

    def consultar_usuarios(self):
        with open(self.nombre, 'r') as archivo:
            for linea in archivo:
                nombre, edad, residencia = linea.strip().split(',')
                print(f"Nombre: {nombre}, Edad: {edad}, Residencia: {residencia}")

    def editar_usuario(self):
        nombre_buscar = input("Ingrese el nombre del usuario que desea editar: ")
        nueva_edad = input("Ingrese la nueva edad: ")
        nuva_residencia = input("Ingrese la nueva residencia: ")
        usuarios_actualizados = []
        with open(self.nombre, 'r') as archivo:
            for linea in archivo:
                nombre, edad, residencia = linea.strip().split(',')
                if nombre == nombre_buscar:
                    edad = nueva_edad
                    residencia = nuva_residencia
                usuarios_actualizados.append(f"{nombre},{edad},{residencia}\n")
    
        with open(self.nombre, 'w') as archivo:
            archivo.writelines(usuarios_actualizados)
        print("Usuario editado.")

    def borrar_usuario(self):
        nombre_buscar = input("Ingrese el nombre del usuario que desea borrar: ")
        usuarios_actualizados = []
        with open(self.nombre, 'r') as archivo:
            for linea in archivo:
                nombre, _, _ = linea.strip().split(',')
                if nombre != nombre_buscar:
                    usuarios_actualizados.append(linea)
    
        with open(self.nombre, 'w') as archivo:
            archivo.writelines(usuarios_actualizados)
        print("Usuario eliminado.")

def main():
    archivo = Gestor("usuarios.txt")
    while True:
        print("\n--- MENU ---")
        print("1. Crear usuario")
        print("2. Consultar usuarios inscritos")
        print("3. Editar usuario")
        print("4. Borrar usuario")
        print("0. Salir")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            archivo.crear_usuario()
        elif opcion == '2':
            archivo.consultar_usuarios()
        elif opcion == '3':
            archivo.editar_usuario()
        elif opcion == '4':
            archivo.borrar_usuario()
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
