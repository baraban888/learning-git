# Tworzymy listę liczb od 0 do 100
numbers = list(range(101))

# Wybieramy tylko te, które dzielą się przez 5
divisible_by_5 = [n for n in numbers if n % 5 == 0]

# Wypisujemy liczby podzielne przez 5
print("Liczby podzielne przez 5:")
print(", ".join(str(n) for n in divisible_by_5))

# Wypisujemy te same liczby podniesione do 3 potęgi
print("\nTe same liczby podniesione do 3 potęgi:")
print(", ".join(str(n**3) for n in divisible_by_5))
