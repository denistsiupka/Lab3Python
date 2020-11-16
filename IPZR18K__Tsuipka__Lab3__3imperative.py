print("Написати Python-скрипт, що буде повертати задану послідовність чисел у"
      "зворотному порядку.")
size = int(input("Введіть розмір масиву:"))
array = []
i = 0
while i < size:
    num = int(input(" Введіть своє число для елемента під індексом %d : " % (i + 1)))
    array.append(num)
    i += 1

arrayRevers = []
i = -1

while i > -(size) - 1:
    num = array[i]
    arrayRevers.append(num)
    i -= 1
print("\nВаш масив, який ви ввели " + str(array))
print("\nВаш зворотний масив " + str(arrayRevers))

