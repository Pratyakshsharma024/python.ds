a = str(input())
count = 0
for i in range(len(a)):
    if a[i:i+3] == "bob":
        count+=1
print(count)
        