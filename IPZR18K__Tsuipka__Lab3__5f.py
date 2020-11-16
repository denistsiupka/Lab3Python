def decTransformHex(num__10):
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    num__16list = []
    while num__10 > 0:
        n = hex[num__10 % 16]
        num__16list.append(str(n))
        num__10 = num__10 // 16
    num__16list.reverse()
    num__16 = "".join(num__16list)
    return num__16

print("Написати Python-скрипт для переведення натурального числа з десяткової"
      " системи числення у шістнадцятирічну.")
num__10 = int(input("Введіть ваше десяткове число: "))
num__16 =  decTransformHex(num__10)
print("\nВаше число у десяткові системі числення: %d\nВаше число у шістнадцятковій системі числення: %s" % (
num__10, num__16))











