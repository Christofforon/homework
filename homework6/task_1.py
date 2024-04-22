
# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for num in numbers:
    if num % 2 == 0:
        print(num)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i+=1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(key, ':', value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in matrix:
    for item in sublist:
        print(item)

# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for num in range(1, 11):
    print("Number", num, "=",num)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
    print(index, value)

# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print('new punct: ')
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numere = [i for i in range(1,11)]
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
while numbers[0] < 50:
    for i in range(len(numbers)):
        numbers[i] *= 2

print(numbers)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
numere_patrat_perfect = [x ** 2 for x in range(1, 11)]
print(numere_patrat_perfect)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1,11):
    print(7 * i)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
perechi = [[i,j] for i in range(1,6) for j in range(1,6)]
print(perechi)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for i,j in perechi:
    if i < j: print(i, j)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
numere = (5, 6, 7, 4, 9, 8, 12, 22, 15, 16, 19, 30)
i = 0
while i < len(numere):
    if numere[i] > 10:
        print("Prima valoare mai mare decât 10 este:", numere[i],"pe pozitia:",i)
        break
    i += 1

# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
dimensiune = int(input("Introduceți dimensiunea pătratului: "))
i = 0
j = 0
while i < dimensiune:
    while j < dimensiune:
        print("*" * dimensiune)
        j += 1
        i += 1
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
dimensiune = int(input("Introduceți dimensiunea: "))
for i in range(1, dimensiune + 1):
    output = ""
    for j in range(1, i + 1):
        output += str(j)

    print(output)
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
dimensiune = int(input("Introduceți dimensiunea: "))
for i in range(dimensiune, 0 , -1):
    output = ""
    for j in range(i, 0, -1):
        output += str(j)
    
    print(output)    
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
s = "abcdefg"

for i in range(len(s)):
    print(s[i:])
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
dimensiune = int(input("Introduceți dimensiunea: "))
for i in range(dimensiune + 1):
    for j in range(dimensiune + 1):
        if (i + j) % 2 == 0:
            print("-", end="")
        else:
            print("+", end="")  
    print()  
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
dimensiune = int(input("Introduceți dimensiunea: "))
for i in range(dimensiune):
    for j in range(i + 1):
        print(3 ** (j + 1), end=" ")
    print()
for i in range(1, dimensiune):
    for j in range(dimensiune - i):
        print(3 ** (i + j + 1), end=" ")
    print()
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.