for i in range(1, 10):
    if i == 5:
        break
    print(i)

nums = [7, 9, 11, 4, 6]
for x in nums:
    if x % 2 == 0:
        print("Первое чётное:", x)
        break

items = ["cat", "dog", "fish"]
target = "dog"
for item in items:
    if item == target:
        print("Найдено!")
        break

for _ in range(100):
    s = input("Введите stop чтобы закончить: ")
    if s == "stop":
        break

nums = [2, 4, 3, 5, 1]
s = 0
for x in nums:
    s += x
    if s > 10:
        break
print("Сумма:", s)

