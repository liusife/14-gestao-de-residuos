from classes import PontoDeColeta, EquipeLimpeza

pontos_coleta = {}
equipes = {}



ponto1 = PontoDeColeta(id_ponto='PC01', 
                       localizacao='Marco Zero, Recife Antigo', 
                       capacidade_kg=500)

ponto2 = PontoDeColeta(id_ponto='PC02', 
                       localizacao='Rua do Bom Jesus, Recife Antigo', 
                       capacidade_kg=350, 
                       ocupacao_atual_kg=100)

pontos_coleta[ponto1.id_ponto] = ponto1
pontos_coleta[ponto2.id_ponto] = ponto2
