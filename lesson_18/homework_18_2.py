# Ітератор, що повертає лист у зворотньому напрямку

def reversed_list(list):
    i = 0
    new_list = []
    while i <= len(list)-1:
        new_list.append(list[-1-i])
        i += 1
    print(new_list)
    return new_list


list_numbers = [11, 12, 13, 14, 15]
reversed_list(list_numbers)

# Ітератор парних чисел
class EvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num and self.current % 2 == 0:
            self.current += 2
            return self.current
        else:
            raise StopIteration


my_iterator = EvenNumbers(32)
for num in my_iterator:
    print(num)

my_iterable = iter([1, 2, 3, 4, 5])

# Прохід по ітератору вручну
print(next(my_iterable))  # Виведе: 1
print(next(my_iterable))  # Виведе: 2
print(next(my_iterable))  # Виведе: 3
print(next(my_iterable))  # Виведе: 4
print(next(my_iterable))

my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(f"{index}: {value}")