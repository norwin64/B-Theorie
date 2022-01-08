import pygame
import os
import blit_text
import time
import database
import Button
import startscreen
import topics
import results


#Init
pygame.init()
pygame.font.init()


#colour
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREY = (180, 180, 180)
BLUE = (150, 240, 255)

#text
font_question = pygame.font.SysFont("Sans Serif", 45)
font = pygame.font.SysFont("Sans Serif", 38)
font_header = pygame.font.SysFont("comicsans", 38)
font_topic = pygame.font.SysFont("comicsans", 28)
HEIGHT_QUESTION = 280

#Main root
FPS = 60
WIDTH, HEIGHT = 1400, 800
root = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Learn")
MODUS = 1



#root design
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Include", "image_untergrund_start.png")), (WIDTH, HEIGHT))

#Header
RETURN_TO_HOME = font_header.render("Home", True, (30, 30, 30))
HOME_BUTTON = Button.Button(80, 0, RETURN_TO_HOME, 1)
TOPIC_BACK = pygame.Rect(200, 0, 1000, 60)
BUTTON_TOPICS = Button.Button(WIDTH-200, 0, font_header.render("Fragenauswahl", True, (30, 30, 30)), 0.7)


#Question
QUESTION_BACK = pygame.Rect(0, 60, WIDTH, HEIGHT_QUESTION-100)
ARROW = pygame.image.load(os.path.join("Include", "Pfeil.png"))

#Field with all answers
field_1 = (20, 250)
field_2 = (20, 400)
field_3 = (20, 550)
field_4 = (20, 700)
FIELD = pygame.image.load(os.path.join("Include", "Field.png"))
FIELD_WRONG = pygame.image.load(os.path.join("Include", "Field_wrong.png"))
FIELD_RIGHT = pygame.image.load(os.path.join("Include", "Field_right.png"))
B1_Button = Button.Button(20, 250, FIELD, 0.8)
B2_Button = Button.Button(20, 400, FIELD, 0.8)
B3_Button = Button.Button(20, 550, FIELD, 0.8)
B4_Button = Button.Button(20, 700, FIELD, 0.8)

#Return Answer is True/False
RETURN_TRUE = pygame.image.load(os.path.join("Include", "True.png"))
RETURN_FALSE = pygame.image.load(os.path.join("Include", "False.png"))





def show_window():
    #root design
    root.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(root, GREY, TOPIC_BACK)
    pygame.draw.rect(root, BLACK, QUESTION_BACK)
    root.blit(ARROW, (0, 60))
    pygame.draw.rect(root, GREY, pygame.Rect(WIDTH - 500, 250, 10, HEIGHT - 260))

    #header
    if HOME_BUTTON.draw(root):
        startscreen.main()
        pygame.quit()
    root.blit(font_topic.render(database.subject() + database.topic[database.id], True, WHITE), (220, 10))
    if MODUS == 1 or MODUS == 4.1 or MODUS == 4.2 or MODUS == 4.3 or MODUS == 6 :
        if BUTTON_TOPICS.draw(root):
            topics.main()
    if MODUS == 6:
        root.blit(font_topic.render(str(len(database.wrong_answers)), True, BLACK), (WIDTH-100, 29))

    #question
    blit_text.blit_text(root, database.q[database.id], (70, 70), font_question, color=WHITE)
    SHOW_ID = font.render(str(database.id + 1), True, GREY)
    root.blit(SHOW_ID, (WIDTH - 50, 200))

    #image
    IMAGE_FIELD = pygame.image.load(os.path.join("Include", database.image[database.id] + ".PNG"))
    root.blit(IMAGE_FIELD, (WIDTH-488, 250))

    #answers
    blit_text.blit_text(root, database.a1[database.id], (80, 250), font, border=550)
    blit_text.blit_text(root, database.a2[database.id], (80, 400), font, border=550)
    blit_text.blit_text(root, database.a3[database.id], (80, 550), font, border=550)
    blit_text.blit_text(root, database.a4[database.id], (80, 700), font, border=550)

    if B1_Button.draw(root):
        test("1")
        time.sleep(1)
    if B2_Button.draw(root):
        test("2")
        time.sleep(1)
    if B3_Button.draw(root):
        test("3")
        time.sleep(1)
    if B4_Button.draw(root):
        test("4")
        time.sleep(1)


    pygame.display.update()

def test(Button):
    global wrong
    if Button == database.ra[database.id]:
        root.blit(RETURN_TRUE, (WIDTH-450, 600))
        root.blit(FIELD_WRONG, (20, 250))
        root.blit(FIELD_WRONG, (20, 400))
        root.blit(FIELD_WRONG, (20, 550))
        root.blit(FIELD_WRONG, (20, 700))
        input = eval("field_" + Button)
        root.blit(FIELD_RIGHT, (input))
        if MODUS == 1:
            database.update_id()
        elif MODUS == 2:
            database.update_id_random()
        elif MODUS == 3:
            database.update_id_image()
        elif MODUS == 4.1:
            database.update_id_luftrecht()
        elif MODUS == 4.2:
            database.update_id_meteorologie()
        elif MODUS == 4.3:
            database.update_id_navigation()
        elif MODUS == 6:
            try:
                database.wrong_answers.remove(database.id)
                database.update_id_wrong()
            except:
                database.wrong_answers.remove(0)
                quit() # show no more wrong questions window sceen
            update_wrong_answer()
        elif MODUS == 7:
            print(results.wrong)
            try:
                results.wrong.remove(database.id)
                database.update_id_wrong_sim()

                print(results.wrong)
            except:
                quit()  # show no more wrong questions window sceen


    else:
        root.blit(RETURN_FALSE, (WIDTH-450, 600))
        root.blit(FIELD_WRONG, (20, 250))
        root.blit(FIELD_WRONG, (20, 400))
        root.blit(FIELD_WRONG, (20, 550))
        root.blit(FIELD_WRONG, (20, 700))
        input = eval("field_" + database.ra[database.id])
        root.blit(FIELD_RIGHT, (input))
        database.wrong_answers.append(database.id)
        update_wrong_answer()
    pygame.display.update()

def update_wrong_answer():
    file = open("Wrong.txt", "w")
    for item in database.wrong_answers:
        file.write(" " + str(item))

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