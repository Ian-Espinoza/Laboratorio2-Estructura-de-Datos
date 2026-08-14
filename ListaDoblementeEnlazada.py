class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None   # nos permite movernos hacia la derecha
        self.anterior = None    # nos permite movernos hacia la izquierda

class ListaDoblemente:
    def __init__(self):
        self.cabeza = None   # inicio de la lista
        self.cola = None      # fin de la lista
        self.tamano = 0        # objetivo es que cada vez que insertemos a la lista nos determine y sepa cuántos elementos hay

    def listaVacia(self):
        return self.cabeza is None   # determinar si la cabeza es NULL

    def insertarAlInicio(self, dato):
        nuevoNodo = Nodo(dato)
        if self.listaVacia():
            # lista vacía: el nuevo nodo es cabeza y cola a la vez
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevoNodo   # la antigua cabeza debe apuntar hacia atrás al nuevo nodo
            self.cabeza = nuevoNodo
        self.tamano += 1
    
    def insertarAlMedio(self, dato, posicion):
        if posicion < 0 or posicion > self.tamano:
            print("Posición inválida")
            return
        if posicion == 0:
            self.insertarAlInicio(dato)
            return
        if posicion == self.tamano:
            self.insertarAlFinal(dato)
            return

        nuevoNodo = Nodo(dato)
        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente

        # insertamos 'nuevoNodo' antes de 'actual'
        anterior = actual.anterior
        anterior.siguiente = nuevoNodo
        nuevoNodo.anterior = anterior
        nuevoNodo.siguiente = actual
        actual.anterior = nuevoNodo
        self.tamano += 1

    def insertarAlMedio(self, dato, posicion):
        if posicion < 0 or posicion >= self.tamano:
            print("Posición inválida")
            return
        if posicion == 0:
            self.insertarAlInicio(dato)
            return
        if posicion == self.tamano:
            self.insertarAlFinal(dato)
            return

        nuevoNodo = Nodo(dato)
        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente

        # insertamos 'nuevoNodo' antes de 'actual'
        anterior = actual.anterior
        anterior.siguiente = nuevoNodo
        nuevoNodo.anterior = anterior
        nuevoNodo.siguiente = actual
        actual.anterior = nuevoNodo
        self.tamano += 1

    def insertarAlFinal(self, dato):
        nuevoNodo = Nodo(dato)
        if self.listaVacia():
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            # gracias a self.cola no hay que recorrer la lista: O(1)
            nuevoNodo.anterior = self.cola
            self.cola.siguiente = nuevoNodo
            self.cola = nuevoNodo
        self.tamano += 1

    def eliminarAlInicio(self):
        if self.listaVacia():
            print("La lista está vacía.")
            return None
        valorEliminado = self.cabeza.dato
        # caso solo existe un nodo en la lista
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self.tamano -= 1
        return valorEliminado
    
    def eliminarAlMedio(self, posicion):
        if self.listaVacia():
            print("La lista está vacía.")
            return None
        if posicion < 0 or posicion >= self.tamano - 1:
            return self.eliminarAlInicio()
        if posicion == 0:
            return self.eliminarAlInicio()
        if posicion == self.tamano - 1:
            return self.eliminarAlFinal()

        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente

        anterior = actual.anterior
        siguiente = actual.siguiente

        anterior.siguiente = siguiente
        siguiente.anterior = anterior
        self.tamano -= 1
        return actual.dato

    def eliminarAlFinal(self):
        if self.listaVacia():
            print("La lista está vacía.")
            return None
        valorEliminado = self.cola.dato
        if self.cabeza != self.cola:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.tamano -= 1
        else:
            self.cabeza = None
            self.cola = None  
            self.tamano -= 1
        return valorEliminado

    def buscarElemento(self, dato):
        if self.listaVacia():
            print("La lista está vacía.")
            return -1
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def imprimirAdelante(self):
        # recorrido normal: de cabeza a cola
        if self.listaVacia():
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimirAtras(self):
        # recorrido inverso: de cola a cabeza (gracias a 'anterior')
        if self.listaVacia():
            print("La lista está vacía.")
            return
        actual = self.cola
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.anterior
        print("None")

    def cantidadElementos(self):
        return self.tamano

    def display(self):
        actual=self.head
        while actual is not None:
            print(actual.data,end="->")
            actual=actual.next
        print("None")

    def eliminarEnPosicion(self, posicion):
        if self.head is None:
            print("La lista está vacía.")
            return
        if posicion == 0:
            self.head = self.head.next
            return
        actual = self.head
        contador = 0
        while actual.next is not None and contador < posicion - 1:
            actual = actual.next
            contador += 1
        if actual.next is None:
            print("Posición fuera de rango.")
            return
        actual.next = actual.next.next

if __name__ == "__main__":
# Crear la lista doblemente enlazada
    lista = ListaDoblemente()
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                # Evitar líneas vacías
                if linea != "":
                    valor = int(linea)
                    # Insertar el valor en la lista
                    lista.insertarAlInicio(valor)
                    lista.imprimirAdelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    except ValueError:
        print("Error: el archivo contiene un dato que no es entero.")
        exit()

