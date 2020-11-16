print("Написати Python-скрипт, що буде обчислювати індекс максимального елемента"
      " масиву n*n, де 1<=n<=5")

n = int(input("Введіть ваше число n: "))

if (n >= 1 and n <= 5):
    size = n * n
    array = []
    i = 0
    while i < size:
        num = int(input(" Введіть своє число для елемента під індексом %d : " % (i + 1)))
        array.append(num)
        i += 1
    x = 0
    j = 0
    for i in range(len(array)):
        if array[i] > x:
            x = array[i]
            j = i

    print("\nВаш масив, який ви ввели " + str(array))
    print("Макс. Елемент: %d. Його індекс %d" % (x, j))
else:
    print("1<=n<=5")
