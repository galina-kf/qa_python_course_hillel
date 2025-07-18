# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0
    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
            # Increment the appropriate variable
            multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def numbers_sum(a, b):
    my_sum = a+b
    return my_sum


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def count_average(*args):
    average = sum(*args)/len(*args)
    print(average)
    return average


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_average(my_list)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reversed_string(string):
    my_list = list(string)
    i = 0
    new_list = []
    while i <= len(string)-1:
        new_list.append(my_list[-1-i])
        i += 1
    new_string = ''.join(new_list)
    print(new_string)
    return new_string


reversed_string('tam tuck puck')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(word_list):
    longest = max(word_list, key=lambda item: len(item))
    print(longest)


word_list = ['new', 'plane', 'pilots']
longest_word(word_list)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    index = str1.find(str2)
    if index is not None:
        return index
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7


str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
'''
Count the amount of symbols in the string
'''


def count_symbol(str, symbol):
    if str and symbol:
        symbol_count = str.count(symbol)
        print(f'\n Text contains letter {symbol} {symbol_count} times')
        return symbol_count
    else:
        print("No params to count symbol")


# task 8

''' 
We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
write code that will help us to get cars that satisfy search_criteria.
Cars should be sorted by price ascending.
We should print up to five (5) first found elements 
'''


def car_search(car_data, search_criteria, search_length):
    car_data_search = {}
    for name, description in car_data.items():
        if description[1] >= search_criteria[0] and description[2] >= search_criteria[1] and \
                description[4] <= search_criteria[2]:
            car_data_search[name] = description
    print(f'\nThe first {search_length} cars according to your search:\n')
    sorted_car_search = sorted(car_data_search.items(), key=lambda x: x[1][4])
    for item in sorted_car_search[:search_length]:
        print(item)

# task 9


'''
    Перевірте чи починається якесь речення з потрібної фрази.
'''


def get_phrase(line, phrase):
    i = 0
    for item in line:
        if item.startswith(phrase):
            index = line.index(item)
            print(f'\n The {index}th sentence starts with {phrase}')
            i += 1
    # to check how many sentences starts with phrase
    if i != 0:
        print(f'\n {i} sentence(s) start with {phrase}')


# task 10


def get_unique_symbol(string):
    if len(string) and not string.isspace():
        s_list = []
        for symbol in string:
            if symbol != ' ':
                if symbol not in s_list:
                    if string.count(symbol) > 10:
                        print(f'This symbol {symbol} presents more than 10 times in your string')
                        print(True)
                    else:
                        print(f'This symbol {symbol} presents 10 or less times in your string')
                        print(False)
                    # add the counted symbols to prevent duplicates
                    s_list.append(symbol)
    else:
        print("Your string does not contain any symbols to count")


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""