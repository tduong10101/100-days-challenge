import random

random.seed(input("Create a seed number: "))

nameAsCsv = input("Give me everybody's names, separated by a comma.\n")
names = nameAsCsv.split(", ")

numNames = len(names)

randIndex = random.randint(0,numNames - 1)

print(f"{names[randIndex]} is going to buy the meal today!")