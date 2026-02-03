i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

lines = ["hi", "", "ok", "", "bye"]
i = 0
while i < len(lines):
    line = lines[i]
    i += 1
    if line == "":
        continue
    print(line)

nums = [5, -2, 3, -10, 4]
i = 0
s = 0
while i < len(nums):
    x = nums[i]
    i += 1
    if x < 0:
        continue
    s += x
print(s)

i = 0
while i < 15:
    i += 1
    if i % 3 == 0:
        continue
    print(i)

while True:
    s = input("Введите что-то (q для выхода): ").strip()
    if s == "":
        continue
    if s == "q":
        break
    print("Вы ввели:", s)

