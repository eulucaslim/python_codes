# dicionário
teams = {}

# encerrar o programa
done = False

# função para listar times
def print_teams():
    print("Times Listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

# função para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")
        
# laço de repetição para exibir o programa
       
while not done:
    
    # Opções do programa
    
    print("O que você deseja fazer\n")
    print("1 - Adicionar um time")
    print("2 - Remover um time")
    print("3 - Listar times")
    print("4 - Adicionar Jogador em um time")
    print("5 - Remover jogador de um time")
    print("6 - Listar jogadores de um time")
    print("7 - Sair")
    
    # Escolha 
    choice = input("> ")
    
    if choice == "1":
        team_name = input("Digite o nome do time\n")
        teams[team_name] = {"name": team_name, "players": []}
        print("Time Adicionado")
        
    elif choice == "2":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja remover\n"))
        
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print("Time Removido...")
        
        else:
            print("Numero Inválido")
            
    elif choice == "3":
        print_teams()
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja adicionar o jogador\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Informe o nome do jogador\n")
            teams[team_name]['players'].append(player_name)
            print("Jogador Adicionado no time")
        else:
            print("Numéro de time está inválido")
    
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja remover o jogador\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover\n"))
            if player_num <= len(teams[team_name]["players"]):
                del teams[team_name]["players"][player_num -1]
                print("Jogador removido do time.")
            else:
                print("Numero do jogador inválido")
        else:
            print("Número do time inválido")
        
    
    elif choice == "6":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja listar os jogador\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
        
        else:
            print("Número do time inválido")
    
    elif choice == "7":
        done = True
        print("Encerrando programa...")
    
    else:
        print("Opção Inválida")
    