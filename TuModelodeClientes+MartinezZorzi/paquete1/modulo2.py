from paquete1.modulo1 import Cliente

def registrar_cliente():
    """Función para registrar un nuevo cliente."""
    #El print("\n" + "="*30 o "-"*30) lo utilizo principalmente para la estetica del codigo a la hora de ejecutarlo en consola!!!
    print("\n" + "="*30)
    print(" REGISTRO DE CLIENTE ".center(30, "="))
    print("="*30)
    nombre = input("Ingrese el nombre del cliente: ")
    contrasenia = input("Ingrese la contraseña del cliente: ")
    email = input("Ingrese el email del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")

    cliente = Cliente(nombre, email, telefono, direccion, contrasenia)
    print("\n" + "-"*30)
    print(f"Cliente registrado exitosamente:\n{cliente}")
    print("-"*30)
    return cliente


def mostrar_cliente(cliente):
    """Función para mostrar la información de un cliente."""
    print("\n" + "="*30)
    print(" INFORMACIÓN DEL CLIENTE ".center(30, "="))
    print("="*30)
    print(cliente.mostrar_informacion())
    print("="*30)


def actualizar_email_cliente(cliente):
    """Función para actualizar el email de un cliente."""
    print("\n" + "="*30)
    print(" ACTUALIZAR EMAIL ".center(30, "="))
    print("="*30)
    cambio = input("¿Desea cambiar el email del cliente? (Si/No): ")
    if cambio == "Si":
        nuevo_email = input(f"Ingrese el nuevo email para {cliente.nombre}: ")
        cliente.actualizar_email(nuevo_email)
        print("="*30)
    else:
        print("\n" + "-"*30)
        print("Actualizacion de Mail cancelada.".center(30))
        print("-"*30)


def login_cliente(cliente):
    """Función para realizar el login de un cliente."""
    print("\n" + "="*30)
    print(" LOGIN DE CLIENTE ".center(30, "="))
    print("="*30)
    while True:
        nombre = input("Ingrese su nombre: ")
        contrasenia = input("Ingrese su email: ")
        

        if contrasenia == cliente.contrasenia and nombre == cliente.nombre:
            print("\n" + "-"*30)
            print("¡Login exitoso!".center(30))
            print("-"*30)
            break
        else:
            print("\n" + "-"*30)
            print("Error: Email o nombre incorrectos. Intente nuevamente.".center(30))
            print("-"*30)

def comprar():
    print("\n" + "="*30)
    print(" COMPRAR ".center(30, "="))
    print("="*30)
    print("¡Bienvenido a la tienda!")
    print("¿Qué producto desea comprar?")
    producto = input("Ingrese el nombre del producto: ")
    print(f"¡{producto} ha sido añadido al carrito!")
    print("¡Gracias por su compra!")

