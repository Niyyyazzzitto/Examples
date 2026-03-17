file = open("test.txt", "r")
print(file.read())
file.close()

file = open("test.txt", "r")
print(file.readline())
print(file.readline())
file.close()

file = open("test.txt", "r")
print(file.readlines())
file.close()