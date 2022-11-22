# Задача 4: Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print("Введите номер координатной четверти от 1 до 4: ")
fourQuadrant  = int(input())
if fourQuadrant == 1:
    print("x(0 , оо)  y (0 , oo)")
elif fourQuadrant == 2:
    print("x(-oo , 0)  y (0 , oo)")
elif fourQuadrant == 3:
    print("x(-oo , 0)  y (-oo , 0)")
elif fourQuadrant == 4:
    print("x(0 , оо)  y (-oo , 0)") 