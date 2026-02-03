for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

words = ["hi", "", "ok", "", "bye"]
for w in words:
    if w == "":
        continue
    print(w)

nums = [3, -1, 0, 5, -2]
for x in nums:
    if x <= 0:
        continue
    print(x)

text = "banana"
for ch in text:
    if ch == "a":
        continue
    print(ch)

for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
