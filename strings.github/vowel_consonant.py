a = int(input())
vow = "AEIOUaeiou"
for i in range(a):
    i = input()
    v_count = 0
    c_count = 0
    for j in i:
        if j in vow:
            v_count+=1
        else:
            c_count+=1
    print(v_count, c_count)
    
