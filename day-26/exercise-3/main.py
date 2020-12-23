with open("file1.txt") as file:
    data1 = file.readlines()
    data1 = [int(n.strip("\n")) for n in data1]

with open("file2.txt") as file:
    data2 = file.readlines()
    data2 = [int(n.strip("\n")) for n in data2]

result = [n for n in data1 if n in data2]
# Write your code above 👆

print(result)


