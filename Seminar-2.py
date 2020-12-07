
#Задача 1

start = "AEfghfgTEgGFBhjaqQ"

alphabet = "abcdefghijklmnopqrstuvwxyz" 

start = start.lower()

foo = {}

for i in start:
    if i in alphabet:
        foo[i] = start.count(i)
    m = max(foo.values())
    cont = m
    l = []
    for key in foo:
        if foo[key] == cont:
            l.append(key)

    l = sorted(l)

print(l[0])

#Задача 2

str = "test 2 order lol top 1 round 3"
count = 0
for element in str.split():
    if element.isalpha():
        count = count + 1
    else:
        count = 0
    if count >= 3:
        print("Имеется последовательность из 3 букв")


# Задача 3

str = "aaaabbbcc"
foo = ''
i = 0
array = []

for j in str:
    if foo == j or foo == '':
        i += 1
        array.append(i)
        foo = j
    else:
        i= 1
        foo = j

print(max(array))

#Задача 4

str = "HELL nO"
foo = []

for element in str:
    if element.isupper():
        foo.append(element)

str = ''.join(foo)
print(str)

#Задача 5

array = [4,4,6,4,2,2,4,6]

result = []
for x in [x for i, x in enumerate(array) if i == array.index(x)]:
  result.extend([x]*array.count(x))
   
print(result)


#Задача 6

array = [1,2,4,5]
unique = [3]

array.append(unique[0]) #добавим наше уникальное значение в общий массив

array.sort() #отсортируем наш массив в порядке возрастания

position = array.index(unique[0]) #узнаем на какой позиции в отсортированном массиве стоит наш уникальный элемент

if(position == 0): #если наш уникальный элемент занял первую позицию значит ближйшийй ближайший будет больше его
    print(array[position + 1])
elif(position == len(array)): #если наш уникальный элемент оказался в конце то значит ближайший меньше его
    print(array[position - 1])
else: #в остальном случае уникальный элемент может оказаться в центре значит берем меньший
    print(array[position - 1])











