adwentures_of_tom_sawer = """\
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_ver1 = adwentures_of_tom_sawer.replace("\n", " ")
print(f"1. Print the next version 1.0: {adwentures_of_tom_sawer_ver1}")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_ver2 = adwentures_of_tom_sawer_ver1.replace("....", " ")
print(f"2. Print the next version 2.0: {adwentures_of_tom_sawer_ver2}")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_ver3 = ' '.join(adwentures_of_tom_sawer_ver2.split())
print(f"3. Print the next version 2.0: {adwentures_of_tom_sawer_ver3}")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
random_list = list(adwentures_of_tom_sawer_ver3)
count_random_letter = []
for letter in random_list:
    if letter == "h":
        count_random_letter.append(letter)
print(f"4. Search for the number of letters 'h': {len(count_random_letter)} times")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer_new = adwentures_of_tom_sawer_ver3.replace('"', "")
words = adwentures_of_tom_sawer_new.split()
capitalized_words = []
for w in words:
    if w[0].isupper():
        capitalized_words.append(w)
print(f"5. The number of words in the text begins with a capital letter: {len(capitalized_words)} times")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
random_word = adwentures_of_tom_sawer_ver3.split()
all_indexes = []
for i in range(0, len(random_word)) :
    if random_word[i] == "Tom" :
        all_indexes.append(i)
print(f"6. The index of the second element 'Tom' : {all_indexes[1]} position")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_ver3.split(". ")[-1]
print(f"7. Save last sentences: {adwentures_of_tom_sawer_sentences}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentences = adwentures_of_tom_sawer_sentences.split(", ")[-1].lower()
print(f"8. The fourth sentences in lower case: {fourth_sentences}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

some_sentences = adwentures_of_tom_sawer_ver3.split(". ")
for sentence in some_sentences:
    if sentence.startswith("By the time"):
        print("9. Yes, the sentence starts with a 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
some_words = adwentures_of_tom_sawer_sentences.split()
print(f"10. The number of words in a sentence: {len(some_words)}")