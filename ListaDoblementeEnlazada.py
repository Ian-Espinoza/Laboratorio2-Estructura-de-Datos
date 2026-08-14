class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None   # nos permite movernos hacia la derecha
        self.anterior = None    # nos permite movernos hacia la izquierda


class ListaDoblemente:
    def __init__(self):
        self.cabeza = None   # inicio de la lista
        self.cola = None     # fin de la lista
        self.tamano = 0      # cantidad de elementos que hay en la lista

    def listaVacia(self):
        return self.cabeza is None

    def insertarAlInicio(self, dato):
        nuevoNodo = Nodo(dato)
        if self.listaVacia():
            # lista vacía: el nuevo nodo es cabeza y cola a la vez
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevoNodo
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

        # caso en que solo existe un nodo en la lista
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
        if posicion < 0 or posicion >= self.tamano:
            print("Posición fuera de rango.")
            return None
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

    def eliminarEnPosicion(self, posicion):
        # se utiliza la función que ya elimina en cualquier posición
        return self.eliminarAlMedio(posicion)

    def display(self):
        # se corrigieron los nombres para usar cabeza, dato y siguiente
        actual = self.cabeza
        textoLista = ""
        while actual is not None:
            textoLista += str(actual.dato) + " <-> "
            actual = actual.siguiente
        textoLista += "None"
        print(textoLista)
        return textoLista

    # ================================================================
    # FUNCIONES NUEVAS SOLICITADAS EN EL LABORATORIO
    # ================================================================

    def buscarNombre(self, nombre):
        # guarda todas las posiciones en las que aparece el nombre
        posiciones = []
        actual = self.cabeza
        posicion = 0

        while actual is not None:
            if str(actual.dato).lower() == nombre.lower():
                posiciones.append(posicion)
            actual = actual.siguiente
            posicion += 1

        return posiciones

    def sustituir(self, posicion, palabra):
        if posicion < 0 or posicion >= self.tamano:
            print("Posición fuera de rango.")
            return None

        actual = self.cabeza
        contador = 0

        while contador < posicion:
            actual = actual.siguiente
            contador += 1

        palabraAnterior = actual.dato
        actual.dato = palabra
        return palabraAnterior

    def ordenar(self):
        # ordenamiento alfabético mediante el método de burbuja
        if self.listaVacia():
            return

        for i in range(self.tamano - 1):
            actual = self.cabeza

            while actual.siguiente is not None:
                if str(actual.dato).lower() > str(actual.siguiente.dato).lower():
                    temporal = actual.dato
                    actual.dato = actual.siguiente.dato
                    actual.siguiente.dato = temporal
                actual = actual.siguiente


if __name__ == "__main__":
    # Crear la lista doblemente enlazada
    lista = ListaDoblemente()

    try:
        with open("datos.txt", "r", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                linea = linea.strip()

                # Evitar líneas vacías
                if linea != "":
                    # datos.txt posee nombres, por eso no se convierte a int
                    valor = linea

                    # Se mantiene la inserción al inicio del código original
                    lista.insertarAlInicio(valor)

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    # Se solicitan los nombres que deben aparecer en Reporte.txt
    estudiante1 = input("Digite el nombre del primer estudiante: ")
    estudiante2 = input("Digite el nombre del segundo estudiante: ")

    # Buscar un nombre y mostrar su posición y cantidad de apariciones
    palabraBuscar = input("\nDigite una palabra para buscar: ")
    posiciones = lista.buscarNombre(palabraBuscar)

    if len(posiciones) > 0:
        print("La palabra está en la posición:", posiciones[0])
    else:
        print("La palabra no se encuentra en la lista.")
    print("La palabra aparece", len(posiciones), "veces")

    # Sustituir una palabra por medio de su posición
    try:
        posicionReemplazar = int(input("\nDigite posición a reemplazar: "))
    except ValueError:
        print("Error: debe digitar una posición numérica.")
        exit()

    nuevaPalabra = input("Digite nueva palabra: ")
    palabraAnterior = lista.sustituir(posicionReemplazar, nuevaPalabra)

    if palabraAnterior is None:
        exit()

    print("Se reemplazó:", palabraAnterior, "por", nuevaPalabra)

    # Guardar e imprimir la lista antes de ordenar
    print("\nLista antes de ordenar:")
    listaAntesDeOrdenar = lista.display()

    # Ordenar e imprimir la lista
    lista.ordenar()
    print("\nLista después de ordenar:")
    listaOrdenada = lista.display()

    # Crear el archivo solicitado por el laboratorio
    with open("Reporte.txt", "w", encoding="utf-8") as archivo:
        archivo.write("========================================\n")
        archivo.write("          REPORTE DE PALABRAS\n")
        archivo.write("========================================\n\n")
        archivo.write("Estudiantes: " + estudiante1 + " y " + estudiante2 + "\n\n")
        archivo.write("Cantidad de palabras: " + str(lista.cantidadElementos()) + "\n\n")
        archivo.write("Palabra buscada: " + palabraBuscar + "\n")

        if len(posiciones) > 0:
            archivo.write("La palabra está en la posición: " + str(posiciones[0]) + "\n")
        else:
            archivo.write("La palabra no se encuentra en la lista.\n")

        archivo.write("La palabra aparece " + str(len(posiciones)) + " veces\n\n")
        archivo.write("Posición reemplazada: " + str(posicionReemplazar) + "\n")
        archivo.write("Se reemplazó: " + str(palabraAnterior) + " por " + nuevaPalabra + "\n\n")
        archivo.write("Lista antes de ordenar:\n")
        archivo.write(listaAntesDeOrdenar + "\n\n")
        archivo.write("Lista después de ordenar:\n")
        archivo.write(listaOrdenada + "\n")

    print("\nEl archivo Reporte.txt se creó correctamente.")
