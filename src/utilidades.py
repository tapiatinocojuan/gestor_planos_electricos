from collections import defaultdict

TIPOS = {
    1: "Centro de carga",
    2: "Placa de accesorios",
    3: "Contacto sencillo",
    4: "Contacto doble",
    5: "Apagador 2 vias",
    6: "Apagador 3 vias",
    7: "Apagador 4 vias",
    8: "Lampara de techo",
    9: "Lampara de pared",
    10: "Lampara de piso",
    "Centro de carga": 1,
    "Placa de accesorios" :2,
    "Contacto sencillo": 3,
    "Contacto doble": 4,
    "Apagador 2 vias": 5,
    "Apagador 3 vias": 6,
    "Apagador 4 vias": 7,
    "Lampara de techo": 8,
    "Lampara de pared": 9,
    "Lampara de piso": 10
}

ALTURA_STD = defaultdict(lambda: 1.10)
ALTURA_STD[1] = 1.50
ALTURA_STD[10] = 0
ALTURA_STD[9] = 2
ALTURA_STD[8] = 2.8

POTENCIA_STD = defaultdict(lambda: 180)
POTENCIA_STD[1] = 6000
POTENCIA_STD[2] = 0
POTENCIA_STD[3] = 90
POTENCIA_STD[4] = 180
POTENCIA_STD[5] = 0
POTENCIA_STD[6] = 0
POTENCIA_STD[7] = 0
POTENCIA_STD[8] = 30
POTENCIA_STD[9] = 30
POTENCIA_STD[10] = 30

FACTOR_MARGEN_X_CURVAS = 1.2

class Accesorio():

    def __init__(self, x, y, z, tipo, potencia, tag=None, espacio="Generico"):
        self.x = x
        self.y = y
        self.z = z
        self.tipo = tipo
        self.potencia = potencia
        self.tag = tag
        self.espacio = espacio
        self.__hijos__ = []
        self.__selected__ = False
        self.__padre__ = None
        self.circuito = ""
        self.cc = None

    def calc_pot(self):
        self.potencia = 0
        for hijo in self.__hijos__:
            self.potencia += hijo.potencia

    def append_hijo(self, hijo):
        self.__hijos__.append(hijo)
    
    def eliminar_hijo(self, hijo):
        for i, obj in enumerate(self.__hijos__):
            if hijo == obj:
                break
        self.__hijos__.pop(i)
    
    def actualizar_coordenadas_hijos(self):
        for hijo in self.__hijos__:
            hijo.x = self.x
            hijo.y = self.y
            hijo.z = self.z
    
    def set_circuito(self, circuito):
        self.circuito = circuito
    
    def set_cc(self, centro_carga):
        self.cc = centro_carga

    def __str__(self):
        return f"{self.tipo}-{self.potencia}W"
    
class Rama():

    def __init__(self, accesorio1, accesorio2, color="#0000FF"):
        self.obj1 = accesorio1
        self.obj2 = accesorio2
        self.dist = None
        self.punto_centro = None
        self.calcular_dist_obj()
        self.calcular_punto_centro()
        self.color = color
        self.__selected__ = False

    def calcular_dist_obj(self):
        """Calcula la distancia entre dos objetos"""
        if self.obj1.tipo == "Placa de accesorios" and self.obj1.tipo==self.obj2.tipo:
            delta_z = abs(self.obj1.z + self.obj2.z)
        else:
            delta_z = abs(self.obj1.z - self.obj2.z)
        dist = self.calc_dist((self.obj1.x, self.obj1.y), (self.obj2.x, self.obj2.y))
        self.dist = (delta_z + dist) * FACTOR_MARGEN_X_CURVAS

    def calcular_punto_centro(self):
        self.punto_centro = (
            (self.obj1.x + self.obj2.x)*0.5,
            (self.obj1.y + self.obj2.y)*0.5
        )
    
    def calc_dist(self, p1, p2):
        "Calcula la distancia entre 2 puntos"
        return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5

