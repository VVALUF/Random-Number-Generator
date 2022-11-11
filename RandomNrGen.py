import random
min_number = input('Min number: ')
if min_number.isdigit():
    min_number = int(min_number)
    if min_number <= 0:
        print('Must be bigger then 0')
        quit()
else:
    print('Type a number next time')
    quit()
max_number = input('Max number: ')
if max_number.isdigit():
    max_number = int(max_number)
    if max_number <= 0:
        print('Must be bigger then 0!')
        quit()
else:
     print('Type a number next time')
     quit()
random_number = random.randint(min_number, max_number)
print(random_number)