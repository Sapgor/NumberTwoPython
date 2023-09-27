def rectangle_area(width, height):
    return width * height
while True:
        print("вычисление площади прямоугольника")
        try:
            width = int(input("Введите ширину: "))
            if width < 1:
                print ("Ошибка: введено отрицательное число или 0")
                continue
            else:
                height = int(input("Введите высоту: "))
                if height < 1:
                    print ("Ошибка: введено отрицательное число или 0")
                    continue
                else:
                    print("Результат:", rectangle_area(width, height))
        except ValueError:
            print("ошибка введено не число")