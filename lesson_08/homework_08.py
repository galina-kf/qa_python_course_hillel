my_list = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']


def get_sum(str):
    sum=0
    try:
        for i in str.split(','):
            sum += int(i)
        print(sum)
    except ValueError:
        print(f'Cannot get Sum for {i}')
    return sum


def find_elem_sum(list):
    for item in list:
        get_sum(item)


find_elem_sum(my_list)