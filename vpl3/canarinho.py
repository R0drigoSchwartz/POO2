from ave import Ave

class Canarinho(Ave):
    def __init__(tamanhoPasso: int, alturaVoo: int):
        super().__init__(tamanhoPasso, alturaVoo)

    def mover(self):
        return f"ANIMAL: DESLOCOU {self.tamanhoPasso} VOANDO"

    def produzirSom(self):
        return f"AVE: PRODUZ SOM: "

    def cantar(self):
        return self.produzirSom()+"PIU"
