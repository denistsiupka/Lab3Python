def isPrime(num, i=2):
    if (i * i > num) and (num % i != 0) :
        return num
    elif (num % i == 0):
        return 0
    else:
        return isPrime(num, i + 1)


print("Написати Python-скрипт, що визначатиме чи є задане натуральне число"
      " простим. Простим називається число, що більше за 1 та не має інших дільників,"
      " окрім 1 та самого себе)")
num = int(input("Введіть ваше число n: "))
if (isPrime(num) == num):
    print("Ваше число n є просте: %d " % (num))
else:
    print("Ваше число n не є просте: %d " % (num))
