# May 19.2022

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('dylan', 'mcdonald',
                           location='edmonton',
                           field='fapping',
                           skin='very nice')
print(my_profile)
for k, v in my_profile.items():
    print(f"This is my {k}, and this is my {v}.")
    print(f"{k.title()}: {v.title()}\n")
