import csv
import random
import query
import results
random.seed()

file = open("daten.csv", newline="")
daten_csv = csv.DictReader(file, delimiter =";")

q = []
a1 = []
a2 = []
a3 = []
a4 = []
ra = []
image = []
topic = []
id = 0

wrong_answers = []

for item in daten_csv:
    q.append(item["question"])
    a1.append(item["a1"])
    a2.append(item["a2"])
    a3.append(item["a3"])
    a4.append(item["a4"])
    ra.append(item["ra"])
    image.append(item["image"])
    topic.append(item["topic"])
image_list = []
for element in range(len(image)):
    if image[element] > "0":
        image_list.append(element)

def update_id():
    global id
    id += 1

def update_id_random():
    global id
    id = random.randint(0, len(q))

def update_id_image():
    global id
    id = image_list[random.randint(0, len(image_list)-1)]
def update_id_luftrecht():
    global id
    id = random.randint(0, 115)
def update_id_navigation():
    global id
    id = random.randint(286, 404)
def update_id_meteorologie():
    global id
    id = random.randint(116, 285)

def update_id_wrong():
    global id
    try:
        id = wrong_answers[random.randint(0, len(wrong_answers)-1)]
    except ValueError:
        query.quit()

def update_id_wrong_sim():
    global id
    id = results.wrong[0]

def subject():
    if id < 116:
        return "Luftrecht: "
    elif id < 286:
        return "Meteorologie: "
    else:
        return "Navigation: "