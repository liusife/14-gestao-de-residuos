import os
from classes import PontoDeColeta, EquipeLimpeza
from dados import pontos_coleta, equipes


def limpar_tela():
    """Limpa o terminal para uma melhor experiência de usuário."""
    os.system('cls' if os.name == 'nt' else 'clear')


# --- CRUD Pontos de Coleta ---

def criar_ponto():
    limpar_tela()
    print("--- Adicionar Novo Ponto de Coleta ---\n")
    id_ponto = input("Digite o ID do novo ponto (ex: 'PC03'): ").upper()
    if id_ponto in pontos_coleta:
        print("\nErro: Já existe um ponto de coleta com este ID.")
        return
    
    localizacao = input("Digite a localização: ")
    try:
        capacidade = int(input("Digite a capacidade em kg: "))
    except ValueError:
        print("\nErro: A capacidade deve ser um número inteiro.")
        return

    novo_ponto = PontoDeColeta(id_ponto, localizacao, capacidade)
    pontos_coleta[id_ponto] = novo_ponto
    
    print(f"\nPonto de coleta '{id_ponto}' criado com sucesso!")

def listar_pontos():
    limpar_tela()
    print("--- Lista de Pontos de Coleta Cadastrados ---\n")
    if not pontos_coleta:
        print("Nenhum ponto de coleta cadastrado.")
        return
    
    for ponto in pontos_coleta.values():
        print(ponto)

def atualizar_ponto():
    listar_pontos()
    id_ponto = input("\nDigite o ID do ponto que deseja atualizar (ou deixe em branco para cancelar): ").upper()
    if not id_ponto or id_ponto not in pontos_coleta:
        print("\nOperação cancelada ou ID inválido.")
        return

    ponto_a_atualizar = pontos_coleta[id_ponto]
    
    print("\nDeixe o campo em branco para manter a informação atual.")
    
    nova_localizacao = input(f"Nova localização ({ponto_a_atualizar.localizacao}): ")
    if nova_localizacao:
        ponto_a_atualizar.localizacao = nova_localizacao

    try:
        nova_capacidade_str = input(f"Nova capacidade em kg ({ponto_a_atualizar.capacidade_kg}): ")
        if nova_capacidade_str:
            ponto_a_atualizar.capacidade_kg = int(nova_capacidade_str)
        
        nova_ocupacao_str = input(f"Nova ocupação atual em kg ({ponto_a_atualizar.ocupacao_atual_kg}): ")
        if nova_ocupacao_str:
            ponto_a_atualizar.ocupacao_atual_kg = int(nova_ocupacao_str)
    except ValueError:
        print("\nErro: Capacidade e ocupação devem ser números inteiros.")
        return
        
    print(f"\n✅ Ponto de coleta '{id_ponto}' atualizado com sucesso!")

def deletar_ponto():
    listar_pontos()
    id_ponto = input("\nDigite o ID do ponto que deseja deletar (CUIDADO: esta ação é irreversível): ").upper()
    if id_ponto in pontos_coleta:
        confirmacao = input(f"Tem certeza que deseja deletar o ponto '{id_ponto}'? (s/n): ").lower()
        if confirmacao == 's':
            del pontos_coleta[id_ponto]
            print(f"\nPonto de coleta '{id_ponto}' deletado com sucesso!")
        else:
            print("\nOperação cancelada.")
    else:
        print("\nErro: Ponto de coleta não encontrado.")

# --- CRUD Equipes de Limpeza ---

def criar_equipe():
    """CREATE: Adiciona uma nova equipe de limpeza."""
    limpar_tela()
    print("--- Cadastrar Nova Equipe de Limpeza ---\n")
    id_equipe = input("Digite o ID da nova equipe (ex: 'EQ-A'): ").upper()
    if id_equipe in equipes:
        print("\nErro: Já existe uma equipe com este ID.")
        return
    
    nome = input("Digite o nome da equipe (ex: 'Alfa'): ")
    try:
        membros = int(input("Digite a quantidade de membros da equipe: "))
    except ValueError:
        print("\nErro: A quantidade de membros deve ser um número inteiro.")
        return

    nova_equipe = EquipeLimpeza(id_equipe, nome, membros)
    equipes[id_equipe] = nova_equipe
    
    print(f"\n✅ Equipe '{nome}' cadastrada com sucesso!")

def listar_equipes():
    """READ: Lista todas as equipes cadastradas."""
    limpar_tela()
    print("--- Lista de Equipes de Limpeza Cadastradas ---\n")
    if not equipes:
        print("Nenhuma equipe de limpeza cadastrada.")
        return
    
    for equipe in equipes.values():
        print(equipe)

def atualizar_equipe():
    """UPDATE: Atualiza os dados de uma equipe existente."""
    listar_equipes()
    id_equipe = input("\nDigite o ID da equipe que deseja atualizar (ou deixe em branco para cancelar): ").upper()
    if not id_equipe or id_equipe not in equipes:
        print("\nOperação cancelada ou ID inválido.")
        return

    equipe_a_atualizar = equipes[id_equipe]
    
    print("\nDeixe o campo em branco para manter a informação atual.")
    
    novo_nome = input(f"Novo nome da equipe ({equipe_a_atualizar.nome}): ")
    if novo_nome:
        equipe_a_atualizar.nome = novo_nome

    try:
        novos_membros_str = input(f"Nova quantidade de membros ({equipe_a_atualizar.membros}): ")
        if novos_membros_str:
            equipe_a_atualizar.membros = int(novos_membros_str)
    except ValueError:
        print("\nErro: A quantidade de membros deve ser um número inteiro.")
        return
        
    print(f"\n✅ Equipe '{id_equipe}' atualizada com sucesso!")

def deletar_equipe():
    """DELETE: Remove uma equipe do dicionário."""
    listar_equipes()
    id_equipe = input("\nDigite o ID da equipe que deseja deletar (CUIDADO: esta ação é irreversível): ").upper()
    if id_equipe in equipes:
        confirmacao = input(f"Tem certeza que deseja deletar a equipe '{id_equipe}'? (s/n): ").lower()
        if confirmacao == 's':
            del equipes[id_equipe]
            print(f"\n🗑️ Equipe '{id_equipe}' deletada com sucesso!")
        else:
            print("\nOperação cancelada.")
    else:
        print("\nErro: Equipe não encontrada.")

# --- Menus da Aplicação ---

def menu_pontos_coleta():
    """Exibe o menu de gerenciamento de pontos de coleta."""
    while True:
        limpar_tela()
        print("--- Gerenciar Pontos de Coleta ---")
        print("1. Criar Ponto de Coleta")
        print("2. Listar Todos os Pontos")
        print("3. Atualizar Ponto de Coleta")
        print("4. Deletar Ponto de Coleta")
        print("0. Voltar ao Menu Principal")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            criar_ponto()
        elif escolha == '2':
            listar_pontos()
        elif escolha == '3':
            atualizar_ponto()
        elif escolha == '4':
            deletar_ponto()
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

def menu_equipes_limpeza():
    """(NOVA FUNCIONALIDADE) Exibe o menu de gerenciamento de equipes."""
    while True:
        limpar_tela()
        print("--- Gerenciar Equipes de Limpeza ---")
        print("1. Cadastrar Nova Equipe")
        print("2. Listar Todas as Equipes")
        print("3. Atualizar Dados da Equipe")
        print("4. Deletar Equipe")
        print("0. Voltar ao Menu Principal")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            criar_equipe()
        elif escolha == '2':
            listar_equipes()
        elif escolha == '3':
            atualizar_equipe()
        elif escolha == '4':
            deletar_equipe()
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")


def main():
    """Função principal que exibe o menu inicial."""
    while True:
        limpar_tela()
        print("=====================================================")
        print("=== Sistema de Gestão de Resíduos ===")
        print("=====================================================\n")
        print("1. Gerenciar Pontos de Coleta")
        print("2. Gerenciar Equipes de Limpeza")
        print("0. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            menu_pontos_coleta()
        elif escolha == '2':
            menu_equipes_limpeza()
        elif escolha == '0':
            print("\nSaindo do sistema. Dados em memória serão perdidos.")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()