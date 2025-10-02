class PontoDeColeta:
    def __init__(self, id_ponto, localizacao, capacidade_kg, ocupacao_atual_kg=0):
        self.id_ponto = id_ponto
        self.localizacao = localizacao
        self.capacidade_kg = capacidade_kg
        self.ocupacao_atual_kg = ocupacao_atual_kg

    def __str__(self):
        percentual = (self.ocupacao_atual_kg / self.capacidade_kg) * 100 if self.capacidade_kg > 0 else 0
        return (f"ID: {self.id_ponto} | Local: {self.localizacao} | "
                f"Capacidade: {self.capacidade_kg}kg | "
                f"Ocupação: {self.ocupacao_atual_kg}kg ({percentual:.2f}%)")

class EquipeLimpeza:
    def __init__(self, id_equipe, nome, membros):
        self.id_equipe = id_equipe
        self.nome = nome
        self.membros = membros

    def __str__(self):
        return f"ID: {self.id_equipe} | Equipe: {self.nome} | Membros: {self.membros}"