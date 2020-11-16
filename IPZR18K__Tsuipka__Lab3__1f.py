def fact(a):
    if a == 0:
        return 1
    else:
        return fact(a-1)*a

print("Написати Python-скрипт, що буде обчислювати факторіал заданого"
      " користувачем натурального числа n.")
n = int(input("Введіть ваше число: "))
num = n
result = fact(n)
print("Факторіал вашого числа %d: %d" % (num,result))

