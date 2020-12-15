with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open("my_file.txt", mode="r") as file:
    content = file.read()
    print(content)