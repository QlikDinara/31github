# This is a sample Python script.
import random

print("Choose 2 integer numbers for matrix dimensions. Type Q for quiting")

while True:
    try:
        n = (input())
        m = (input())
        if n == ("Q") or m == ("Q"):
            print("Quitting")
            break
        else:
            for i in range(int(n)):
                for j in range(int(m)):
                    print(random.randint(0, 1000), end=" ")
                print()
    except ValueError:
        print("Invalid")
        continue
