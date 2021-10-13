import numpy as np

def Output():
    res = np.array([
        "I saw a " + adjective + ' ' + noun + ' ' + verb + " his ball",
        "The " + adjective + ' ' + noun + ' ' + verb + " over a lazy dog",
        "My " + adjective + ' ' + noun + ' ' + verb + " me ice cream",
    ])

    print(res[num])

paragraphs = np.array([
    "I saw a " + '____ ' + ' ____ ' + ' ____' + " his ball",
    "The " + '____ ' + ' ____ ' + ' ____' + " over a lazy dog",
    "My " + '____ ' + ' ____ ' + ' ____' + " me ice cream",
])

num = 0

input('>>>> Press Enter to play!')

print('Welcome to the Game!You have to fill the empty spaces in the paragraph bellow\n')
print(paragraphs[num])

adjective = input('Enter an adjective: ')
noun = input('Enter a noun: ')
verb = input('enter a verb: ')

print('\n')
print('Your Mad Lib: ')
print('##############')
Output()

flag = True

while flag:
    input('Press Enter for the next one!')
    num += 1
    print(paragraphs[num])
    adjective = input('Enter an adjective: ')
    noun = input('Enter a noun: ')
    verb = input('enter a verb: ')
    Output()

    if num == 2:
        print('WELL DONE!')
        exit()
