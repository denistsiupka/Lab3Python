print("Написати Python-скрипт, що буде обчислювати факторіал заданого"
      " користувачем натурального числа n.")
n = int(input("Введіть ваше число: "))
num = n
factorial = 1
for i in range(0, num):
    factorial = factorial * n
    n -= 1
print("Факторіал вашого числа %d: %d" % (num,factorial))
