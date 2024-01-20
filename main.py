import time
import random
import sys

DEPTH = None


class Mancala_Game:
    def __init__(self, mancala):
        if mancala != None:
            self.mancala = mancala[:]
        else:
            self.mancala = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def print_mancala(self):
        print(" " + " ".join(['(' + str(x) + ')' for x in range(12, 6, -1)]))
        print("    " + "   ".join(["v"] * 6))
        print(f"    {' | '.join([str(x) for x in self.mancala[12:6:-1]])}")
        print(f"{self.mancala[13]} {' ' * 25} {self.mancala[6]}")
        print(f"    {' | '.join([str(x) for x in self.mancala[0:6]])}")

        print("    " + "   ".join(["^"] * 6))
        print("   " + " ".join(['(' + str(x) + ')' for x in range(6)]))

    def make_player_move(self, i):   #responsavel por fazer mover as peças e indicar se o jogador tem direito a jogada nova
        repeat_turn = False
        pecas = self.mancala[i]
        self.mancala[i] = 0

        for j in range(pecas):
            i += 1
            i = i % 14     # evita que i tenha um valor superior ao indice 13

            if i == i % 7 + 6:     #garante que um jogador não pontue na casa do oponente
                continue

            self.mancala[i] += 1

            if j == pecas - 1:     # se esta tiver sido a ultima iteração do loop.....
                if i == 6 or i == 13:
                    repeat_turn = True
                if steal_option == True:
                    if i < 6 and self.mancala[i] == 1 and self.mancala[-i + 12] != 0:
                        self.mancala[6] += self.mancala[-i + 12] + 1
                        self.mancala[i] = 0
                        self.mancala[-i + 12] = 0
                    elif i > 6 and i != 13 and self.mancala[i] == 1 and self.mancala[12 - i] != 0:
                        self.mancala[13] += self.mancala[12 - i] + 1
                        self.mancala[i] = 0
                        self.mancala[12 - i] = 0

        return repeat_turn

    def End(self):
        if sum(self.mancala[0:6]) == 0:
            self.mancala[13] += sum(self.mancala[7:13])
            self.mancala[0:6] = [0] * 6
            self.mancala[7:13] = [0] * 6
            return True
        elif sum(self.mancala[7:13]) == 0:
            self.mancala[6] += sum(self.mancala[0:6])
            self.mancala[0:6] = [0] * 6
            self.mancala[7:13] = [0] * 6
            return True
        return False


    def get_heuristic(self):
        if self.End():
            if self.mancala[13] > self.mancala[6]:
                return 100
            elif self.mancala[13] == self.mancala[6]:
                return 0
            else:
                return -100
        else:
            return self.mancala[13] - self.mancala[6]

def get_hint(mancala):
    best_value = -float('inf')
    best_move = -1
    for i in range(0, 6):
        if mancala.mancala[i] == 0:
            continue
        copy = Mancala_Game(mancala.mancala[:])
        copy.make_player_move(i)
        new_value, _ = alphabeta(copy, depth=10, maximizing_player=False)  #maiximizing a False, para que o minimax comece a testar a
        if new_value > best_value:                                         # melhor jogada consoante a perspetiva do jogador
            best_value = new_value
            best_move = i
    print(f"Recommended move: {best_move}")


def alphabeta(mancala, depth=DEPTH, alpha=-999, beta=999, maximizing_player=False):
    if depth == 0 or mancala.End():
        return mancala.get_heuristic(), -1              #evitar um loop infinito e que o programa
                                                        # tente avaliar um estado do jogo que não pode mais ser modificado,
                                                        #pois o jogo já chegou ao fim.
    start_time = time.time()
    if maximizing_player:

        best_value = -float('inf')
        player_move = -1
        for i in range(7, 13, 1):
            if mancala.mancala[i] == 0:
                continue
            copy = Mancala_Game(mancala.mancala[:])
            test = copy.make_player_move(i)

            new_value, _ = alphabeta(copy, depth - 1, alpha, beta, not maximizing_player)

            if best_value < new_value:

                make_player_move = i
                best_value = new_value
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        end_time = time.time()
        return best_value, make_player_move
    else:
        best_value = float('inf')
        player_move = -1
        for i in range(0, 6, 1):
            if mancala.mancala[i] == 0:
                continue

            copy = Mancala_Game(mancala.mancala[:])
            test = copy.make_player_move(i)
            new_value, _ = alphabeta(copy, depth - 1, alpha, beta, not maximizing_player)

            if best_value > new_value:
                make_player_move = i
                best_value = new_value
            beta = min(beta, best_value)
            if alpha >= beta:
                break

        end_time = time.time()
        return best_value, make_player_move

def computer_vs_computer(depth_p1, depth_p2):
    mancala = Mancala_Game(None)
    turn = random.randint(0, 1)
    while not mancala.End():
        print(f"\nTurn {turn}")
        mancala.print_mancala()
        sys.stdout.flush()

        if turn % 2 == 0:
            # Player 1 (maximizing player)
            best_value = -float('inf')
            best_move = -1
            for i in range(0, 6):
                if mancala.mancala[i] == 0:
                    continue
                copy = Mancala_Game(mancala.mancala[:])
                copy.make_player_move(i)
                new_value, _ = alphabeta(copy, depth=depth_p1, maximizing_player=True)
                if new_value > best_value:
                    best_value = new_value
                    best_move = i
            print(f"Player 1 makes move: {best_move}")
            mancala.make_player_move(best_move)

        else:
            # Player 2 (minimizing player)
            best_value = float('inf')
            best_move = -1
            for i in range(7, 13, 1):
                if mancala.mancala[i] == 0:
                    continue
                copy = Mancala_Game(mancala.mancala[:])
                copy.make_player_move(i)
                new_value, _ = alphabeta(copy, depth=depth_p2, maximizing_player=False)
                if new_value < best_value:
                    best_value = new_value
                    best_move = i
            print(f"Player 2 makes move: {best_move}")
            mancala.make_player_move(best_move)

        turn += 1

    print("\nGame over!")
    mancala.print_mancala()
    sys.stdout.flush()

    if mancala.mancala[6] > mancala.mancala[13]:
        print("Player 1 wins!")
    elif mancala.mancala[6] < mancala.mancala[13]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")



def player1_player2():
    board = Mancala_Game(None)
    board.print_mancala()
    while True:
        if board.End():
            break
        while True:
            if board.End():
                break
            move = int(input("\n \n PLAYER 1 TURN (7-12) >>> "))
            if move < 7 or move > 12 or board.mancala[move] == 0:
                print("You can't play at this position. Choose another position")
                continue

            board_move = board.make_player_move(move)
            board.print_mancala()
            if not board_move:
                break
        while True:
            if board.End():
                break
            move = int(input("PLAYER 2 TURN (0-5) >>> "))
            if move > 5 or board.mancala[move] == 0:
                print("You can't play at this position. Choose another position")
                continue

            board_move = board.make_player_move(move)
            board.print_mancala()
            if not board_move:     #verifica se o jogador tem direito a uma jogada extra
                break

    if board.mancala[6] < board.mancala[13]:
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")
    print('GAME ENDED')
    board.print_mancala()


def player_aibot():     ## O CODIGO ESTA DUPLICADO DEVIDO AO FACTO DE QUE A DECISÃO DE QUEM COMEÇA A JOGAR É ALEATORIA
    hint: int = 2
    board = Mancala_Game(None)
    board.print_mancala()


    starting_player = random.randint(0, 1)   #sorteio de quem começa


    if starting_player == 0:         #o jogador 1 começa a jogar

        while True:
            if board.End():
                break
            while True:
                if board.End():
                    break
                if board.mancala[13] - board.mancala[6] >= 5 and hint > 0:
                    resp = input("You are almost losing, do you want a hint? You only have %d left (y/n) " % (hint))
                    if resp == 'y':
                        move = get_hint(board)
                        print(move)
                        hint -= 1
                move = int(input("\n\n  YOUR TURN >>> "))
                if move > 5 or board.mancala[move] == 0:
                    print("You can't Play at this position. Choose another one")
                    continue
                move_result = board.make_player_move(move)
                board.print_mancala()
                if not move_result:
                    break

            while True:
                if board.End():
                    break
                print("\n\nAI-BOT TURN >>> ", end="")
                start_time = time.time()
                _, k = alphabeta(board, 10, -100000, 100000, True)
                print(k)
                end_time = time.time()
                total_time = end_time - start_time
                print(">>Calculated in {:.3f}".format(total_time))
                board_result = board.make_player_move(k)
                board.print_mancala()

                if not board_result:
                    break

        board.print_mancala()

    else:
        # AI-BOT começa a jogar
        while True:
            if board.End():
                break

            while True:
                if board.End():
                    break
                print("\n\nAI-BOT TURN >>> ", end="")
                start_time = time.time()
                _, k = alphabeta(board, 10, -100000, 100000, True)
                print(k)
                end_time = time.time()
                total_time = end_time - start_time
                print(">>Calculated in {:.3f}".format(total_time))
                board_result = board.make_player_move(k)
                board.print_mancala()

                if not board_result:
                    break

            while True:
                if board.End():
                    break
                if board.mancala[13] - board.mancala[6] >= 5 and hint > 0:
                    resp = input("You are almost losing, do you want a hint? You only have %d left (y/n) " % (hint))
                    if resp == 'y':
                        move = get_hint(board)
                        hint -= 1
                move = int(input("\n\n YOUR TURN >>> "))
                if move > 5 or board.mancala[move] == 0:
                    print("You can't Play at this position. Choose another")
                    continue
                move_result = board.make_player_move(move)
                board.print_mancala()
                if not move_result:
                    break

    board.print_mancala()

    if board.mancala[6] < board.mancala[13]:
        print("\n "
              "*****        ITS GAME OVER    ****** \n"
              "||||||||||||| AI WINS |||||||||||")

    else:
        print("*****        ITS GAME OVER    ****** \n"
                  "||||||||||| YOU WIN  ||||||||||")





print("\n:::::::::::::::::::::::::::::::::::::::")
print("!!!   BEM VINDO AO JOGO DO MANCALA  !!!")
print(":::::::::::::::::::::::::::::::::::::::")
while True:
    print("(1) Play ")
    print("(2) Credits")
    print("(3) Quit ")
    type = int(input(">>>"))
    if type == 1:
        print("\n" * 20)
        print("(1) Player 1 vs Player 2")
        print("(2) Player 1 vs AI ")
        print("(3) Computer vs computer")
        print("(4) go back")
        type = int(input(">>>"))
        if type == 1:
            print("\n" * 20)
            print("CHOOSE YOUR DIFICULTY")
            print("(1) Easy (no stealing)")
            print("(2) Hard ( stealing)")
            print("(3) Go back")
            type = int(input(">>>"))
            if type == 1:
                steal_option = False
                player1_player2()
                break
            elif type == 2:
                steal_option = True
                player1_player2()
                break
            elif type == 3:
                continue
        elif type == 2:
            print("\n" * 20)
            print("CHOOSE YOUR DIFICULTY")
            print("(1) Easy (no stealing)")
            print("(2) Hard ( stealing and medium Minimax depth limit)")
            print("(3) Hardcore ( stealing and high MiniMax depth limit)")
            print("(4) Go back")
            type = int(input(">>>"))
            if type == 1:
                steal_option = False
                DEPTH = 3
                player_aibot()
                break
            elif type == 2:
                steal_option = True
                player_aibot()
                DEPTH = 6
                break
            elif type == 3:
                steal_option = True
                DEPTH = 15
                player_aibot()
            elif type == 4:
                continue

            else:
                print("Wrong Gameplay Type. Enter Again")
                continue
        elif type == 3:
            print("Indique a profundidade do AI-BOT 1")
            depth_p1 = int(input())
            print("Indique a profundidade do AI-BOT 2")
            depth_p2 = int(input())
            steal_option = True
            computer_vs_computer(depth_p1, depth_p2)


    elif type == 2:
        print("\n" * 20)
        print("##################################################################################################################### \n"
            " This game was created by Guilherme Jesus Oliveira and Rodrigo Teixeira Taveira within the scope of the EIACD discipline \n"
              " Hope you enjoy it  :).  Wanna try it? \n"
              "#####################################################################################################################")
    elif type == 3:
        print("\n" * 20)
        print(" You quit")
        break
    else:
        print("Wrong Gameplay Type. Try Again")
        continue