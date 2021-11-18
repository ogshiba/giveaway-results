import random

with open('participants.csv') as file:
    participants = file.read().splitlines()

winners = random.sample(participants, 250)

with open('winners.csv', mode='a') as winners_file:
    for winner in winners:
        winners_file.write(f'{winner}\n')
