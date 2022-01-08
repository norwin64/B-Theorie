import pygame
import os
import Button
import startscreen
import sim
import database
import query

pygame.init()
pygame.font.init()

#Main root
FPS = 60
WIDTH, HEIGHT = 1400, 800
root = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Topics")

#text
text = pygame.font.SysFont("comicsans", 60)
text2 = pygame.font.SysFont("comicsans", 66)
GREY = (200, 200, 200)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Include", "image_untergrund_start.png")), (WIDTH, HEIGHT))
RETURN_TO_HOME = text.render("Home", True, (30, 30, 30))
HOME_BUTTON = Button.Button(80, 0, RETURN_TO_HOME, 1/2)

RESULT_GREEN = pygame.transform.scale(pygame.image.load(os.path.join("Include", "result_green.png")), (900,250))
RESULT_RED = pygame.transform.scale(pygame.image.load(os.path.join("Include", "result_red.png")), (900,250))
SUCCESSFULL = pygame.image.load(os.path.join("Include", "99.png"))
FAILED = pygame.image.load(os.path.join("Include", "98.png"))
SEE_WRONG = Button.Button(WIDTH-400, HEIGHT-100, text.render("Fehler", True, (0, 0, 0)), 1 )
wrong = []

def show_window(l, m, n, w):
    bestanden = 0
    root.blit(BACKGROUND, (0, 0))
    if l >= 30:
        root.blit(RESULT_GREEN, (10, 50))
        bestanden += 1
    else:
        root.blit(RESULT_RED, (10, 50))
    if m >= 30:
        root.blit(RESULT_GREEN, (10, 230))
        bestanden += 1
    else:
        root.blit(RESULT_RED, (10, 230))
    if n >= 30:
        root.blit(RESULT_GREEN, (10, 410))
        bestanden += 1
    else:
        root.blit(RESULT_RED, (10, 410))

    root.blit(text.render("Luftrecht: " + str(40 - l) + " Fehler", True, GREY), (72, 122))
    root.blit(text.render("Meteorologie: " + str(40 - m) + " Fehler", True, GREY), (72, 302))
    root.blit(text.render("Navigation: " + str(40 - n) + " Fehler", True, GREY), (72, 482))
    root.blit(text.render("Insgesamt: " + str(120 - m - n - l) + " Fehler", True, GREY), (72, 652))

    root.blit(text.render("Luftrecht: " + str(40-l) + " Fehler", True, (0, 0, 0)), (70, 120))
    root.blit(text.render("Meteorologie: " + str(40-m) + " Fehler", True, (0, 0, 0)), (70, 300))
    root.blit(text.render("Navigation: " + str(40-n) + " Fehler", True, (0, 0, 0)), (70, 480))
    root.blit(text.render("Insgesamt: " + str(120-m-n-l) + " Fehler", True, (0, 0, 0)), (70, 650))


    if bestanden == 3:
        root.blit(text.render("Bestanden!", True, (0, 0, 0)), (1004, 74) )
        root.blit(text.render("Bestanden!", True, (0, 255, 0)), (1000, 70) )
        root.blit(SUCCESSFULL, (1000, 100))
    else:
        root.blit(text.render("Nicht Bestanden!", True, (0, 0, 0)), (904, 74))
        root.blit(text.render("Nicht Bestanden!", True, (255, 0, 0)), (900, 70))
        root.blit(FAILED, (1000, 130))

    #Button falsche Fragen
    if SEE_WRONG.draw(root):
        query.MODUS = 7
        database.id = wrong[0]
        query.main()
    pygame.display.update()


def quit():
    startscreen.main()
    pygame.display.quit()

def main(l, m, n, w):
    for element in w:
        wrong.append(element)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        show_window(l, m, n, w)
    quit()

if __name__ == "__main__":
    main()