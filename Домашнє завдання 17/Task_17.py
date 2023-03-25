import json
import csv
import random

with open("my_dict.json", "r") as file:
    my_dict = json.load(file)

operators = ['095', '066', '098', '096', '050', '097']

rows = []

for key, value in my_dict.items():
    name = value[0]
    age = value[1]
    if random.random() < 0.75:
        phone = random.choice(operators) + str(random.randint(0, 9999999)).zfill(7)
    else:
        phone = ""
    rows.append([key, name, age, phone])

with open("my_csv.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Имя", "Возраст", "Телефон"])
    writer.writerows(rows)