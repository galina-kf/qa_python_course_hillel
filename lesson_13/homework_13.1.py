import csv

with open('random.csv', newline='') as r, open('random-michaels.csv', newline='') as rm:
    reader_r = list(csv.reader(r))
    reader_rm = list(csv.reader(rm))

    # remove duplicate in random.csv
    new_r = []
    for item in reader_r:
        if item not in new_r:
            new_r.append(item)
    print(new_r)

    # remove duplicate in random-michaels.csv
    new_rm = []
    for item in reader_rm:
        if item not in new_rm:
            new_rm.append(item)
    print(new_rm)

    # create a new list with unique records
    for item in new_r:
        if item not in new_rm:
            new_rm.append(item)
    print(new_rm)

# write new data to the result file
with open('result_korotenko.csv', mode='a', newline='') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerows(new_rm)













