import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

result = random.randint(0,1)
if result == 0:
    print("Tails")
else:
    print("Heads")