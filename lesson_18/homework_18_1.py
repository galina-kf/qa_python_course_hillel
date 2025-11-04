import random

# Генератор парних чисел
numbers = random.randrange(100)
even_numbers = [x for x in range(numbers) if x%2 == 0]
print(f"List of even numbers: {even_numbers}")


# Генератор чисел Фібоначчі
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(10):
    print(next(fib))