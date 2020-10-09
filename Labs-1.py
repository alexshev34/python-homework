# # Задача1

array = [23,56,345,6786,45645,6676,7878]

print(array[0])
print(array[2])
print(array[-2])

# # Задача 2

array = [23,45,78,9,10,15]
N = 3
if(len(array) - 1 <N):
    print(-1)

else:
    print(array[N]**N)

# Задача 3

string = "сбербанк"
symbol = 'б' 
number = string.rfind(symbol)
print (number) 

 

# # Задача 4

array = int(101100110100)
i = 0
while array % 10 == 0:
    array = array // 10
    i += 1
print(i)

# # Задача 5

string = "python"
print(string[::-1])

# # Задача 6

array = [7,7,7,7]
number = array[1]
j = False
for key in array:
    if(key != number):
        j = True

print(j)

# #Задача 7

def password(data: str) -> bool:
    return len(data) > 16 and all(re.search(p, data) for p in ('[AZ]', '\d', '[az]'))

#Задача 8

array=[[[555]], [9, [5, 2, [8], 8, 8, 4], 3]]
def flat_list(array, new_list=[]):
    for i in array:
        if type(i) == int:
            new_list.append(i)
        else:            
            flat_list(i)
    return new_list
print(flat_list(array))

#Задача 9

stats = {'a':5.1, 'b':2.2, 'c': 3.7}
inverse = [(value, key) for key, value in stats.items()]
print(max(inverse)[1])

# #Задача 10

data= [2,4,5,7,1,1,2]
result = []
for i in data:
    if data.count(i) > 1:
        result.append(i)
print(result)


