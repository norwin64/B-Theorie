import pygame
import os
import blit_text
import database
import Button
import results
import datetime
import time
import startscreen
pygame.init()

WIDTH, HEIGHT = 1400, 800
root = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Prüfungssimulation")
FPS = 60

ICON_SIZE = 70

font_question = pygame.font.SysFont("Verdana", 24)

GREEN = (100, 250, 150)
BLACK = (50, 50, 50)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Include", "sim_back.png")), (WIDTH, HEIGHT))
ICON = pygame.transform.scale(pygame.image.load(os.path.join("Include", "startbutton.png")), (ICON_SIZE, ICON_SIZE))
QUESTION_BACK = pygame.Rect(0, 40, WIDTH, 200)

field_1 = (20, 250)
field_2 = (20, 400)
field_3 = (20, 550)
field_4 = (20, 700)
FIELD = pygame.image.load(os.path.join("Include", "Field.png"))
FIELD_WRONG = pygame.image.load(os.path.join("Include", "Field_wrong.png"))
FIELD_RIGHT = pygame.image.load(os.path.join("Include", "Field_right.png"))
B1_Button = Button.Button(40, 260, FIELD, 0.5)
B2_Button = Button.Button(40, 410, FIELD, 0.5)
B3_Button = Button.Button(40, 560, FIELD, 0.5)
B4_Button = Button.Button(40, 710, FIELD, 0.5)

CANC = pygame.image.load(os.path.join("Include", "canc.png"))
cancilation_button = Button.Button(840, HEIGHT-120, CANC, 1)

correct_luftrecht = 0
correct_meteorologie = 0
correct_navigation = 0
question = 1
wrong = []
starttime = int(time.time())
endtime = int(starttime + 5400)

def show_window():
    check_time()
    root.blit(BACKGROUND, (0, 0))
    root.blit(ICON, (WIDTH - ICON_SIZE - 10, HEIGHT - ICON_SIZE - 10))

    pygame.draw.rect(root, GREEN, pygame.Rect(5, 10, 200, 40))
    root.blit(font_question.render(database.subject(), True, BLACK), (10, 10))
    root.blit(font_question.render(str(question) + "/120", True, (150, 150, 150)), (WIDTH/2-50, 3))

    root.blit(font_question.render(str(time_left) + " min übrig", True, (150, 150, 150)), (WIDTH-180, 10))

    root.blit(font_question.render(str(datetime.datetime.now().hour).zfill(2) + ":" + str(datetime.datetime.now().minute).zfill(2) + " Uhr", True, (150, 150, 150)), (WIDTH-210, HEIGHT-50))

    pygame.draw.rect(root, GREEN, QUESTION_BACK)
    blit_text.blit_text(root, database.q[database.id], (10, 70), font_question, color=(0, 0, 0), border = 10)

    IMAGE_FIELD = pygame.image.load(os.path.join("Include", database.image[database.id] + ".PNG"))
    root.blit(IMAGE_FIELD, (WIDTH - 488, 250))

    if cancilation_button.draw(root):
        reset_sim()
        quit()

    blit_text.blit_text(root, database.a1[database.id], (80, 250), font_question, border=550)
    blit_text.blit_text(root, database.a2[database.id], (80, 400), font_question, border=550)
    blit_text.blit_text(root, database.a3[database.id], (80, 550), font_question, border=550)
    blit_text.blit_text(root, database.a4[database.id], (80, 700), font_question, border=550)

    if B1_Button.draw(root):
        test("1")
    if B2_Button.draw(root):
        test("2")
    if B3_Button.draw(root):
        test("3")
    if B4_Button.draw(root):
        test("4")

    pygame.display.update()

def test(Button):
    global correct_luftrecht
    global correct_meteorologie
    global correct_navigation
    global question
    global wrong
    if Button == database.ra[database.id]:
        if question <= 40:
            correct_luftrecht += 1
        elif question <= 80:
            correct_meteorologie += 1
        elif question <= 120:
            correct_navigation += 1
    else:
        wrong.append(database.id)
    question += 1
    if question <= 40:
        database.update_id_luftrecht()
    elif question <= 80:
        database.update_id_meteorologie()
    elif question <= 120:
        database.update_id_navigation()
    else:
        results.main(correct_luftrecht, correct_meteorologie, correct_navigation, wrong)
        quit()

def check_time():
    global time_left
    starttime = int(time.time())
    time_left = round((endtime-starttime)/60)
    if starttime == endtime:
        results.main(correct_luftrecht, correct_meteorologie, correct_navigation, wrong)
        quit()

def reset_sim():
    global correct_luftrecht
    global correct_meteorologie
    global correct_navigation
    global question
    global wrong
    global starttime
    global endtime
    correct_luftrecht = 0
    correct_meteorologie = 0
    correct_navigation = 0
    question = 1
    wrong = []
    starttime = int(time.time())
    endtime = int(starttime + 5400)

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