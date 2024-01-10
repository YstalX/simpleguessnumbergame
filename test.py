import random
import time

game1 = random.randint(0, 10)  # значение от 0 до 10
game2 = random.randint(0, 20)  # значение от 0 до 20
game3 = random.randint(0, 100)  # значение от 0 до 100
num = 2
print(game1, game2, game3, "DEBUG")

print('Первый Режим - от 0 до 10')
print('Второй Режим - от 0 до 20')
print('Третий Режим - от 0 до 100')
time.sleep(1)
guess = int(input('Выберите режим игры : '))

if guess == num:
   print('Вы выбрали второй режим')# Начало нового блока
   time.sleep(1)
   guess2 = int(input('Выберите число : '))
   if guess2 == game2:
    print('Вы угадали!!!')
   else:
    print("Вы не угадали,загаданное число  было - ", game2)  
elif guess < num:
   print('Вы выбрали первый режим') # Ещё один блок
   time.sleep(1)
   guess1 = int(input('Выберите число : '))
   if guess1 == game1:
    print('Вы угадали!!!')
   else:
    print("Вы не угадали,загаданное число было - ", game1) 
# Внутри блока вы можете выполнять всё, что угодно ...
else:
   print('Вы выбрали третий режим')
   time.sleep(1)
   guess3 = int(input('Выберите число : '))
   if guess3 == game3:
    print('Вы угадали!!!')
   else:
    print("Вы не угадали,загаданное число было - ", game3) 