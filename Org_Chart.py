class Org_chart:
    class Persona:
        def __init__(self, puesto, nombre, titulo, contacto):
            self.puesto = puesto
            self.nombre = nombre
            self.titulo = titulo
            self.contacto = contacto
        
        def __str__(self):
            return f"{self.puesto}, {self.nombre}, {self.titulo}, {self.contacto}"

    def __init__(self, person: "Org_chart.Persona"):
        self.person = person
        self._children = []

    def insert(self, node: 'Org_chart'):
        self._children.append(node)

    def print_tree(self, level=0):
        ident = ' ' * (level * 4)
        print(f"{ident}{self.person.puesto}, {self.person.nombre}, {self.person.titulo}, {self.person.contacto}")

        for child in self._children:
            child.print_tree(level + 1)

    def buscar(self, clave):
        result = []
        if self.person.nombre == clave or self.person.puesto == clave or self.person.titulo == clave:
            result.append(self)

        for child in self._children:
            result += child.buscar(clave)

        return result

    def nivel_hijo(self, clave, level=0):
        if self.person.nombre == clave or self.person.puesto == clave or self.person.titulo == clave:
            return level

        for child in self._children:
            result = child.nivel_hijo(clave, level + 1)
            if result is not None:
                return result
        return None

    def buscar_por_nombre(self, nombre):
        if self.person.nombre == nombre:
            return self

        for child in self._children:
            resultado = child.buscar_por_nombre(nombre)
            if resultado:
                return resultado
        return None

    def add(self, nuevo):
        persona = self.buscar_por_nombre(nuevo)
        if persona:
            nueva_persona = Org_chart(
                Org_chart.Persona(
                    input("Puesto de la persona: "),
                    input("Nombre de la persona: "),
                    input("Título de la persona: "),
                    input("Contacto de la persona: ")
                )
            )
            persona.insert(nueva_persona)
            print("Listo, persona agregada.")
        else:
            print("Persona no encontrada.")

    def borrar(self, clave):
        i = 0
        while i < len(self._children):
            child = self._children[i]
            if child.person.nombre == clave:
                del self._children[i]
                print("listo")
                return True
            elif child.borrar(clave):
                return True
            else:
                i += 1
        return False


def orgchart_create():
    def crear_hijo():
        puesto = input("Puesto de la persona: ")
        nombre = input("Nombre de la persona: ")
        titulo = input("Título de la persona: ")
        contacto = input("Contacto de la persona: ")
        return Org_chart(Org_chart.Persona(puesto, nombre, titulo, contacto))

    def construir(persona, nivel):
        if nivel == 0:
            return

        try:
            numero_hijos = int(input(f"¿Cuántos hijos tiene {persona.person.puesto} {persona.person.nombre}?: "))
        except ValueError:
            print("Solo números")
            return

        for i in range(numero_hijos):
            print(f"Ingresar datos del hijo {i + 1} de {persona.person.puesto} {persona.person.nombre}")
            hijo = crear_hijo()
            persona.insert(hijo)
            construir(hijo, nivel - 1)

    print("Primero, ingrese los datos de la raíz o jefe principal.")
    root = crear_hijo()

    try:
        nivel_max = int(input("Ingresar cuántos niveles se necesitan: "))
    except ValueError:
        print("Solo números")
        return None

    construir(root, nivel_max)
    return root


# Uso del organigrama
arbol = orgchart_create()
print("El organigrama fue creado")
arbol.print_tree()

while True:
    print("¿Qué acción quiere realizar?")
    print("1.- Buscar")
    print("2.- Saber el nivel de un directivo")
    print("3.- Añadir un nuevo elemento")
    print("4.- Borrar elemento")
    print("5.- Ver el árbol")
    print("6.- Salir")
    try:
        eleccion = int(input("Elija un número del 1 al 6: "))
    except ValueError:
        print("Número no válido")
        continue

    if eleccion == 1:
        clave = input("¿Qué deseas buscar (nombre/puesto/título)? ")
        resultados = arbol.buscar(clave)
        if resultados:
            for encontrado in resultados:
                print(f"Encontrado: {encontrado.person}")
        else:
            print("No encontrado")

    elif eleccion == 2:
        buscar_nivel = input("Ingrese el nombre, puesto o título para buscar nivel: ")
        nivel = arbol.nivel_hijo(buscar_nivel)
        if nivel is not None:
            print(f"{buscar_nivel} está en el nivel {nivel}")
        else:
            print("No encontrado")

    elif eleccion == 3:
        donde = input("Ingrese el nombre, puesto o contacto bajo el cual estará el nuevo elemento: ")
        arbol.add(donde)

    elif eleccion == 4:
        a_borrar = input("Ingresa el nombre de la persona a borrar: ")
        arbol.borrar(a_borrar)

    elif eleccion == 5:
        arbol.print_tree()

    elif eleccion == 6:
        break

    else:
        print("Número no válido")
        
#Ejemplo
"""
arbol = Org_chart(Org_chart.Persona("Rector " , "Arturo F. " , "Doctorado ", "000000 " ))
child1 = (Org_chart("Director ","Ivan " ,"Ingeniero ", "111111" ))
child2 = (Org_chart("Director ", "Alfredo ","Ingeniero " , "222222"   ))
grandchild1 = (Org_chart("Maestro " , "Liliana" , "Licenciada " ,"333333" ))
grandchild2 =(Org_chart("Maestro" , "Octavio " , "Licenciado" , "444444"))
grandchild3 = (Org_chart("Maestro " , "Christian ","Lecenciado ", "555555" ))
arbol.insert(child1)
arbol.insert(child2)
child1.insert(grandchild1)
child2.insert(grandchild2)
child2.insert(grandchild3)
arbol.print_tree()"""