#Создайте новую функцию def test... с произвольным числом параметров разного типа,
# функция должна распечатывать эти параметры внутри своего тела

def test(a, b, c):
    print(a, b, c)


list_ = [1.1, 2]
disk_ = {'c': "str"}
test(*list_, **disk_)

#Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре
def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)


print(faktorial(6))
