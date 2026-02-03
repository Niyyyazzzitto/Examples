i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i <= 100:
    if i % 7 == 0:
        print("Первое кратное 7:", i)
        break
    i += 1

while True:
    pwd = input("Пароль: ")
    if pwd == "1234":
        print("Ок")
        break
    print("Неверно")

nums = [3, 8, 7, 10, 1]
s = 0
i = 0
while i < len(nums):
    s += nums[i]
    if s > 20:
        break
    i += 1
print("Сумма:", s)

text = "hello world"
target = "w"
i = 0
while i < len(text):
    if text[i] == target:
        print("Найдено на позиции:", i)
        break
    i += 1
