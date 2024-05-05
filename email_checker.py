import re
print(
    '\n*** valid email length is [5:15] and have lower,upper,digit or "_" ***\n')
email = input('please enter your email: ')
state = re.search(r'[a-zA-Z0-9_]{5,15}@[a-zA-Z]+\.[a-zA-Z]{2,3}', email)
if state == None:
    print('not a valid email!!!')
else:
    print('valid email!!')
