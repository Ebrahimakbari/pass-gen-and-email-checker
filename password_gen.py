import random
import string

while True:
    def get_setting():
        user_setting = input(
            'please enter setting[password len , is upper , is lower , is digit , is symbol , is space]: ').split(',')
        return user_setting

    def upper_pass():
        return random.choice(string.ascii_uppercase)

    def lower_pass():
        return random.choice(string.ascii_lowercase)

    def digit_pass():
        return random.choice(string.digits)

    def symbol_pass():
        return random.choice(string.punctuation)

    def space_pass():
        return ' '
    
    def check_setting(sett):
        set_of_main = {1: upper_pass(), 2: lower_pass(), 3: digit_pass(), 4: symbol_pass(), 5: space_pass()}
        
        def decide(item):
            a , b = item
            return sett[a] == 'true'
        set_of_main = dict(filter(decide , set_of_main.items()))
        return set_of_main

    def create_random_place(sett):
        password = []
        check_set = check_setting(sett)

        while len(password) < int(sett[0]):
            sets = list(check_set.keys())
            random.shuffle(sets)

            for i in range(int(sett[0])):
                if i >= len(sets):
                    password.append(random.choice(
                        list(check_setting(sett).values())))

                else:
                    password.append(check_set[(sets)[i]])

        return password

    get_sett = get_setting()
    flag = False
    flag1 = False
    for item in get_sett:
        if item == 'done':
            print('program finished')
            flag1 = True
        elif not (item.isdigit()) and item not in ['true', 'false', 'done']:
            flag= True
            break
    if flag == True:
        print('invalid input!!! , try again')
        continue
    elif flag1 == True:
        break

    def run_me():
        final_pass = create_random_place(get_sett)
        print(f'password is =   {''.join(final_pass)}')
        print(f'password is =   {final_pass}')

    run_me()
