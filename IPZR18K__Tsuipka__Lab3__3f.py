def newArr(arr, size, i=0):
    if i == size:
        return arr
    num = int(input(" Введіть своє число для елемента під індексом %d : " % (i + 1)))
    arr.append(num)
    return newArr(arr, size, i + 1)

def revArr(arr, sizeArr, arrRev, i=-1):
    if i == -(sizeArr) - 1:
        return arrRev
    arrRev.append(arr[i])
    return revArr(arr, sizeArr, arrRev, i - 1)


print("Написати Python-скрипт, що буде повертати задану послідовність чисел у"
      "зворотному порядку.")
array = []
size = int(input("Введіть розмір масиву:"))
newArr(array, size)

arrayRevers = []
revArr(array, size, arrayRevers)

print("\nВаш масив, який ви ввели " + str(array))
print("\nВаш зворотний масив " + str(arrayRevers))
