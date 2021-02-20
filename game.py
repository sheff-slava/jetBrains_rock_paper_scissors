import random


random.seed()
default_options = ('rock', 'paper', 'scissors')
default_beat_options = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
user_name = input('Enter your name: ')
score = 0
with open('rating.txt', 'r') as f:
    for line in f:
        if line.startswith(user_name):
            score = int(line.replace(user_name + ' ', ''))
print(f'Hello, {user_name}!')
options = list()
beat_options = dict()
list_of_options = input()
if list_of_options != '':
    options = list_of_options.split(',')
    beat_options = dict.fromkeys(options)
    for index, option in enumerate(options):
        new_list = options[index + 1:] + options[:index]
        new_list = new_list[:len(new_list) // 2]
        beat_options[option] = new_list
else:
    options = default_options
    beat_options = default_beat_options
print("Okay, let's start")
user_input = input()
while user_input != '!exit':
    if user_input == '!rating':
        print('Your rating:', score)
    elif user_input in options:
        option = random.choice(options)
        if option == user_input:
            score += 50
            print(f'There is a draw ({option})')
        elif option in beat_options[user_input]:
            print(f'Sorry, but the computer chose {option}')
        elif user_input in beat_options[option]:
            score += 100
            print(f'Well done. The computer chose {option} and failed')
    else:
        print('Invalid input')
    user_input = input()
print('Bye!')
