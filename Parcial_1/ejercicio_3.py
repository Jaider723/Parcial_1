import os

class Producto:
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Inventario:
    def __init__(self,nombre):
        self.nombre = nombre
            
    def ingresar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        producto = Producto(nombre, cantidad)
        with open(self.nombre, 'a') as archivo:
            archivo.write(f"{producto.nombre},{producto.cantidad}\n")
        print("Producto ingresado.")

    def buscar_producto(self):
        nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")
        band = False
        with open(self.nombre, 'r') as archivo:
            for linea in archivo:
                nombre, cantidad = linea.strip().split(',')
                if nombre == nombre_buscar:
                    print(f"Producto: {nombre}, Cantidad: {cantidad}")
                    band = True
        if not band:
            print("Producto no encontrado.")

    def borrar_producto(self):
        nombre_buscar = input("Ingrese el nombre del producto que desea borrar: ")
        productos_actualizados = []
        with open(self.nombre, 'r') as archivo:
            for linea in archivo:
                nombre, _= linea.strip().split(',')
                if nombre != nombre_buscar:
                    productos_actualizados.append(linea)
    
        with open(self.nombre, 'w') as archivo:
            archivo.writelines(productos_actualizados)
        print("producto eliminado.")
        
    def ordenar_productos(self):
        with open(self.nombre, 'r') as archivo:
            productos = archivo.readlines()
        productos_ordenados = sorted(productos)   
        with open(self.nombre, 'w') as archivo:
            archivo.writelines(productos_ordenados)
        print("Productos ordenados.")

def main():
    archivo = Inventario("inventario.txt")
    while True:
        print("\n--- MENU ---")
        print("1. Ingresar producto")
        print("2. Buscar producto")
        print("3. Borrar producto")
        print("4. Ordenar productos")
        print("0. Salir")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            archivo.ingresar_producto()
        elif opcion == '2':
            archivo.buscar_producto()
        elif opcion == '3':
            archivo.borrar_producto()
        elif opcion == '4':
            archivo.ordenar_productos()
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
