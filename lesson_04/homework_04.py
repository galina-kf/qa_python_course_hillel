adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawyer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawyer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")
print(adventures_of_tom_sawyer)

# task 02 ==
""" Замініть .... на пробіл
"""

adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", "")
print(adventures_of_tom_sawyer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("  ", "")
print(adventures_of_tom_sawyer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

i = 0
for item in adventures_of_tom_sawyer:
    if item == "h":
        i += 1
print(f'\n Text contains letter h {i} times')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

i = 0
for item in adventures_of_tom_sawyer:
    if item.isupper():
        i += 1
print(f'\n Text contains {i} words that start with capital letter')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

# this variant shows the position of the first letter of "Tom" second time
index_1 = adventures_of_tom_sawyer.find("Tom")
index_2 = adventures_of_tom_sawyer.find("Tom", index_1+1)
print(f'\n The word Tom second time is placed on {index_2} position')

# this variant shows the position of word "Tom" second time in text
new_string = adventures_of_tom_sawyer.split()
index_list = []
i = None
for item in new_string:
    if item == 'Tom':
        i = new_string.index('Tom')
        index_list.append(i)
        new_string.pop(i)
if index_list.__len__() >= 2:
    print(f'\n The word Tom second time is on {index_list[1]}th position')
else:
    print('\n The word "Tom" exists in the text only once')


# task 07
""" Розділіть змінну adventures_of_tom_sawyer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawyer_sentences
"""
#
adventures_of_tom_sawyer_sentences = []
new = adventures_of_tom_sawyer.strip(".").split(".")
for item in new:
    adventures_of_tom_sawyer_sentences.append(item.strip()+".")
print(adventures_of_tom_sawyer_sentences)


# task 08
""" Виведіть четверте речення з adventures_of_tom_sawyer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adventures_of_tom_sawyer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

i = 0
for item in adventures_of_tom_sawyer_sentences:
    if item.startswith("By the time"):
        index = adventures_of_tom_sawyer_sentences.index(item)
        print(f'\n The {index}th sentence starts with "By the time"')
        i += 1
# to check how many sentences starts with "By the time"
if i != 0:
    print(f'\n {i} sentence(s) start with "By the time"')

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawyer_sentences.
"""

print(f'\n The last sentence contains {adventures_of_tom_sawyer_sentences[-1].split().__len__()} words')
