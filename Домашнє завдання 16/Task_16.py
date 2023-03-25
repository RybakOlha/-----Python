import json

my_dict = {
    345643: ("Alice", 15),
    786547: ("Tracy", 16),
    376548: ("Serge", 40),
    345619: ("David", 20),
    456728: ("Michael", 35),
	 675489: ("Andrew", 19)
}

with open("my_dict.json", "w") as file:
    json.dump(my_dict, file)