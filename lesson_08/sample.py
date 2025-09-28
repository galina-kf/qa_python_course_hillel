def calculate_sum_from_file(filename):
    sum = 0
    try:
        with open(filename) as f:
            for line in f:
                try:
                    sum += int(line)
                except ValueError:
                    return "Invalid data in the file"
        return sum

    except FileNotFoundError:
        return "File not found"

