# April 24.2022

users = ['admin', 'adrian', 'dale', 'constance', 'fred']
#users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, computer loves you")
        else:
            print("Hello " + user.title() + ", welcome back!")
else:
    print("We need to find some users!")
