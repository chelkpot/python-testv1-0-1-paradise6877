# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
numbers = [2, 3, 4]

squares = []
for num in numbers:
    squares.append(num * num)

print("Числа:", numbers)
print("Квадраты:", squares)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
