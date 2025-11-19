a = int(input())
for i in range(a):
    i = str(input())
    if i == i[::-1]:
        print(1)
    else:
        print(0)
        