i = 1
while i <= 5:
    print(i)
    i += 1

n = 5
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(total)

sec = 5
while sec > 0:
    print(sec)
    sec -= 1
print("Старт!")

text = "go"
while text != "stop":
    text = input("Напиши stop чтобы выйти: ")
print("Выход")

n = 6
fact = 1
while n > 1:
    fact *= n
    n -= 1
print(fact)
