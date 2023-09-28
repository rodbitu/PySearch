# Inicializa o tabuleiro com espaços em branco
def initialize_board(size = 3):
    return [[" " for _ in range(size)] for _ in range(size)]

# Printa o tabuleiro na tela
def display_board(board):
    size = len(board)
    print("  " + "   ".join(map(str, range(size))))  # Printa os rótulos das colunas
    for i, row in enumerate(board):
        print(f"{i} {' | '.join(row)}")  # Printa as linhas do tabuleiro
        if i < size - 1:
            print(" ---" + "+---" * (size - 1))  # Printa as linhas horizontais entre as linhas do tabuleiro

# Checkagem de vitória
def check_victory(board, player):
    size = len(board)
    
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or all(board[j][i] == player for j in range(size)):
            return True
    if all(board[i][i] == player for i in range(size)) or all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False

# Movimentos disponíveis no tabuleiro
def available_moves(board):
    size = len(board)
    return [(i, j) for i in range(size) for j in range(size) if board[i][j] == " "]

# Contador de nós gerados
def count_nodes(board):
    return sum(1 for row in board for cell in row if cell != " ")

# Função de avaliação heurística simples
def heuristic_evaluation(board):
    if check_victory(board, "O"):
        return 1
    elif check_victory(board, "X"):
        return -1
    else:
        return 0

# Algoritmo Minimax com poda alfa-beta
def minimax(board, player, depth, maximizing, alpha, beta):
    if depth == 0 or check_victory(board, "O") or check_victory(board, "X") or not available_moves(board):
        return heuristic_evaluation(board)

    if maximizing:
        best_value = -float("inf")
        for i, j in available_moves(board):
            board[i][j] = "O"
            value = minimax(board, "X", depth - 1, False, alpha, beta)
            board[i][j] = " "
            best_value = max(best_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return best_value
    else:
        worst_value = float("inf")
        for i, j in available_moves(board):
            board[i][j] = "X"
            value = minimax(board, "O", depth - 1, True, alpha, beta)
            board[i][j] = " "
            worst_value = min(worst_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return worst_value

# Função para a jogada do agente
def agent_move(board, max_depth):
    best_move = None
    best_value = -float("inf")
    for i, j in available_moves(board):
        board[i][j] = "O"
        value = minimax(board, "X", max_depth, False, -float("inf"), float("inf"))
        board[i][j] = " "
        if value > best_value:
            best_value = value
            best_move = (i, j)
    board[best_move[0]][best_move[1]] = "O"
    print(f"Nós gerados para esta jogada: {count_nodes(board)}")

# Função principal do jogo da velha
def tic_tac_toe_game():
    board_size = int(input("Digite o tamanho do tabuleiro(Obrigatório ser maior que 2). Ex: 3, 4, etc."))
    if board_size < 3:
        raise ValueError("Obrigatório tamanho do tabuleiro ser maior que 2.")
    
    board = initialize_board(board_size)

    while True:
        try:
            max_depth = int(input("Digite o nível de antecipação (profundidade do Minimax)"))
            break
        except ValueError:
            print("Input inválido. Digite um número válido.")

    # Pergunta ao usuário se deseja iniciar o jogo
    current_player = input("Deseja iniciar o jogo? (Y/N): ").upper()

    print("\nBem-Vindo ao jogo da velha!\n")

    if current_player == "N":
        current_player = "Agent"
        print("O agente inicia o jogo.")
        agent_move(board, max_depth)
    else:
        current_player = "You"
        print("Você inicia o jogo.")

    while True:
        display_board(board)

        if check_victory(board, "O"):
            print("O agente ganhou!")
            break
        elif check_victory(board, "X"):
            print("Você ganhou!")
            break
        elif not available_moves(board):
            print("Empatou!")
            break

        if current_player == "You":
            while True:
                try:
                    row = int(input(f"Escolha a linha (0-{board_size - 1}): "))
                    col = int(input(f"Escolha a coluna (0-{board_size - 1}): "))
                    if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == " ":
                        break
                    else:
                        print("Posição inválida. Tente denovo.")
                except ValueError:
                    print("Input inválido. Digite um número válido.")
            board[row][col] = "X"
        else:
            agent_move(board, max_depth)

        current_player = "Agent" if current_player == "You" else "You"

tic_tac_toe_game()