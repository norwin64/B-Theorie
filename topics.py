import pygame
import os
import Button
import startscreen
import query
import database

pygame.init()
pygame.font.init()

#Main root
FPS = 60
WIDTH, HEIGHT = 1400, 800
root = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Topics")

#text
text = pygame.font.SysFont("comicsans", 80)


BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Include", "image_untergrund_start.png")), (WIDTH, HEIGHT))
RETURN_TO_HOME = text.render("Home", True, (30, 30, 30))
HOME_BUTTON = Button.Button(80, 0, RETURN_TO_HOME, 1/2)

START_BACK = pygame.image.load(os.path.join("Include", "Start_Back.png"))
START_BUTTON = Button.Button(WIDTH-550, HEIGHT-330, START_BACK, 0.7)

ARROW_CHOSEN = pygame.font.SysFont("comicsans", 100).render("->", True, (30, 30, 30))

LUFTRECHT = text.render("Luftrecht", True, (30, 30, 30))
LUFTRECHT_BUTTON = Button.Button(130, 100, LUFTRECHT,1)

METEOROLOGIE = text.render("Meteorologie", True, (30, 30, 30))
METEOROLOGIE_BUTTON = Button.Button(130, 300, METEOROLOGIE, 1)

NAVIGATION = text.render("Navigation", True, (30, 30, 30))
NAVIGATION_BUTTON = Button.Button(130, 500, NAVIGATION, 1)



WRONG = text.render("Wrong answers", True, (30, 30, 30))
WRONG_BUTTON = Button.Button(750, 200, WRONG, 1)

def show_window():
    root.blit(BACKGROUND, (0, 0))
    if HOME_BUTTON.draw(root):
        startscreen.main()
        quit()

    if START_BUTTON.draw(root):
        query.main()
        quit()

    if query.MODUS == 4.1:
        root.blit(ARROW_CHOSEN, (40, 90))
    elif query.MODUS == 4.2:
        root.blit(ARROW_CHOSEN, (40, 290))
    elif query.MODUS == 4.3:
        root.blit(ARROW_CHOSEN, (40, 490))
    elif query.MODUS == 6:
        root.blit(ARROW_CHOSEN, (660, 190))

    if LUFTRECHT_BUTTON.draw(root):
        database.update_id_luftrecht()
        startscreen.button_chosen(4.1)
    if METEOROLOGIE_BUTTON.draw(root):
        database.update_id_meteorologie()
        startscreen.button_chosen(4.2)
    if NAVIGATION_BUTTON.draw(root):
        database.update_id_navigation()
        startscreen.button_chosen(4.3)

    if WRONG_BUTTON.draw(root):
        database.update_id_wrong()
        startscreen.button_chosen(6)

    if database.wrong_answers == []:
        root.blit(pygame.font.SysFont("comicsans", 25).render("(Keine falsch beantworteten Fragen übrig)", True, (0, 0, 0)),(800,  310))

    pygame.display.update()

def quit():
    startscreen.main()
    pygame.display.quit()


def main():
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