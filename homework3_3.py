#Создайте новую функцию def test... с произвольным числом параметров разного типа,
# функция должна распечатывать эти параметры внутри своего тела

def test(*args):
    print(*args)


test(5.4, 54, 'str', False)

#Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре
def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)


print(faktorial(6))
