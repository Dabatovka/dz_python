# Задача 1. Найдите сумму цифр трехзначного числа.


a = int(input("Введите трехзначное число: "))
s = ((a % 10) + (a % 100//10) + (a//100))
print(s)