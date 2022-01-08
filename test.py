my_file = open("Wrong.txt", "r")
lines = my_file.read().split(" ")

for line in lines:
    database.wrong_answers.append(int(line))

print(wrong_answers)