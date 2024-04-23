# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
arr=[]
for i in range(10):
	arr.append(i+1)


# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:

for i in arr:
    if i % 2 == 0:
        print(i)

# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1

# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {
    'name': 'jon',
    'age': 35,
    'city': 'New-York',
}
for key, value in person.items():
    print(key, value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in arr2:
    print(f"Lista: {list}")
    for elem in list:
        print(f"Elementul {elem}")

# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
arr3 = [x+1 for x in range(10)]
for i in arr3:
    print(i)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for index, item in enumerate(arr3):
    print(f"Elementul {item} cu indexul {index}")
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3]
for f, n in zip(fruits, numbers):
    print(f, n)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
arr4 = [x+1 for x in range(10)]
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
arr5 = [5, 6, 7]
print(arr5[0])
while arr5[0] < 50:
    for i in range(len(arr5)):
        arr5[i] *= 2
    print(arr5)

# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
number = 7
for i in range(1, 11):
    result = number * i
    print(result)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
arr6 = []
for i in range(6):
   for j in range(6):
        arr6.append([i,j])
print(arr6)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:

for i in arr6:
    if i[0] < i[1]:
        print(i)
    
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:

lisr_of_number=[3,45,3,1,33]
index = 0
gasit = False

while index < len(lisr_of_number):
    if lisr_of_number[index] > 10:
        print(lisr_of_number[index])
        gasit = True
        break
    index += 1
if not gasit:
    print("Nu exista valori mai mari decat 10")
  
        
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
num_stele = int(input('Introdu un numar'))

for i in range(1,num_stele+1):
    print("")
    for j in range(1,num_stele+1):
        print('*',end="")

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

for i in range(1,8):
    print('')
    for y in range(1,i):
        print(y,end="")
        
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(1, 6):
    for j in range(5, i-1,-1):
        print(j, end="")
    print()
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
some_sting= 'abcdefg'
dimen = len(some_sting)
for i in range(dimen):
    print(some_sting[i:dimen])

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
for i in range(8):
    if i % 2 ==0:
        for j in range(8):
            print('+-',end="")
    else:
        for j in range(8):
            print("-+",end="")
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
print("=========")

for i in range(1,7):
    for j in range(1,i):
        res = 3**j
        print(res, end=" ")
        
    
    print()

for i in range(7):
    for j in range(i+2,6):
        res = 3**j
        print(res, end=" ")
    print()

# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
