import pygame
import pygame_menu
import os
import Button
import query
import database
import topics
import sim
import datetime

#Init
pygame.init()
pygame.font.init()

#Main root
WIDTH, HEIGHT = 1420, 800
ICON_SIZE = 70
root = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("B Schein Abfrageprogramm")
FPS = 60


#colour
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE  =("#e4622a")

#root Design
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Include", "image_untergrund_start.png")), (WIDTH, HEIGHT))
ICON = pygame.transform.scale(pygame.image.load(os.path.join("Include", "startbutton.png")), (ICON_SIZE, ICON_SIZE))

#start
START_BACK = pygame.image.load(os.path.join("Include", "Start_Back.png"))
START_BUTTON = Button.Button(800, HEIGHT/2-100, START_BACK, 1)

#Menu
ARROW_CHOSEN = pygame.font.SysFont("comicsans", 70).render("->", True, BLACK)

LBO = pygame.font.SysFont("comicsans", 70).render("Learn by order", True, BLACK)
LBO_BUTTON = Button.Button(130, 100, LBO, 1)

LR = pygame.font.SysFont("comicsans", 70).render("Learn random", True, BLACK)
LR_BUTTON = Button.Button(130, 220, LR, 1)

IQ = pygame.font.SysFont("comicsans", 70).render("Bildfragen", True, BLACK)
IQ_BUTTON = Button.Button(130, 340, IQ, 1)

LBT = pygame.font.SysFont("comicsans", 68).render("Fragenauswahl", True, (50, 50, 50))
LBT_BUTTON = Button.Button(130, 460, LBT, 1)

ES = pygame.font.SysFont("comicsans", 70).render("Prüfungssimulation", True, BLACK)
ES_BUTTON = Button.Button(130, 580, ES, 1)

def button_chosen(a):
    global MODUS
    query.MODUS = a


def show_window():
    #root design
    root.blit(BACKGROUND, (0, 0))
    root.blit(ICON, (WIDTH - ICON_SIZE - 10, HEIGHT - ICON_SIZE - 10))
    root.blit(pygame.font.SysFont("Verdana", 24).render(str(datetime.datetime.now().hour).zfill(2) + ":" + str(datetime.datetime.now().minute).zfill(2) + " Uhr", True, (150, 150, 150)), (WIDTH-210, HEIGHT-50))

    #Menu
    if query.MODUS == 1:
        database.id = 0
        root.blit(ARROW_CHOSEN, (60, 100))
    elif query.MODUS == 2:
        root.blit(ARROW_CHOSEN, (60, 220))
    elif query.MODUS == 3:
        root.blit(ARROW_CHOSEN, (60, 340))
    elif query.MODUS == 4:
        root.blit(ARROW_CHOSEN, (60, 460))
    elif query.MODUS == 5:
        root.blit(ARROW_CHOSEN, (60, 580))

    if START_BUTTON.draw(root):
        if query.MODUS != 5:
            query.main()
            quit()
        else:
            sim.main()
            quit()

    if LBO_BUTTON.draw(root):
        button_chosen(1)
    if LR_BUTTON.draw(root):
        database.id = database.random.randint(0,len(database.q))
        button_chosen(2)
    if IQ_BUTTON.draw(root):
        database.id = database.image_list[database.random.randint(0, len(database.image_list) - 1)]
        button_chosen(3)
    if LBT_BUTTON.draw(root):
        topics.main()
    if ES_BUTTON.draw(root):
        database.id = database.random.randint(0,115)
        button_chosen(5)


    pygame.display.update()

def import_data():
    my_file = open("Wrong.txt", "r")
    lines = my_file.read().split(" ")

    for line in lines:
        try:
            database.wrong_answers.append(int(line))
        except:
            pass

def quit():
    pygame.display.quit()
    exit()

def main():
    import_data()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        show_window()
    quit()

if __name__ == "__main__":
    main()
