first = input("число первое: ")
second = input(("число второе: "))
third = input(("число третье: "))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else: print(0)