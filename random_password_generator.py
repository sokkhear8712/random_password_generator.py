import random
import string

# Задаем длину пароля
length = 12

# Генерируем пароль
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Выводим пароль на экран
print(password)
