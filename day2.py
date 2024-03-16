phrase = 'Neno is me'.title().split()

test = 'Nemo' in phrase

if test == True:
    print(f'I found Nemo at {phrase.index('Nemo')+1}')
else:
    print("I can't find Nemo :(")

