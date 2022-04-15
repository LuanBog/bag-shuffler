import random
import time

def shuffle_bag():
    contents = []

    with open('./bag.txt', 'r', encoding='utf-8') as bag:
        for line in bag.readlines():
            contents.append(line)

        random.shuffle(contents)

    with open('./bag.txt', 'a') as bag:
        bag.truncate(0)

        for content in contents:
            bag.write(content)
        
    print('Shuffled!')

if __name__ == '__main__':
    try:
        amount = int(input('[1] Shuffle amount: '))
    except ValueError:
        amount = 1

    if amount <= 0:
        amount = 1

    print('')
    for i in range(amount):
        shuffle_bag()
        time.sleep(0.125)
