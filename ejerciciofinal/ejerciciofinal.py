#Creamos una clase Cliente con los atributos nombre, email y telefono.
class Cliente:

    def __init__(self, nombre, email, telefono):
        self.nombre = nombre #Atributo nombre de la clase Cliente
        self.email = email #Atributo email de la clase Cliente
        self.telefono = telefono #Atributo telefono de la clase Cliente

#Implantamos el método __str__ para mostrar la información del cliente de una manera amigable, self hace referencia a la clase Cliente.
    def __str__(self):
        return f'Cliente (nombre:{self.nombre}, email:{self.email}, telefono:{self.telefono})'
    

#Creamos una clase SistemaClientes que gestione una colección de clientes. 
#Esta clase debe tener un atributo clientes que sea una lista de objetos cliente.
#Implementamos los métodos agregar_cliente, eliminar_cliente, buscar_cliente y listar_clientes en la clase SistemaClientes.
class SistemaClientes:
    def __init__(self):
        self.clientes = [] #Inicializamos la lista (de momento vacía) de clientes.
    def agregar_cliente (self, cliente): 
        self.clientes.append(cliente) #Agregar un nuevo cliente a la lista.
        print(f"El cliente {cliente.nombre} fue agregado satisfactoriamente")
    def eliminar_cliente (self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                self.clientes.remove(cliente) #Elimina el cliente encontrado.
                print(f"El cliente {nombre} fue eliminado satisfactoriamente")
                return
        print(f"No se han encontrado clientes con el nombre {nombre}.") #Nos muestra un mensaje indicando que no se ha encontrado al cliente.   
    def buscar_cliente (self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return print (cliente) #Nos devuelve el nombre del cliente encontrado.
        return print (None) #Nos devuelve un mensaje "None" si no encuentra al cliente.
    def listar_clientes (self):
        if not self.clientes:
            print("No hay clientes registrados") #Nos muestra un mensaje si no existen clientes en la lista.
        else:
            for cliente in self.clientes:
                print(cliente) #Nos muestra la información de todos los clientes de la lista.

#Se crea una instancia del sistema de clientes.
sistema = SistemaClientes()

#A partir de aquí se muestran ejemplos para comprobar que el código funciona.
#Declaración de instancias de clase. Creamos algunos clientes.
cliente1 = Cliente("Antonio", "antoniofernandez5764@gmail.com", 676735667)
cliente2 = Cliente("Alejandra", "alejandragutierrez8472@gmail.com", 674366473)
cliente3 = Cliente("Roberto", "robertogomez6472@gmail.com", 674378902)

#Agregamos clientes al sistema
sistema.agregar_cliente(cliente1)
sistema.agregar_cliente(cliente2)
sistema.agregar_cliente(cliente3)

#Listar clientes
sistema.listar_clientes()

#Buscar un cliente
cliente_buscado = sistema.buscar_cliente("Antonio")
cliente_buscado = sistema.buscar_cliente("Ana")

#Eliminar un cliente
sistema.eliminar_cliente("Antonio")
sistema.eliminar_cliente("Ana")

#Listar clientes nuevamente
sistema.listar_clientes()

#1º nos muestra que los tres clientes han sido agregados satisfactoriamente a la lista. 
#2º le pedimos que nos muestre la lista de clientes y nos aparece una lista con los datos de los tres clientes.
#3º le pedimos que nos busque al cliente Antonio, el cual nos muestra.
#4º le pedimos que nos busque al cliente Ana, y nos devuelve "None" ya que no existe.
#5º eliminamos al cliente Antonio y nos muestra en un mensaje que se ha eliminado el cliente.
#6º en cambio, si le pedimos eliminar al cliente Ana, nos dice que no ha encontrado clientes con ese nombre.
#7º por último, le pedimos que nos vuelva a mostrar la lista de clientes, en la que solo aparecen Alejandra y Roberto.