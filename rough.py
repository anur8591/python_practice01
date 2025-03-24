i = 1
while i <= 50:
    print(i)
    i+=1

for i in range(0, 10):
    for j in range(i + 1):
        print("*", end="")
    print("\n")
for i in range(9, 0, -1):
    for j in range(i):
        print("*", end="")
    print("\n")


li = [1,2,3,4,5,6,7,8,9]
print(li[::-1])