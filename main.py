import pygame as pg
import customtkinter as ctk
import ia


board = [[0 for u in range(3)] for i in range(3)]
who = 0


def turn(coord):
    x, y = coord[0] // 300, coord[1] // 300
    global who
    if board[y][x] != 0:
        who = 0 if who == 1 else 1
        return False
    board[y][x] = who + 1
    if not check_win():
        if ia_active:
            print(ia.get_best_move(board))
            case_tuple = ia.get_best_move(board)
            board[case_tuple[1]][case_tuple[0]] = who + 2 if who == 0 else 1
            who = 0 if who == 1 else 1
        who = 0 if who == 1 else 1
    else:
        return False


def win_interface(winner = 3):
    if winner == False:
        return False
    global is_over
    is_over = True
    back_rect = pg.draw.rect(screen, color=(200, 200, 200), rect=(100, 300, 700, 300))
    if winner == 1:
        text = rob_font.render("Cross wins", True, (0, 0, 0))
        screen.blit(text, (127, 360))
    elif winner == 2:
        text = rob_font.render("Circle wins", True, (0, 0, 0))
        screen.blit(text, (127, 360))
    elif winner == 3:
        text = rob_font.render("Draw", True, (0, 0, 0))
        screen.blit(text, (200, 360))


def check_win():
    global board
    for i in range(3):
        if 0 != board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if 0 != board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if 0 != board[0][0] == board[1][1] == board[2][2] or 0 != board[0][2] == board[1][1] == board[2][0]:
        return board[i][0]
    return check_draw()


def check_draw():
    for i in range(3):
        for u in range(3):
            if board[i][u] == 0:
                return False
    return 3

def open_menu():
    root = ctk.CTk()
    root.geometry("230x200")
    root.title("Start Menu")
    ia_active = ctk.BooleanVar()
    frame = ctk.CTkFrame(root)
    titleLabel = ctk.CTkLabel(root, width=200, font=("Roboto", 40), height=100, text="Tic Tac Toe")
    startButton = ctk.CTkButton(root, width=100, height=50, text="Start", command=root.destroy, font=('Roboto', 20))
    checkIA = ctk.CTkCheckBox(root, height=10, variable =ia_active, onvalue = True,
                              offvalue = False, text="Play against IA ?")
    checkIA.grid(row=2, column=1, padx=10, pady=10)
    startButton.grid(row=3, column=1, padx=10)
    titleLabel.grid(row=1, column=1, padx=10)
    root.mainloop()
    return ia_active.get()


ia_active = open_menu()
ia_color = 1
pg.init()
dimensions = (900, 900)
screen = pg.display.set_mode(dimensions)
FPS = 30
rob_font = pg.font.SysFont("roboto", 130)
running = True
is_over = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP and not is_over:
            print(ia_active)
            pos = pg.mouse.get_pos()
            turn(pos)
            print("\n")
            for e in board:
                print(e)
    for i in range(3):
        for u in range(3):
            pg.draw.rect(screen, color=(255, 255, 255), rect=(i*300, u*300, 300, 300), width=3)
            if board[i][u] == 1:
                pg.draw.line(screen, color=(255, 255, 255), start_pos=(u*300, i*300),
                             end_pos=(u*300+300, i*300+300), width=3)
                pg.draw.line(screen, color=(255, 255, 255), start_pos=(u*300, i*300+300),
                             end_pos=(u*300+300, i*300), width=3)
            elif board[i][u] == 2:
                pg.draw.circle(screen, color=(255, 255, 255), center=(u*300+150, i*300+150), radius=140)
    ended = check_win()
    win_interface(ended)
    pg.display.flip()
