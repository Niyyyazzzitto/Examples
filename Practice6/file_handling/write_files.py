file = open("test.txt", "w")
file.write("Hello world")
file.close()

file = open("test.txt", "a")
file.write("\nNew line")
file.close()

file = open("newfile.txt", "x")
file.write("Created")
file.close()

with open("test.txt", "r") as file:
    print(file.read())