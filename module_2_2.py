first = int(input('Введите первую цифру: '))
second = int(input('Введите вторую цифру: '))
third = int(input('Введите третью цифру: '))
if first == second == third:
    print(3)
elif first == second or second == third or third ==first:
    print(2)
else:
    print(0)