print("Написати Python-скрипт для переведення натурального числа з десяткової"
      " системи числення у шістнадцятирічну.")
num__10 = int(input("Введіть ваше десяткове число: "))
num = num__10
hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
num__16list_1 = []
while num__10 > 0:
    num__16list_1.append(hex[num__10 % 16])
    num__10 = num__10 // 16

sizeRev = -(len(num__16list_1)) - 1
i = -1
num__16list_2 = []
while i > sizeRev:
    num__16list_2.append(str(num__16list_1[i]))
    i -= 1

num__16 = "".join(num__16list_2)
print("\nВаше число у десяткові системі числення: %d\nВаше число у шістнадцятковій системі числення: %s" % (
num, num__16))
