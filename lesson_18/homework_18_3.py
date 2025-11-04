import logging
import pytest

# Створення та налаштування логера
logging.basicConfig(
    filename='login_function.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    force=True
)
logger = logging.getLogger("log_event")


# Декоратор логування
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Test arguments: {args, kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Test result: {result}")
        return func(*args, **kwargs)
    return wrapper


# Декоратор виключень
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError as er:
            logging.error(f"Error raises: {er}")
        return func(*args, **kwargs)
    return wrapper


my_list = [1, 2, 3, 4, 5]
error_list = {1, 2, 3, 4, 5}

@logging_decorator
@exception_decorator
def reversed_list(list):
    i = 0
    new_list = []
    while i <= len(list)-1:
        new_list.append(list[-1-i])
        i += 1
    return new_list


reversed_list(my_list)

reversed_list(error_list)
