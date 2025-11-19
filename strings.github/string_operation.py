a = str(input())
vow = "aeiou"
b = []
for i in a:
    if i in vow:
        i = "#"
    b += i
print("".join(b))