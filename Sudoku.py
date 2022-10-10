import pygame
import math
import random
import time
pygame.init()

#Veriables
font = pygame.font.SysFont("comicsansms", 36)
button_font = pygame.font.SysFont("MV Boli", 34)
end_game_font = pygame.font.SysFont("MV Boli", 65)
Title_font = pygame.font.SysFont("Fixedsys", 150)
Pregame = True
Ingame = False
Endgame = False
level = []

#Window
window = pygame.display.set_mode((450, 500))
pygame.display.set_caption('Sudoku')

button = pygame.image.load(r'C:\Users\ruanl\OneDrive\Pictures\Coding\Sudoku\Layer 1.png')

#Functions

def time_convert(sec):
    global time_lap
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    time_lap = str("{0}:{1}:{2}".format(int(hours),int(mins),int(sec)))
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))

def mouse_pos():
    MouseX, MouseY = pygame.mouse.get_pos()
    mouse_gridX = (math.floor(MouseX/50))*50
    mouse_gridY = (math.floor(MouseY/50))*50
    pygame.draw.rect(window, (150,150,150), (mouse_gridX+1, mouse_gridY+51, 48, 48))

def update():
    window.fill(0)
    #Grid
    for i in range(0,len(level)):
        if level[i] != ' ':
            super_grid[i] = level[i]
    for i in range(0, 9):
        for j in range(0, 9):
            pygame.draw.rect(window, (89,156,151), (i*50+1, j*50+51, 48, 48))
            display_number = font.render(super_grid[j*9+i],True,(0,0,50))
            window.blit(display_number,(i*50+14, j*50-2+50))
    pygame.draw.rect(window, (0,0,0), (148, 50, 4, 450))
    pygame.draw.rect(window, (0,0,0), (298, 50, 4, 450))
    pygame.draw.rect(window, (0,0,0), (0, 198, 450, 4))
    pygame.draw.rect(window, (0,0,0), (0, 348, 450, 4))

def in_game_buttons():
    button_1 = pygame.transform.scale(button, (148, 48))
    MouseX, MouseY = pygame.mouse.get_pos()
    window.blit(button_1, (1, 1, 148, 48))
    window.blit(button_1, (151, 1, 148, 48))
    window.blit(button_1, (301, 1, 148, 48))
    home_button = button_font.render("Home",True,(0,0,50))
    restart_button = button_font.render("Restart",True,(0,0,50))
    solve_button = button_font.render("Done",True,(0,0,50))
    window.blit(home_button,(30,-2))
    window.blit(restart_button,(162,-2))
    window.blit(solve_button,(330,-2))

def ingame_mouse_pressed():
    global Pregame
    global Ingame
    global level
    MouseX, MouseY = pygame.mouse.get_pos()
    if MouseX > 1 and MouseX < 149 and MouseY > 1 and MouseY < 49:
        Pregame = True
        Ingame = False
        for i in range(0,len(super_grid)):
            super_grid[i] = ' '
    if MouseX > 151 and MouseX < 299 and MouseY > 1 and MouseY < 49:
        for i in range(0,len(level)):
            super_grid[i] = level[i]
    if MouseX > 301 and MouseX < 449 and MouseY > 1 and MouseY < 49:
        check_numbers()
def pregame_buttons():
    button_1 = pygame.transform.scale(button, (200, 50))
    window.fill((0,0,50))
    title = Title_font.render("Sudoku",True,(255,255,255))
    easy_button = button_font.render("Easy",True,(0,0,50))
    medium_button = button_font.render("Medium",True,(0,0,50))
    hard_button = button_font.render("Hard",True,(0,0,50))
    impossible_button = button_font.render("Impossible",True,(0,0,50))
    window.blit(button_1, (125, 127, 150, 50))
    window.blit(button_1, (125, 214, 150, 50))
    window.blit(button_1, (125, 301, 150, 50))
    window.blit(button_1, (125, 388, 150, 50))
    window.blit(easy_button,(190, 125))
    window.blit(medium_button,(163, 212))
    window.blit(hard_button,(190, 299))
    window.blit(impossible_button,(145, 386))
    window.blit(title,(32,0))

def pregame_mouse_pressed():
    global Pregame
    global Ingame
    global level
    global start_time
    MouseX, MouseY = pygame.mouse.get_pos()
    if MouseX > 125 and MouseX < 275 and MouseY > 127 and MouseY < 177:
        Pregame = False
        Ingame = True
        level = easy[random.randint(0,len(easy)-1)]
        start_time = time.time()
    if MouseX > 125 and MouseX < 275 and MouseY > 214 and MouseY < 264:
        Pregame = False
        Ingame = True
        level = medium[random.randint(0,len(medium)-1)]
        start_time = time.time()
    if MouseX > 125 and MouseX < 275 and MouseY > 301 and MouseY < 351:
        Pregame = False
        Ingame = True
        level = hard[random.randint(0,len(hard)-1)]
        start_time = time.time()
    if MouseX > 125 and MouseX < 275 and MouseY > 388 and MouseY < 438:
        Pregame = False
        Ingame = True
        level = impossible[random.randint(0,len(impossible)-1)]
        start_time = time.time()

def check_numbers():
    for i in range(0,9):
        for j in range(0,9):
            for n in range(0,(9-j)):
                if super_grid[(i*9+j)] != ' ':
                    number = (i*9+j)
                    next_in_colomb = (i*9+j+n)
                    if number != next_in_colomb:
                        if super_grid[number] == super_grid[next_in_colomb]:
                            print(number, next_in_colomb)
                            super_grid[number] = ' '
                            super_grid[next_in_colomb] = ' '
            for m in range(0,(9-i)):
                if super_grid[(i*9+j)] != ' ':
                    number = (i*9+j)
                    next_in_row = (i*9+j+m*9)
                    if number != next_in_row:
                        if super_grid[number] == super_grid[next_in_row]:
                            print(number, next_in_row)
                            super_grid[number] = ' '
                            super_grid[next_in_row] = ' '
    for i in range(0,3):
        for j in range(0,3):
            for n in range(0,3):
                for m in range(0,3):
                    number = (m+n*9+j*3+i*27)
                    if super_grid[number] != ' ':
                        for b in range(0,(3)):
                            for p in range(0,(3)):
                                numbers_in_block = (p+b*9+j*3+i*27)
                                if number != numbers_in_block:
                                    if super_grid[number] == super_grid[numbers_in_block]:
                                        print(number, numbers_in_block)
                                        super_grid[number] = ' '
                                        super_grid[numbers_in_block] = ' '
    j = 0
    for i in range(0,len(super_grid)):
        if super_grid[i] != ' ':
            j += 1
    if j == len(super_grid):
        global Ingame
        global Endgame
        global end_time
        Endgame = True
        Ingame = False
        end_time = time.time()
        time_lapsed = end_time - start_time
        time_convert(time_lapsed)

def endgame_buttons():
    window.fill((0,0,50))
    button_1 = pygame.transform.scale(button, (200, 100))
    button_2 = pygame.transform.scale(button, (200, 50))
    title_1 = Title_font.render("Well",True,(255,255,255))
    title_2 = Title_font.render("Done!",True,(255,255,255))
    home_button = end_game_font.render("Home",True,(0,0,50))
    time_button = button_font.render(time_lap,True,(0,0,50))
    window.blit(button_1,(120,300))
    window.blit(button_2,(120,410))
    window.blit(home_button,(135,295))
    window.blit(time_button,(140,408))
    window.blit(title_1,(120,0))
    window.blit(title_2,(82,100))

def endgame_mouse_pressed():
    global Pregame
    global Endgame
    MouseX, MouseY = pygame.mouse.get_pos()
    if MouseX > 120 and MouseX < 320 and MouseY > 300 and MouseY < 400:
        Pregame = True
        Endgame = False
        for i in range(0,len(super_grid)):
            super_grid[i] = ' '
    
#Sudoku grids
super_grid =[" "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," ",
             " "," "," "," "," "," "," "," "," "]

#Easy
e_level_1 =[" ","6"," ", "3"," "," ", "8"," ","4",
            "5","3","7", " ","9"," ", " "," "," ",
            " ","4"," ", " "," ","6", "3"," ","7",
            
            " ","9"," ", " ","5","1", "2","3","8",
            " "," "," ", " "," "," ", " "," "," ",
            "7","1","3", "6","2"," ", " ","4"," ",
            
            "3"," ","6", "4"," "," ", " ","1"," ",
            " "," "," ", " ","6"," ", "5","2","3",
            "1"," ","2", " "," ","9", " ","8"," "]

#medium
m_level_1 =[" ","3"," ", "7"," ","8", " "," "," ",
            " "," "," ", " "," "," ", "2"," "," ",
            " "," ","4", " "," "," ", " ","7","1",
            
            "6"," ","1", " "," "," ", " "," ","2",
            "7"," "," ", " "," ","5", " "," "," ",
            " "," "," ", " "," "," ", "8","5"," ",
            
            " "," ","3", " ","8"," ", " "," "," ",
            "9","2"," ", " ","6"," ", " "," ","5",
            "1"," "," ", " "," "," ", "9"," ","6"]

#Hard
h_level_1 =[" "," "," ", " "," "," ", " "," "," ",
            " "," "," ", " "," ","3", " ","8","5",
            " "," ","1", " ","2"," ", " "," "," ",
            
            " "," "," ", "5"," ","7", " "," "," ",
            " "," ","4", " "," "," ", "1"," "," ",
            " ","9"," ", " "," "," ", " "," "," ",
            
            "5"," "," ", " "," "," ", " ","7","3",
            " "," ","2", " ","1"," ", " "," "," ",
            " "," "," ", " ","4"," ", " "," ","9"]

#Impossible
i_level_1 =[" "," "," ", "7"," "," ", " "," "," ",
            "1"," "," ", " "," "," ", " "," "," ",
            " "," "," ", "4","3"," ", "2"," "," ",
            
            " "," "," ", " "," "," ", " "," ","6",
            " "," "," ", "5"," ","9", " "," "," ",
            " "," "," ", " "," "," ", "4","1","8",
            
            " "," "," ", " ","8","1", " "," "," ",
            " "," ","2", " "," "," ", " ","5"," ",
            " ","4"," ", " "," "," ", "3"," "," "]

#Sudoku Levels
easy = [e_level_1]
medium = [m_level_1]
hard = [h_level_1]
impossible = [i_level_1]

#Number Functions
def number_1():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '1'
def number_2():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '2'
def number_3():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '3'
def number_4():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '4'
def number_5():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '5'
def number_6():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '6'
def number_7():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '7'
def number_8():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '8'
def number_9():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = '9'
def number_0():
    grid_numberX, grid_numberY = pygame.mouse.get_pos()
    grid_number = ((math.floor(grid_numberX/50))+((math.floor((grid_numberY-50)/50))*9))
    super_grid[grid_number] = ' '

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if Pregame:
            if pygame.mouse.get_pressed() == (True,False,False):
                pregame_mouse_pressed()
        if Ingame:
            if pygame.mouse.get_pressed() == (True,False,False):
                ingame_mouse_pressed()
        if Endgame:
            if pygame.mouse.get_pressed() == (True,False,False):
                endgame_mouse_pressed()
        if event.type == pygame.KEYDOWN:
            if Ingame:
                if event.key == pygame.K_KP1:
                    number_1()
                if event.key == pygame.K_1:
                    number_1()
                if event.key == pygame.K_KP2:
                    number_2()
                if event.key == pygame.K_2:
                    number_2()
                if event.key == pygame.K_KP3:
                    number_3()
                if event.key == pygame.K_3:
                    number_3()
                if event.key == pygame.K_KP4:
                    number_4()
                if event.key == pygame.K_4:
                    number_4()
                if event.key == pygame.K_KP5:
                    number_5()
                if event.key == pygame.K_5:
                    number_5()
                if event.key == pygame.K_KP6:
                    number_6()
                if event.key == pygame.K_6:
                    number_6()
                if event.key == pygame.K_KP7:
                    number_7()
                if event.key == pygame.K_7:
                    number_7()
                if event.key == pygame.K_KP8:
                    number_8()
                if event.key == pygame.K_8:
                    number_8()
                if event.key == pygame.K_KP9:
                    number_9()
                if event.key == pygame.K_9:
                    number_9()
                if event.key == pygame.K_KP0:
                    number_0()
                if event.key == pygame.K_0:
                    number_0()

    if Ingame:
        update()
        in_game_buttons()
    if Pregame:
        pregame_buttons()
    if Endgame:
        endgame_buttons()
    #mouse_pos()
    pygame.display.update()

pygame.quit()
