string = input("Your string: ")


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


get_unique_symbol(string=string)

