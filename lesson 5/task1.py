import random
#Написать функцию-генератор rand_nums,
#генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно).
#Количество чисел N, которое выдаст генератор передается в функцию через параметр:
#>>> rand15 = rand_nums(15)
#>>> next(rand15) # 1-й вызов
#11
#>>> next(rand15) # 2-й вызов
#38
#...
#>>> next(rand15) # 15-й вызов
#7
#>>> next(rand15) # 16-й вызов
#...StopIteration...

def rand_nums(num):
    while num > 0:
        num -= 1
        number = random.randrange(1, 100)
        yield number

rand15 = rand_nums(15)
print(next(rand15))     #1
print(next(rand15))     #2
print(next(rand15))     #3
print(next(rand15))     #4
print(next(rand15))     #5
print(next(rand15))     #6
print(next(rand15))     #7
print(next(rand15))     #8
print(next(rand15))     #9
print(next(rand15))     #10
print(next(rand15))     #11
print(next(rand15))     #12
print(next(rand15))     #13
print(next(rand15))     #14
print(next(rand15))     #15
print(next(rand15))     #16








