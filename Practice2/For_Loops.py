for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

nums = [1, 2, 3, 4]
total = 0
for x in nums:
    total += x
print(total)

names = ["Ann", "Bob", "Cory"]
for idx, name in enumerate(names, start=1):
    print(idx, name)

text = "hello"
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print(count)
