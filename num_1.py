# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток,
#  которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

n = int(input('введите количество монет ='))
print('введите значение для каждой монеты (0/1)')
m = 0
for i in range(n):
    a = int(input())
    if a == 1:
        m += 1
print('минимальное количество переворотов')
print(m if m<n/2 else n-m)
