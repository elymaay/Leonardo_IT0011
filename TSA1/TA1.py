
print("Pattern a:")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")  
    for k in range(1, i + 1):
        print(k, end="")  
    print()  


print("\nPattern b:")
i = 1
while i <= 7:
    if i % 2 != 0:  
        for j in range(i):
            print(i, end="")  
        print()  
    i += 1
