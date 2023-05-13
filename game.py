# Hangman game in python - simple
import random

secret_words = ['car', 'man']
print('Welcome to the Hangman game!')

word_time = random.choice(secret_words)
word_hit = '_' * len(word_time)
hits = ''
while True:
    print(word_hit)

    hit = input('Type a word or a letter:\n')

    if hit in word_time:
        hits += f'{hit}'
    
    word_hit = ''
    for letter in word_time:
        if letter in hits:
            word_hit += f'{letter}'
        else:
            word_hit += '_'
        
    if word_hit == word_time:
        print(f'You hit this word!\n the word is {word_time}')
        break

    if hit == word_time:
        print(f'You hit this word!\n the word is {word_time}')
        break


