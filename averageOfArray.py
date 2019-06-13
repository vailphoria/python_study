n = int(input())
stri = ""
for j in range(n):
    a = list(map(int, input().split()))
    avg = 0
    for i in range(len(a)):
        avg += a[i]
    avg /= len(a)-1
    if avg%1 >= 0.5:
        avg = int(avg)+1
    else:
        avg = int(avg)
    stri += str(avg) + " "
print(stri)