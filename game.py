# Hangman game in python - simple
import random
    
    
def game():
    secret_words = introduction()
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


def introduction():
    already = False
    while not already:
        secret_words = []
        print('Welcome to the Hangman game!')
        number_words = input('How much words do you want to play to, type a int number!')
        
        if number_words.isnumeric():
            number_words = int(number_words)
            already = True
            
            for i in range(number_words):
                secret_words.append(input('Type some words for another people to play!'))
    
    return secret_words

game()
