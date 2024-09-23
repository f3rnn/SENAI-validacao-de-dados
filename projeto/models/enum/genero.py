from enum import Enum

class Genero:
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")

    def __init__(self, caracter: str, texto: str) -> None:
        self.caracter = caracter
        self.texto = texto