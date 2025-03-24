from paquete1.modulo1 import Cliente
from paquete1.modulo2 import *

print("Bienvenido al sistema de gestión de clientes.")
cliente = registrar_cliente()
print("¡Bienvenido al sistema!")
login_cliente(cliente)
mostrar_cliente(cliente)
actualizar_email_cliente(cliente)
comprar()
mostrar_cliente(cliente)
