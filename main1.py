#zad.1
cub = [num ** 3 for num in range(1, 11)]
for cube in cub:
    if cube % 2 == 1:
        print(cube, end=" ")
print()
#zad.2
# Zadanie 1
# Lista sześcianów od 1 do 10
cubes = [n**3 for n in range(1, 11)]

# Wypisz tylko te, które są niepodzielne przez 2
for cube in cubes:
    if cube % 2 == 1:   # liczby nieparzyste
        print(cube)

print("-" * 30)

# Zadanie 2
lista = [2, 0, 0, 0, 1, 0, 0, 0, 0, 2, 3, 0, 0]
zeros = [x for x in lista if x == 0]
non_zeros = [x for x in lista if x != 0]

print("Zeros:", zeros)
print("Non-zeros:", non_zeros)
