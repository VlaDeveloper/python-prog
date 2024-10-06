animals = [
    ['small panda', 'owl', 'spider', 'wolf', 'flamingo', 'coati'],
    ['bear', 'manul', 'golden eagle', 'big panda'],
    ['goose']
]

def print_neighbours(group, index):
    if group >= len(animals):
        print(f'Incorrect group')
        return
    elif index >= len(animals[group]):
        print(f'Incorrect index')
        return

    if len(animals[group]) > 1:
        print(f'The neighbours of the {animals[group][index]} are {animals[group][index-1]} and {animals[group][index+1]}')
    else:
        print(f'There are no neighbours for the {animals[group][index]}')

if __name__ == '__main__':
    user_group = int(input('Enter the group of an animal: '))
    user_index = int(input('Enter the index of an animal: '))
    print_neighbours(user_group, user_index)
