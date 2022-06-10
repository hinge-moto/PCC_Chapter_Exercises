# April 22.2022

ass = 'phat'

print("Is ass == phat? I predict True")
print(ass == 'phat')

print("\nIs ass == slappin? I predict False")
print(ass == 'slappin')

print("\nIs ass == phat and slappin? I predict True")
print((ass == 'phat') and (ass == 'slapping'))


ass_list = [ass]

print()
print(ass_list)

ass_list.append('slappin')
print(ass_list)

if 'slappin' in ass_list:
    print("\nTruly this ass slaps")

if 'slappin' and 'phat' in ass_list:
    ass_list.append('thicc')
    print("\nAppending thiccness")
    print(ass_list)
    print("This thiccness is sickening")
