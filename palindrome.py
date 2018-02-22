import random
from time import time

lower_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
word_length = 4
how_many = 0
word = ''
start = time()

for j in range(1000000):
    # making a word
    for i in range(word_length):
        x = lower_letters[random.randint(0, 25)]
        word += x

    word_reverse = word[::-1]

    if word == word_reverse:
        how_many += 1
        print('{}th Palindrome: {}'.format(how_many, word))

    word = ''


end = time()
print('time:', end - start)
