import turtle as t
import random as r 
import time
 
def start_moves():
    global width_height
    global n
    global game_mode
    global side
    global scores_place
    global screen
    global positionsO
    global positionsX
    global positions_computer
    global positions_player
    global allpositions
    global Lxcentrecoordinates
    global Lycentrecoordinates
    global score
    global playerside
    global control_turn
    global control_score
    global write_score
    width_height = int(t.numinput('Size', 'Choose the size of the window (prefer a number between 400 and 800): ', default = 700))
    n = int(t.numinput('Cells', 'Give the number of cells you want in each side: ', default = 3))
    game_mode = int(t.numinput('Game mode', "Choose the game mode (1 player against the computer (1) or 2 players against each other (2) or the computer against itself (3) ?): ", default=1))
    if game_mode == 1:
        side = t.textinput('Playerside', "Choose how you want to play (type 'X' or 'O'): ")
    elif game_mode == 2:
        side = t.textinput('Playerside', "How the first player wants to play? (type 'X' or 'O'): ")
    scores_place = 300
    positionsO = []
    positionsX = []
    allpositions = []
    Lxcentrecoordinates = []
    Lycentrecoordinates = []
    for i in range(0, n):
        Lxcentrecoordinates.append((2 * i + 1) * width_height / (2 * n))
        Lycentrecoordinates.append((2 * i + 1) * width_height / (2 * n))
    scoreX = 0
    scoreO = 0
    score = [scoreX, scoreO]
    screen = t.Screen()
    screen.setup(width_height + scores_place, width_height, startx = 0, starty = 0)
    screen.screensize(width_height+scores_place, width_height)
    screen.setworldcoordinates(0, 0, width_height+scores_place, width_height)
    screen.title('Tictactoe')
    screen.bgcolor('yellow')
    t.speed('fastest')
    t.hideturtle()
    t.penup()
    for i in range(30):
        t.color((i % 2) * 'blue' + ((i + 1) % 2) * 'red')
        t.goto((width_height + scores_place) / 2, 20 / (i / 3 + 10) * width_height / 3)
        t.write('Tic Tac Toe', move = False, align = 'center', font = 'Calibri {}'.format(int(3.5 * (i + 1) * width_height / 600)))
    time.sleep(2)
    t.clear()
    t.color('green')
    if game_mode == 3:
        control_turn = 'computer'
        t.goto((width_height + scores_place) / 2, 2 * width_height / 3)
        t.write("The computer against itself...", move = False, align = 'center', font = 'Calibri {}'.format(int(50 * width_height / 600)))
        side = 'O'
##        time.sleep(1)
##        first_play = r.randint(0, 1)
##        if first_play == 0:
##            t.goto((width_height + scores_place) / 2, width_height / 3)
##            t.write("Computer ▢ plays first!", move = False, align = 'center', font = 'Calibri {}'.format(int(50 * width_height / 600)))
##            side = 'O'
##        elif first_play == 1:
##            t.goto((width_height + scores_place) / 2, width_height / 3)
##            t.write("Computer x plays first!", move = False, align = 'center', font = 'Calibri {}'.format(int(50 * width_height / 600)))
##            side = 'O'
    if side == 'O' or side == 'o' or side == '' or side == None:
        playerside = 0
        control_score = 0
        positions_computer = positionsX
        positions_player = positionsO
    elif side == 'X' or side == 'x':
        playerside = 1
        control_score = 1
        positions_computer = positionsO
        positions_player = positionsX
    if game_mode == 1:
        t.goto((width_height + scores_place) / 2, 2 * width_height / 3)
        t.write("I am turning a coin...", move = False, align = 'center', font = 'Calibri {}'.format(int(60 * width_height / 600)))
        time.sleep(1)
        first_play = r.randint(0, 1)
        if first_play == 0:
            t.goto((width_height + scores_place) / 2, width_height / 3)
            t.write("You play first!", move = False, align = 'center', font = 'Calibri {}'.format(int(60 * width_height / 600)))
            control_turn = 'player'
        elif first_play == 1:
            t.goto((width_height + scores_place) / 2, width_height / 3)
            t.write("I play first!", move = False, align = 'center', font = 'Calibri {}'.format(int(60 * width_height / 600)))
            control_turn = 'computer'
            playerside = playerside + 1
    if game_mode == 2:
        control_turn = 'player'
        t.goto((width_height + scores_place) / 2, 2 * width_height / 3)
        t.write("Get ready...", move = False, align = 'center', font = 'Calibri {}'.format(int(60 * width_height / 600)))
        time.sleep(1)
        t.goto((width_height + scores_place) / 2, width_height / 3)
        t.write("Go!", move = False, align = 'center', font = 'Calibri {}'.format(int(60 * width_height / 600)))
    time.sleep(2)
    t.clear()
    t.color('black')
    t.pensize(width_height /(10 * n))
    for i in range(0, n + 1):
        t.penup()
        t.goto(i * width_height / n, 0)
        t.pendown()
        t.goto(i * width_height / n, width_height)
    for i in range(0, n + 1):
        t.penup()
        t.goto(0, i * width_height / n)
        t.pendown()
        t.goto(width_height, i * width_height / n)
    t.penup()
    t.goto(width_height + 15, 0)
    t.color('green')
    t.pensize(10 * width_height / 600)
    t.setheading(90)
    t.pendown()
    for i in range(4):
        t.forward((i + 1) % 2 * width_height + (i % 2) * (scores_place - 15))
        t.right(90)
    t.penup()
    t.goto(width_height + 15 + (scores_place - 15) / 2, width_height * 8.7 / 10)
    t.write('Scores:', move = False, align = 'center', font = 'Calibri {}'.format(int(30 * width_height / 600)))
    t.goto(width_height + 15 + (scores_place - 15) / 2, width_height * 1.5 / 10)
    t.write('Turn:', move = False, align = 'center', font = 'Calibri {}'.format(int(30 * width_height / 600)))
    t.goto(width_height + 15 + (scores_place - 15) / 2, width_height * 7 / 10)
    t.dot(150 * width_height / 600, 'blue')
    t.color('white')
    t.write('0', move = False, align = 'center', font = 'Calibri {}'.format(int(30 * width_height / 600)))
    t.goto(width_height + 15 + (scores_place - 15) / 2, width_height* 4 / 10)
    t.dot(150 * width_height / 600, 'red')
    t.write('0', move = False, align = 'center', font = 'Calibri {}'.format(int(30 * width_height / 600)))
    write_score = True
    if game_mode == 1 or game_mode == 2:
        turn()
    elif game_mode == 3:
        computers_only()
    
def X(a):
    t.penup()
    t.pensize(a / 5)
    t.left(135)
    t.forward(a / 2)
    t.right(135)
    for i in [1,-1]:
        t.pendown()
        t.begin_fill()
        t.right(i * 45)
        t.forward(a)
        t.left(180)
        t.forward(a)
        t.right(i * 135)
        t.penup()
        t.forward(a * 2 ** 0.5 / 2)
        t.left(180)
    t.penup()
    t.right(45)
    t.forward(a / 2)
    t.setheading(90)
    
def O(b):
    t.penup()
    t.pensize(0.3 * b)
    t.left(135)
    t.forward(0.5 * 2 ** 0.5 * b)
    t.right(135)
    for i in range(4):
        t.pendown()
        t.begin_fill()
        t.forward(b)
        t.right(90)
        t.end_fill()
    t.penup()
    t.right(45)
    t.forward(0.5 * 2 ** 0.5 * b)
    t.setheading(90)

def coordinates_grid(x, y, alteration):
    if alteration == 'coordinates -> grid':
        return [int(x * n / width_height), int(y * n / width_height)]
    elif alteration == 'grid -> coordinates':
        return [(2 * x + 1) * width_height / (2 * n), (2 * y + 1) * width_height / (2 * n)]

def middlepoint(x, y):
    Lx=[]
    Ly=[]
    Lxchoose=[]
    Lychoose=[]
    for i in range(0, n):
        Lx.append(abs(Lxcentrecoordinates[i] - x))
        Ly.append(abs(Lycentrecoordinates[i] - y))
    for i in range(0, n):
        Lxchoose.append([Lx[i], Lxcentrecoordinates[i]])
        Lychoose.append([Ly[i], Lycentrecoordinates[i]])
    Lx.sort()
    Ly.sort()
    for i in range(0, n):
        if Lxchoose[i][0] == Lx[0]:
            x = Lxchoose[i][1]
        if Lychoose[i][0] == Ly[0]:
            y = Lychoose[i][1]
    t.setposition(x, y)
    
def turn():
    t.penup()
    t.goto(width_height + 15 + (scores_place - 15) / 2, width_height / 80)
    if len(allpositions) != n ** 2:
        t.color('yellow')
        t.write(((playerside + 1) % 2) * 'x' + (playerside % 2) * '▢', move = False, align = 'center', font = 'Calibri {}'.format(int(70 * width_height / 600)))
        t.color(((playerside + 1) % 2) * 'blue' + (playerside % 2) * 'red')
        t.write(((playerside + 1) % 2) * '▢' + (playerside % 2) * 'x', move = False, align = 'center', font = 'Calibri {}'.format(int(70 * width_height / 600)))
        if control_turn == 'computer':
            computer_play()
        
def computer_play():
    global control_turn
    global control_score
    global score
    global write_score
    global allpositions
    global positions_computer
    global positions_player
    global playerside
    max_score_computer = 0
    max_score_computer2 = 0
    max_score_player = 0
    sum_score = 0
    L_positions = []
    for i in range(n):
        for j in range(n):
            if [i, j] not in allpositions:
                L_positions.append([i, j])
    random_position = r.choice(L_positions)
    random_grid_part = [random_position[0], random_position[1]]
    chosen_grid_parts_computer = []
    chosen_grid_parts_computer2 = []
    chosen_grid_parts_player = []
    chosen_grid_parts_player2 = []
    chosen_grid_parts = []
    last_score_computer = score[control_score]
    last_score_player = score[abs(control_score - 1)]
    write_score = False
    if len(allpositions) < 2:
        centre_block = [int(n / 2), int(n / 2)]
        if n % 2 == 0:
            random_choice_x = r.randint(-1, 0)
            random_choice_y = r.randint(-1, 0)
        elif n % 2 != 0:
            random_choice_x = r.randint(-1, 1)
            random_choice_y = r.randint(-1, 1)
        chosen_grid_part = [centre_block[0] + random_choice_x, centre_block[1] + random_choice_y]
    else:
        for i in range(n):
            for j in range(n):
                if [i, j] not in allpositions:
                    playerside = playerside + 1
                    positions_computer.append([i, j])
                    scoreXO()
                    if score[control_score] - last_score_computer > max_score_computer:
                        max_score_computer = score[control_score] - last_score_computer
                        chosen_grid_parts_computer = []
                        chosen_grid_parts_computer.append([i, j])
                    elif score[control_score] - last_score_computer == max_score_computer:
                        chosen_grid_parts_computer.append([i, j])
                    score[control_score] = last_score_computer
                    positions_computer.pop(-1)
                    playerside = playerside + 1
                    positions_player.append([i, j])
                    scoreXO()
                    if score[abs(control_score-1)] - last_score_player > max_score_player:
                        max_score_player = score[abs(control_score-1)] - last_score_player
                        chosen_grid_parts_player = []
                        chosen_grid_parts_player.append([i, j])
                    elif score[abs(control_score-1)] - last_score_player == max_score_player:
                        chosen_grid_parts_player.append([i, j])
                    score[abs(control_score-1)] = last_score_player
                    positions_player.pop(-1)
        for item in chosen_grid_parts_computer:
            positions_computer.append(item)
            allpositions.append(item)
            for i in range(n):
                for j in range(n):
                    if [i, j] not in allpositions:
                        playerside = playerside + 1
                        positions_computer.append([i, j])
                        scoreXO()
                        sum_score = sum_score + score[control_score]
                        score[control_score] = last_score_computer
                        positions_computer.pop(-1)
                        playerside = playerside + 1
            if sum_score > max_score_computer2:
                max_score_computer2 = sum_score
                chosen_grid_parts_computer2 = []
                chosen_grid_parts_computer2.append(item)
            elif sum_score == max_score_computer2:
                chosen_grid_parts_computer2.append(item)
            positions_computer.pop(-1)
            allpositions.pop(-1)
            sum_score = 0
        max_score_computer2 = 0
        sum_score = 0
        for item in chosen_grid_parts_player:
            positions_computer.append(item)
            allpositions.append(item)
            for i in range(n):
                for j in range(n):
                    if [i, j] not in allpositions:
                        playerside = playerside + 1
                        positions_computer.append([i, j])
                        scoreXO()
                        sum_score = sum_score + score[control_score]
                        score[control_score] = last_score_computer
                        positions_computer.pop(-1)
                        playerside = playerside + 1
            if sum_score > max_score_computer2:
                max_score_computer2 = sum_score
                chosen_grid_parts_player2 = []
                chosen_grid_parts_player2.append(item)
            elif sum_score == max_score_computer2:
                chosen_grid_parts_player2.append(item)
            positions_computer.pop(-1)
            allpositions.pop(-1)
            sum_score = 0
        print(chosen_grid_parts_computer)
        print(chosen_grid_parts_player)
        print(chosen_grid_parts_computer2)
        print(chosen_grid_parts_player2)
        if max_score_computer > max_score_player or max_score_computer == max_score_player and max_score_computer != 0 and len(chosen_grid_parts_computer2) != 0:
            for item in chosen_grid_parts_computer2:
                if item in chosen_grid_parts_player2:
                    chosen_grid_parts.append(item)
            if len(chosen_grid_parts) != 0:
                chosen_grid_part = r.choice(chosen_grid_parts)
            elif len(chosen_grid_parts) == 0:
                chosen_grid_part = r.choice(chosen_grid_parts_computer2)
        elif max_score_player > max_score_computer and len(chosen_grid_parts_player2) != 0:
            for item in chosen_grid_parts_player2:
                if item in chosen_grid_parts_computer2:
                    chosen_grid_parts.append(item)
            if len(chosen_grid_parts) != 0:
                chosen_grid_part = r.choice(chosen_grid_parts)
            elif len(chosen_grid_parts) == 0:
                chosen_grid_part = r.choice(chosen_grid_parts_player2)
        elif max_score_computer == max_score_player and max_score_computer == 0 and len(chosen_grid_parts_computer2) != 0:
            chosen_grid_part = r.choice(chosen_grid_parts_computer2)
        else:
            chosen_grid_part = random_grid_part
    write_score = True
    drawXO(coordinates_grid(chosen_grid_part[0], chosen_grid_part[1], 'grid -> coordinates')[0], coordinates_grid(chosen_grid_part[0], chosen_grid_part[1], 'grid -> coordinates')[1])
    
def drawXO(x, y):
    global positionsO
    global positionsX
    global allpositions
    global playerside
    global control_turn
    if abs(x - width_height / 2) <= width_height / 2 and abs(y - width_height / 2) <= width_height / 2:
        middlepoint(x, y)
        x = t.position()[0]
        y = t.position()[1]
        if coordinates_grid(x, y, 'coordinates -> grid') not in allpositions:
            if game_mode == 1 or game_mode == 3:        
                if control_turn == 'player':
                    control_turn = 'computer'
                elif control_turn == 'computer':
                    control_turn = 'player'
            if playerside % 2 == 0:
                t.color('blue')
                O(0.49 * width_height / n)
                playerside = playerside + 1
                positionsO.append(coordinates_grid(x, y, 'coordinates -> grid'))
            else:
                t.color('red')
                X(0.7 * width_height / n)
                playerside = playerside + 1
                positionsX.append(coordinates_grid(x, y, 'coordinates -> grid'))
            allpositions = positionsO + positionsX
            scoreXO()
            turn()

def scoreXO():
    global score
    positions = ((playerside + 1) % 2) * positionsX + (playerside % 2) * positionsO
    try:
        if [positions[-1][0], positions[-1][1] + 1] in positions and [positions[-1][0], positions[-1][1] + 2] in positions:
            score[playerside % 2] = score[playerside % 2] + 1
        if [positions[-1][0], positions[-1][1] - 1] in positions and [positions[-1][0], positions[-1][1] - 2] in positions:
            score[playerside % 2] = score[playerside % 2] + 1
        if [positions[-1][0] + 1, positions[-1][1]] in positions and [positions[-1][0] + 2, positions[-1][1]] in positions:
            score[playerside % 2] = score[playerside % 2] + 1
        if [positions[-1][0] - 1, positions[-1][1]] in positions and [positions[-1][0] - 2, positions[-1][1]] in positions:
            score[playerside % 2] = score[playerside % 2] + 1
        if [positions[-1][0] - 1, positions[-1][1]] in positions and [positions[-1][0] + 1, positions[-1][1]] in positions:
            score[playerside % 2] = score[playerside % 2] + 1 
        if [positions[-1][0], positions[-1][1] - 1] in positions and [positions[-1][0], positions[-1][1] + 1] in positions:
            score[playerside % 2] = score[playerside % 2] + 1 
        if [positions[-1][0] + 1, positions[-1][1] + 1] in positions and [positions[-1][0] + 2, positions[-1][1] + 2] in positions:
            score[playerside % 2] = score[playerside % 2] + 1 
        if [positions[-1][0] - 1, positions[-1][1] - 1] in positions and [positions[-1][0] - 2, positions[-1][1] - 2] in positions:
            score[playerside % 2] = score[playerside % 2] + 1 
        if [positions[-1][0] - 1, positions[-1][1] + 1] in positions and [positions[-1][0] - 2, positions[-1][1] + 2] in positions:
            score[playerside % 2] = score[playerside % 2] + 1 
        if [positions[-1][0] + 1, positions[-1][1] - 1] in positions and [positions[-1][0] + 2, positions[-1][1] - 2] in positions:
            score[playerside % 2] = score[playerside % 2] + 1 
        if [positions[-1][0] - 1, positions[-1][1] - 1] in positions and [positions[-1][0] + 1, positions[-1][1] + 1] in positions:
            score[playerside % 2] = score[playerside % 2] + 1 
        if [positions[-1][0] - 1, positions[-1][1] + 1] in positions and [positions[-1][0] + 1, positions[-1][1] - 1] in positions:
            score[playerside % 2] = score[playerside % 2] + 1
    except:
        pass
    if write_score == True:
        t.goto(width_height + 15 + (scores_place - 15) / 2, width_height * (((playerside + 1) % 2) * 4 + (playerside % 2) * 7) / 10)
        t.dot(150 * width_height / 600, ((playerside + 1) % 2) * 'red' + (playerside % 2) * 'blue')
        t.color('white')
        t.write('{}'.format(score[playerside % 2]), move = False, align = 'center', font = 'Calibri {}'.format(int(30 * width_height / 600)))
    if len(allpositions) == n**2:
        t.penup()
        t.goto(width_height / 5, width_height / 5)
        t.color('black')
        t.pendown()
        for i in range(2):
            t.begin_fill()
            for i in range(4):
                t.forward(width_height * 3 / 5)
                t.right(90)
            t.end_fill()
        t.penup()
        t.goto(width_height / 2, width_height * 3 / 10)
        t.color('brown')
        if score[0] > score[1]:
            t.write('Player x\nwins!', move = False, align = 'center', font = 'Calibri {}'.format(int(70 * width_height / 600)))
        elif score[1] > score[0]:
            t.write('Player ▢\nwins!', move = False, align = 'center', font = 'Calibri {}'.format(int(70 * width_height / 600)))
        elif score[0] == score[1]:
            t.write("It's a\ndraw!", move = False, align = 'center', font = 'Calibri {}'.format(int(70 * width_height / 600)))

def control_click(x, y):
    if control_turn == 'player':
        drawXO(x, y)
    elif control_turn == 'computer':
        pass

def computers_only(eventx = None, eventy = None):
    global control_turn
    global control_score
    global playerside
    global positions_computer
    global positions_player
    for i in range(n ** 2):
        control_turn = 'computer'
        if positions_computer == positionsX:
            positions_computer = positionsO
            positions_player = positionsX
        elif positions_computer == positionsO:
            positions_computer = positionsX
            positions_player = positionsO
        control_score = (control_score + 1) % 2
        turn()
        
def play_again(eventx = None, eventy = None):
    new_game = t.textinput('New game', "Do you want to play again? (type 'yes' or press Enter to start a new game)")
    if new_game == 'yes' or new_game == '':
        t.clear()
        start_moves()

start_moves()
screen.onscreenclick(control_click, 1)
screen.onscreenclick(computers_only, 2)
screen.onscreenclick(play_again, 3)
screen.listen()
screen.mainloop()