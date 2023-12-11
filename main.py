import pygame as pg


board = []


class Case:
    def __init__(self, state):
        self.state = state
        self.state_str = ""
        match self.state:
            case 0:
                self.state_str = "Blank"
            case 1:
                self.state_str = "Cross"
            case 2:
                self.state_str = "Circle"
            case _:
                self.state_str = "Blank"

    def __str__(self):
        return f"State: {self.state_str}"

    def __repr__(self):
        return f"State: {self.state_str}"


def create_board():
    global board
    for i in range(3):
        board.append([])
        for u in range(3):
            board[i].append(Case(0))


def place_case(coord, type):
    board[coord[1]][coord[0]] = Case(type)


who = 1


def turn(coord):
    x, y = coord[0] // 300, coord[1] // 300
    global who
    if board[y][x].state != 0:
        who = 0 if who == 1 else 1
        return False
    place_case((x, y), who+1)


def win_interface(winner = 2):
    global is_over
    is_over = True
    back_rect = pg.draw.rect(screen, color=(255, 255, 255), rect=(100, 300, 700, 300))
    match (winner):
        case 0:
            text = rob_font.render("Cross wins", True, (0, 0, 0))
            screen.blit(text, (127, 360))
        case 1:
            text = rob_font.render("Circle wins", True, (0, 0, 0))
            screen.blit(text, (127, 360))
        case 2:
            text = rob_font.render("Draw", True, (0, 0, 0))
            screen.blit(text, (200, 360))


def check_win():
    global board
    is_equality = False
    for e in board:
        for el in e:
            if el.state == 0:
                is_equality = True
    for i in range(3):
        if 0 != board[i][0].state == board[i][1].state == board[i][2].state:
            win_interface(who)
    for i in range(3):
        if 0 != board[0][i].state == board[1][i].state == board[2][i].state:
            win_interface(who)
    if 0 != board[0][0].state == board[1][1].state == board[2][2].state or 0 != board[0][2].state == board[1][1].state == board[2][0].state:
        win_interface(who)
    elif not is_equality:
        win_interface()



create_board()

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
            who = 0 if who == 1 else 1
            pos = pg.mouse.get_pos()
            turn(pos)
            print("\n")
            for e in board:
                print(e)
    for i in range(3):
        for u in range(3):
            pg.draw.rect(screen, color=(255, 255, 255), rect=(i*300, u*300, 300, 300), width=3)
            if board[i][u].state == 1:
                pg.draw.line(screen, color=(255, 255, 255), start_pos=(u*300, i*300), end_pos=(u*300+300, i*300+300), width=3)
                pg.draw.line(screen, color=(255, 255, 255), start_pos=(u*300, i*300+300), end_pos=(u*300+300, i*300), width=3)
            elif board[i][u].state == 2:
                pg.draw.circle(screen, color=(255, 255, 255), center=(u*300+150, i*300+150), radius=140)
    check_win()
    pg.display.flip()
