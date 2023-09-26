text = "Текст ..."

words = text.split()

word_count = {}

for _ in words:
    if _ in word_count:
        word_count[_] += 1
    else:
        word_count[_] = 1

print(word_count)
