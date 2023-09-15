from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False



@dataclass
class Conjunto:
    elementos: list[Elemento] = []
    nombre: str = ""
    contador: int = 0

    def __post_init__(self):
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nombre_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        return Conjunto(elementos=elementos_comunes, nombre=nombre_resultante)

    def __str__(self):
        nombres_elementos = [elem.nombre for elem in self.elementos]
        return f"Conjunto {self.nombre}: ({', '.join(nombres_elementos)})"
















