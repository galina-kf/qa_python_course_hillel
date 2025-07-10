# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1
people_records.insert(0, ('Halyna', 'Korotenko', 48, 'Test engineer', 'Kharkiv'))

# 2
people_records[1], people_records[5] = people_records[5], people_records[1]
for item in people_records:
    print(item)

# 3 Variant 1
check_items = [people_records[6], people_records[10], people_records[13]]

new_list = [x for x in check_items if x[2] >= 30]
if new_list.__len__() < check_items.__len__():
    print('\n Not all people in required list have age above 30')
print(f'The required people\'s with age above 30: {new_list}')

# 3 Variant 2
required_list = []
indexes = [6, 10, 13]

for i in indexes:
    if people_records[i][2] >= 30:
        required_list.append(people_records[i])
if required_list.__len__() < indexes.__len__():
    print("\nNot all people in required list have age above 30")
print(f'The required people\'s with age above 30: {required_list}')

# 3 Variant 3
indexes = [6, 10, 13]
for i in indexes:
    if people_records[i][2] >= 30:
        print(f'\n The person with age above 30: {people_records[i]}')
    else:
        print(f'\n The person with age not above 30: {people_records[i]}')
