class Cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"
    
    def actualizar_email(self, nuevo_email):
        """Actualiza el email del cliente."""
        self.email = nuevo_email
        print(f"El email de {self.nombre} ha sido actualizado a {self.email}.")

    def mostrar_informacion(self):
        """Muestra toda la información del cliente."""
        return f"Nombre: {self.nombre}\nEmail: {self.email}\nTeléfono: {self.telefono}\nDirección: {self.direccion}"  



