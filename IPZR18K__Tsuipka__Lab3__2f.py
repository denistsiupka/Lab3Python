def size(n):
    if (n >= 1 and n <= 5):
        n *= n
        return n
    else:
        print("1<=n<=5")


def maxArr(array):
    x = 0
    j = 0
    for i in range(len(array)):
        if array[i] > x:
            x = array[i]
            j = i
    return j


def newArr(arr, size, i=0):
    if size == i:
        return arr
    else:
        num = int(input(" Введіть своє число для елемента під індексом %d : " % (i + 1)))
        arr.append(num)
        return newArr(arr, size, i + 1)


print("Написати Python-скрипт, що буде обчислювати індекс максимального елемента"
      " масиву n*n, де 1<=n<=5")
size = size(int(input("Введіть ваше число n: ")))
arr = []
arr = newArr(arr, size)
index = maxArr(arr, size)
print("\nВаш масив, який ви ввели " + str(arr))
print("Макс. Елемент: %d. Його індекс %d" % (((arr[index])), index))
