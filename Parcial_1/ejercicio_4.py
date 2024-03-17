def get_numero():
    while True:
        numero = input("Ingrese un número de 4 cifras: ")
        if len(numero) != 4 or not numero.isdigit():
            print("El número ingresado no tiene 4 cifras.")
        else:
            return int(numero)
  
def descomponer_numero(numero):
    digito_1 = numero // 1000
    digito_2 = (numero // 100) % 10
    digito_3 = (numero // 10) % 10
    digito_4 = numero % 10
    if digito_1 % digito_4 == 0:
        print(f"{digito_1} es múltiplo de {digito_4}")
    else:
        print(f"{digito_1} no es múltiplo de {digito_4}")
    print(f"{digito_2} + {digito_3} = {digito_2 + digito_3}")
    
def main():
    numero = get_numero()
    descomponer_numero(numero)
    
if __name__ == "__main__":
    main()